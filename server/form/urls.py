from django.urls import path, include
from . import views

urlpatterns = [
    path('data/', views.DataEntry.as_view()),
    path('email/', views.Email.as_view()),
]
