from django.contrib.auth import views as auth_views
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
    path('add_institution/', views.add_institution, name='add_institution'),  # URL to display the form
    path('institution_success/', views.institution_success, name='institution_success'),  # Success page
    path('add_student/', views.add_student, name='add_student'),
    path('student_success/', views.student_success, name='student_success'), 
    path('load_institutions/', views.load_institutions, name='load_institutions'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
        # path("check-student-uniqueness/", views.check_student_uniqueness, name="check_student_uniqueness"),
]