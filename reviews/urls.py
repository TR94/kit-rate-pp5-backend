from django.urls import path 
from reviews import views

urlpatterns = [
    path('reviews/', views.ReviewList.as_view()),
    path('reviews/product/<int:product>/', views.ReviewList.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view()),

]