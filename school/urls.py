from django.urls import include, path
from . import views

app_name = 'school'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', include('course.urls', namespace='courses')),
    path('team/', include('teacher.urls', namespace='team')),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('account/', include('account.urls', namespace='account')),
    path('', views.product_all, name='school_home'),

]
