from django.urls import include, path
from .views import login, registration

app_name='account'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration')
]
