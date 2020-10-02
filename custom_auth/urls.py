from django.urls import path
from .views import loginAuth, registration

urlpatterns = [
        path('login/', loginAuth, name='login'),
        path('register/',registration, name='register')
]