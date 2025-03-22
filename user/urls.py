from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('log_in',views.log_in,name='log_in'),
    path('sing_on',views.sing_on,name='sing_on'),
    path('add_contact',views.add_contact,name='add_contact'),
]