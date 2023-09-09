from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('get-routes', home, name="Home"),
    path('login', TokenObtainPairView.as_view(), name="Login"),
    path('login/refresh', TokenRefreshView.as_view(), name="Test Token"),
    path('register', register, name="Register"),
    path('expenses', expenses, name="Post Expense"),
    path('expenses', expenses, name="Get all Expenses"),
    path('expenses/<int:id>', delete_expense, name="Delete expense"),
    path('week-expenses', sum_of_last_7_days, name="Sum of last 7 days"),
    path('home', home)
]




