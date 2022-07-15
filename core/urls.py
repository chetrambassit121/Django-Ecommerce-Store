import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("store.urls"), name="store"),
    path("basket/", include("basket.urls"), name="basket"),
    # path("payment/", include("payment.urls", namespace="payment")),
    path("account/", include("account.urls"), name="account"),
    path("orders/", include("orders.urls"), name="orders"),
    path("__debug__/", include(debug_toolbar.urls)),
    path("checkout/", include("checkout.urls"), name="checkout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
