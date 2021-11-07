from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/checkout',views.cart_checkout.as_view(),name='checkout')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)