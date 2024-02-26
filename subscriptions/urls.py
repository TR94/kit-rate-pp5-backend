from django.urls import path
from subscriptions import views

urlpatterns = [
    path('subscriptions/', views.SubscribeList.as_view()), 
    path('subscriptions/<int:pk>/', views.SubscribeDetail.as_view()),
    path('subscriptions/my-subscriptions/', views.MySubscriptions.as_view()),

]