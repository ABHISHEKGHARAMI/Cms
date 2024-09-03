from django.urls import path
from . import views

urlpatterns = [
    path('register/',
         views.StudentRegistrationView.as_views(),
         name='student_registration'),
]