from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	return HttpResponse("<h1> Home Page </h1>")


def categories(request):
	return HttpResponse("<h1> Categories </h1>")


def categories_by_id(request, cat_id):
	return HttpResponse(f"<h1> Categories </h1> <p> ID: {cat_id} </p>")
