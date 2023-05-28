from django.urls import path
from profiless import views


urlpatterns = [
    path('profiless/', views.ProfileList.as_view()),
    path('profiless/<int:pk>/', views.ProfileDetail.as_view()),
  
]

