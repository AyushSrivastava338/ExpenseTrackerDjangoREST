from django.urls import path
from .views import *

urlpatterns = [
    path('get-routes', home, name="Home"),
    path('post-expense', post_expense, name="Post Expense"),
    path('get-all-expenses', get_all_expenses, name="Get all Expenses")
]
