from django.urls import path
from user.views import UserView, UserDetailView


urlpatterns = [
    path('', UserView.as_view()),
    path('<int:pk>/', UserDetailView.as_view())
]
