from django.urls import path
from .import views
from .views import *
urlpatterns=[
    path('aajapi/',views.TodayAPI.as_view()),
    path('aajapi/<int:pk>/',views.TodayAPI.as_view()),

]