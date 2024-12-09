from django.http import  HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from .models import Article

categories_from_db = [
	{"id": 1, "name": "Traveling"},
	{"id": 2, "name": "Sport"},
	{"id": 3, "name": "IT & Development"},
	{"id": 4, "name": "Cars"},
	{"id": 5, "name": "Fashion"},
]


def index(request):
	# articles = Article.objects.filter(is_published=1)
	articles = Article.published.all()
	return render(request, "blog/home.html", {"articles": articles})


def about(request):
	return render(request, "blog/about.html", {"title": "About Page"})


def show_article(request, article_slug):
	article = get_object_or_404(Article, slug=article_slug)
	
	data = {
		"title": article.title,
		"content": article.content,
		"time_create": article.time_create,
		"time_update": article.time_update,
		"is_published": article.is_published
	}
	return render(request, "blog/show-article.html", data)


def show_category(request, cat_id):
	return render(
		request,
		"blog/category.html",
		{
			"title": categories_from_db[cat_id - 1].get("name"),
			"cat_selected": cat_id
		},
	)


def add_post(request):
	return render(request, "blog/add-post.html", {"title": "Add Post"})


def contacts(request):
	return render(request, "blog/contacts.html", {"title": "Contacts"})


def login(request):
	return render(request, "blog/login.html", {"title": "Login"})


def page_not_found(request, exception):
	return HttpResponseNotFound(f"<h1> Page Not Found 404 </h1>")
