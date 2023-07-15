from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import generic
import json
from .models import Projects, User


# Create your views here.
class Index(generic.ListView):
    model = Projects
    context_object_name = 'projects'
    template_name = 'eportfolio/index.html'

    def get_queryset(self):
        return Projects.objects.order_by("-id")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "eportfolio/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "eportfolio/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "eportfolio/register.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("about_me"))
        else:
            return render(request, "eportfolio/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "eportfolio/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def about_me(request):
    return render(request, "eportfolio/about_me.html")


def my_projects(request):
    projects = Projects.objects.all()

    return render(request, "eportfolio/my_projects.html", {
        "projects": projects
    })


def create(request):
    if request.method == 'POST' and request.user.is_authenticated:
        post_data = json.loads(request.body)
        title = post_data.get('title')
        author = post_data.get('author')
        description = post_data.get('description')
        requirements = post_data.get('requirements')
        technology = post_data.get('technology')
        video = post_data.get('video')

        project = Projects(
            title=title,
            author=author,
            description=description,
            requirements=requirements,
            technology=technology,
            video=video
        )
        project.save()

    return render(request, "eportfolio/my_projects.html")
