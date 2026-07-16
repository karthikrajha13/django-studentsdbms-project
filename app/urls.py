from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),

    path("register/", views.register, name="register"),
    path("search/", views.search, name="search"),
    path("students/", views.students, name="students"),

    path("edit/<int:id>/", views.edit, name="edit"),
    path("delete/<int:id>/", views.delete, name="delete"),

    path("python/", views.python_students, name="python"),
    path("orm/", views.orm_demo, name="orm"),

    # IMPORTANT
    path("djangoform/", views.django_form, name="djangoform"),

    path("signup/", views.signup, name="signup"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
]