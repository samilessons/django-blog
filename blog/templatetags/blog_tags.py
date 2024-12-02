from django import template
import blog.views as views

register = template.Library()


@register.simple_tag()
def get_categories():
	return views.categories_from_db


@register.inclusion_tag("blog/category.html")
def show_categories():
	cats = views.categories_from_db
	return {"cats": cats}
