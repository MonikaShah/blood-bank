from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    path('organizer/', views.organizer, name='organizer'),
    path('services/', views.services, name='services'),
    path('donor/', views.donor, name='donor'),
    path('other-activities/', views.other_activities, name='other_activities'),
    path('gallery/', views.gallery, name='gallery'),
    path('thalassemia/', views.thalassemia, name='thalassemia'),
    path('contact/', views.contact, name='contact'),
    path('donation/', views.donation, name='donation'),
]