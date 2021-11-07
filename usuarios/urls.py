from django.urls import path
from usuarios import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [


    path('', views.CrearUsuario.as_view(),name='register'),
    path('login/', views.IndexView.as_view(),name='login'),
    path('login/salir/', views.LogOut),
    path('update/', views.profile, name = 'update'),
    path('reporte/', views.reporte, name = 'reporte'),
    path('inventario/', views.inventario, name = 'inventario'),
    path('productos/', login_required(login_url='/register/login/')(views.add_product.as_view()), name='productos')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
