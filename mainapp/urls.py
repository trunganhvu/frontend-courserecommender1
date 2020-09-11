from django.urls import path
from . import views
from . import adminviews

urlpatterns = [
    path('login/', adminviews.login_page, name = 'login'),

    path('profile/', views.profile_page, name = 'profile'),
    path('transcript/', views.transcript_page, name = 'transcript'),
    path('changepassword/', views.changepassword_page, name = 'changepassword'),
    path('suggestioncourse/', views.suggestioncourse_page, name = 'suggestioncourse'),
    path('scoreforecast/', views.scoreforecast_page, name = 'scoreforecast'),
    path('statistical/', views.statistical_page, name = 'statistical'),
    path('statisticals/', views.statistical_page, name = 'statistical1'),
]