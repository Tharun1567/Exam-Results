from django.urls import path
from result import views
urlpatterns=[
    path('<str:rollno>',views.func)
]