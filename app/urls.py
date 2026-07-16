from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about),
    path('contact/', views.contact),
    path("register/", views.register),
    path("search/", views.search),
    path("students/", views.students),
    path("edit/<int:id>/", views.edit),
    path("delete/<int:id>/", views.delete),
    path("python/", views.python_students),
    path("orm/", views.orm_demo),
    path("djangoform/", views.django_form, name="django_form"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
]