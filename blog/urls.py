from django.urls import path, include
from . import views

urlpatterns = [
	path("", views.index),
	path("categories/", views.categories),  # http://127.0.0.1:8000/categories/
	path("categories/<int:cat_id>", views.categories_by_id),  # http://127.0.0.1:8000/categories/1/
]
