from django.shortcuts import render
from django.views.generic import ListView
from post.models import Publicaciones
# Create your views here.

class HomePageView(ListView):

    model=Publicaciones



