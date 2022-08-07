from django.urls import path

from . import views
app_name='api'
urlpatterns = [
    path('UserData/<str:username>',views.UserDataViewSet.as_view()),
    path('UserData/',views.UserDataViewSet.as_view()),
    path('ExpenseData/<int:userid>',views.ExpenseDataViewSet.as_view()),
    path('ExpenseData/<int:userid>/<int:expense_id>',views.ExpenseDataViewSet.as_view()),
    path('category',views.ExpenseCategoryViewSet.as_view()),
    path('category/<str:categoryname>',views.ExpenseCategoryViewSet.as_view())
    ]