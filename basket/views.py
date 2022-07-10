from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from store.models import Product




def basket_summary(request):
    return render(request, 'store/basket/summary.html')