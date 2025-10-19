from django.urls import path

from . import views 


urlpatterns = [path('',views.index, name='index'),
                path('travel_destination.html', views.travel_destination, name='travel_destination'),
                path('contact/', views.contact, name='contact'),
                ]
                 
