from django.urls import path
from .views import *

urlpatterns = [
    path('get-routes', home, name="Home"),
    path('expenses', post_expense, name="Post Expense"),
    path('expenses', get_all_expenses, name="Get all Expenses"),
    path('expenses/<int:id>', get_expense, name="Get Expense by ID")
]
