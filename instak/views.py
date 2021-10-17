from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# from .forms import PostImage,EditProfile,UpdateProfile,CommentForm,Likes,FormFollow
from .models import Image,Profile,Comments,Followers
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    title='Home'
    return render(request,"index.html",{"title":title})