from django.urls import path, include
from . import views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('osoby/', views.osoba_list),
    path('osoby/<int:pk>/', views.osoba_detail),
    path('osoby/<str:input>/', views.osoba_namefit),
    path('druzyny/', views.druzyna_list),
    path('druzyny/<int:pk>/', views.druzyna_detail),
]