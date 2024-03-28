from django.urls import path
from .views import login_view, registration

app_name = 'account'

urlpatterns = [
    path('', login_view, name='login'),
    path('registration/', registration, name='registration')
]
