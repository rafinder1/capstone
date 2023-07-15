from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path("my_projects", views.my_projects, name="my_projects"),
    path("about_me", views.about_me, name="about_me"),
    path('create', views.create, name='create'),

    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path('login', views.login_view, name='login'),


]
