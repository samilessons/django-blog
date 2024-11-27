from django.urls import path, include, re_path, register_converter
from . import views

from . import converters

register_converter(converters.FourDigitYearConverter, "year_from_4_numbers")

urlpatterns = [
	path("", views.index, name="index"),
	path("categories/", views.categories, name="categories"),  # http://127.0.0.1:8000/categories/
	path("categories/<int:cat_id>", views.categories_by_id),  # http://127.0.0.1:8000/categories/1/
	path("categories/<slug:cat_slug>", views.categories_by_slug, name="cat_slug"),  # http://127.0.0.1:8000/categories/dd3/
	path("archive/<year_from_4_numbers:year>/", views.archive),  # http://127.0.0.1:8000/archive/2023/
]
