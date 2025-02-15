from django.shortcuts import render, redirect, get_object_or_404
from app.models import User

""""""
def home(request):
    return render(request, 'app/test/index.html')

def create(request):
    return render(request, 'app/test/create.html')

def creation_successful(request):
    return render(request, 'app/test/creation_successful.html')

def user_edit(request):
    return render(request, 'app/user/edit.html')