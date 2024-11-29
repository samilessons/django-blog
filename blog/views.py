from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = ["About", "Add Article", "Contacts", "Log In"]


class MyClass:
	def __init__(self, a, b):
		self.a = a
		self.b = b

def index(request):
	# t = render_to_string("blog/index.html")
	# return HttpResponse(t)
	data = {
		"title": "Home Page",
		"description": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium aliquid corporis molestiae quas quos ullam.",
		"menu": menu,
		"float": 22.33,
		"int": 75,
		"lst": [7, 5, "Hello", "bye", False],
		"set": {1, 2, 1, 1, 2, 3},
		"ddd": {"name": "John Smith", "password": "123456789"},
		"cls": MyClass(45, 89),
		"url": slugify("The Home Page")
	}
	return render(request, "blog/index.html", data)


def about(request):
	return render(request, "blog/about.html", {"title": "About Page"})


def categories(request):
	return HttpResponse("<h1> Categories </h1>")


def categories_by_id(request, cat_id):
	return HttpResponse(f"<h1> Categories </h1> <p> ID: {cat_id} </p>")


def categories_by_slug(request, cat_slug):
	return HttpResponse(f"<h1> Categories </h1> <p> SLUG: {cat_slug} </p>")


def archive(request, year):
	if year > 2024:
		# return redirect("/", permanent=True)
		# return redirect(index, permanent=True)
		# return redirect("index", permanent=True)
		# return redirect("cat_slug", "armenia")
		uri = reverse("cat_slug", args=("armenia",))
		return redirect(uri, permanent=True)
	# return HttpResponseForbidden()
	
	return HttpResponse(f"<h1> Archive </h1> <p> Archive: {year} </p>")


def page_not_found(request, exception):
	return HttpResponseNotFound(f"<h1> Page Not Found 404 </h1>")
