from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('metrics/', views.MetricsPageView.as_view()),
    path('results/', views.ResultsPageView.as_view()),
]
