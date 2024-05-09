from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('caeser', views.caeser, name='caeser'),
    path('autokey', views.autokey, name='autokey'),
    path('playfair', views.playfair, name='playfair'),
    path('des', views.des, name='des'),
    path('rsa', views.rsa, name='rsa'),
    path('modulo', views.modulo, name='modulo'),
    path('congruence', views.congruence, name='congruence'),
    path('permutation', views.permutation, name='permutation'),
]

