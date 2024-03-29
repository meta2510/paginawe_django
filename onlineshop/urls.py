from django.urls import path
from onlineshop import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "onlineshop"

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/',views.product_detail,name='product_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)