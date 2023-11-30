from django.urls import include, path
from . import views
from teacher.views import teacher_all

app_name='school'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('', views.product_all, name='school_home'),

]
