from django.urls import path
from . import adminviews

urlpatterns = [
    path('manageuser/', adminviews.manageuser_page, name = 'manageuser'),
    path('trainingframework/', adminviews.trainingframework_page, name = 'trainingframework'),
    path('subject/', adminviews.subject_page, name = 'subject'),
    path('learningoutcome/', adminviews.learningoutcome_page, name = 'learningoutcome'),
    path('suggestioncourseadmin/', adminviews.suggestioncourse_page, name = 'suggestioncourseadmin'),
    path('scoreforecastadmin/', adminviews.scoreforecast_page, name = 'scoreforecastadmin'),
    path('statisticaladmin/', adminviews.statistical_page, name = 'statisticaladmin'),
]