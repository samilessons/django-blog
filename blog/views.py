from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from .models import Article, Category, ArticleTags


def index(request):
	# articles = Article.objects.filter(is_published=1)
	articles = Article.published.all()
	return render(request, "blog/home.html", {"articles": articles})


def about(request):
	return render(request, "blog/about.html", {"title": "About Page"})


def show_category(request, cat_slug):
	category = get_object_or_404(Category, slug=cat_slug)
	articles = Article.published.filter(category_id=category.pk)
	data = {
		"name": category.name,
		"slug": category.slug,
		"id": category.id,
		"articles": articles,
		"cat_selected": category.id
	}
	return render(request, "blog/category.html", data)


def show_article(request, article_slug):
	article = get_object_or_404(Article, slug=article_slug)
	
	data = {
		"title": article.title,
		"content": article.content,
		"time_create": article.time_create,
		"time_update": article.time_update,
		"is_published": article.is_published,
		"tags": article.tags.all()
	}
	return render(request, "blog/show-article.html", data)


def show_tags(request, tag_slug):
	tag = get_object_or_404(ArticleTags, slug=tag_slug)
	articles = tag.tags.filter(is_published=Article.Status.PUBLISHED)
	
	data = {
		"title": f"Tag: {tag.tag}",
		"articles": articles,
	}
	
	return render(request, "blog/show-tags.html", data)


def add_post(request):
	return render(request, "blog/add-post.html", {"title": "Add Post"})


def contacts(request):
	return render(request, "blog/contacts.html", {"title": "Contacts"})


def login(request):
	return render(request, "blog/login.html", {"title": "Login"})


def page_not_found(request, exception):
	return HttpResponseNotFound(f"<h1> Page Not Found 404 </h1>")
