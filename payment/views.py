import json
import os

import stripe
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.conf import settings

from basket.basket import Basket
from orders.views import payment_confirmation


def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'payment/orderplaced.html')


class Error(TemplateView):
    template_name = 'payment/error.html'


@login_required
def BasketView(request):

    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    stripe.api_key = settings.STRIPE_SECRET_KEY
    # stripe.api_key = 'sk_test_51LKoAzK9hbEX1KOtYXq3k2cFnNygJMq15I9ZtILjc4UTVTvkkPZd9HaLyMo6GysfGJEM4h7bLFxwdjzjIQgFgFcn00sT22AT0m'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )

    return render(request, 'payment/payment_form.html', {'client_secret': intent.client_secret, 
                                                        'STRIPE_PUBLISHABLE_KEY': os.environ.get('STRIPE_PUBLISHABLE_KEY')})

    # return render(request, 'payment/payment_form.html', {'client_secret': intent.client_secret, 
    #                                                     'STRIPE_PUBLISHABLE_KEY': 'pk_test_51LKoAzK9hbEX1KOtVKFvweQLHfZC2PF850eqOuBNoxGfbqHjVVLoANJ6W7y4cBP3cjzJ2wRQ2mS8dWiyFneNkUP3000IFikGh6'})


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_confirmation(event.data.object.client_secret)

    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)