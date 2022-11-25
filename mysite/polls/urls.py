from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('osoby/', views.osoba_list),
    path('osoby/<int:pk>/', views.osoba_detail),
    path('osoby/<int:pk>/details', views.osoba_view),
    path('osoby/<int:pk>/team_squad', views.osoba_teamSquad),
    path('osoby/<int:pk>/update', views.osoba_update),
    path('osoby/<int:pk>/remove', views.osoba_remove),
    path('osoby/<str:input>/', views.osoba_namefit),
    path('druzyny/', views.druzyna_list),
    path('druzyny/<int:pk>/', views.druzyna_detail),
    path('druzyny/<int:id>/czlonkowie', views.druzyna_teammates),
    path('login/', include('rest_framework.urls')),
]