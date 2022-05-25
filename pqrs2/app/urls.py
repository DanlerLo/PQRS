from django.urls import path
from .views import home, about, blog, portfolio, registros, agregar_producto, listar_producto, modificar_producto, eliminar_producto, peticiones, quejas, reclamos, sugerencias, post, profile
urlpatterns = [
    path('', home, name='home'),
    path('about/' , about, name='about'),
    path('blog/' , blog, name='blog'), 
    path('portfolio/' , portfolio, name='portfolio'),
    path('contact/' , registros, name='registros'),
    path('agregar-producto/' , agregar_producto, name='agregar_producto'),
    path('listar-producto/' , listar_producto, name='listar_producto'),
    path('modificar-producto/<id>' , modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<id>' , eliminar_producto, name='eliminar_producto'),
    path('peticiones/', peticiones, name='peticiones'), 
    path('quejas/', quejas, name='quejas'),
    path('reclamos/', reclamos, name='reclamos'),
    path('sugerencias/', sugerencias, name = 'sugerencias'),
    path('post/', post, name='post'),
    path('profile/', profile, name='profile')
    
    


]
