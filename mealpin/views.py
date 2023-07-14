from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages


def index(request):
    return render(request, "index.html")
