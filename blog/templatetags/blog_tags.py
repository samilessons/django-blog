from django import template
import blog.views as views

register = template.Library()


# @register.simple_tag()
# def get_categories():
# 	return views.categories_from_db


@register.inclusion_tag("blog/includes/categories.html")
def show_categories(cat_selected=0):
	cats = views.categories_from_db
	return {"cats": cats, "cat_selected": cat_selected}
