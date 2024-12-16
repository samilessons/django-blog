from django import template
from blog.models import Category, ArticleTags

register = template.Library()


@register.inclusion_tag("blog/includes/categories.html")
def show_categories(cat_selected=0):
	cats = Category.objects.all()
	return {"cats": cats, "cat_selected": cat_selected}


@register.inclusion_tag("blog/includes/tags.html")
def show_tags():
	return {"tags": ArticleTags.objects.all()}
