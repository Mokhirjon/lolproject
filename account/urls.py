from django.urls import path
from .views import SignupUserview
urlpatterns = [
    path('sign_up/',SignupUserview.as_view())
]