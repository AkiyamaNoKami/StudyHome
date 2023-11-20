from django.urls import include, path
from . import views

app_name='school'

urlpatterns = [
    path('', views.product_all, name='school_home'),
]
