from django.db import models
from django.urls import reverse


class Article(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True)
	content = models.TextField(blank=True)
	time_create = models.DateTimeField(auto_now_add=True)
	time_update = models.DateTimeField(auto_now=True)
	is_published = models.BooleanField(default=True)
	
	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse("article", kwargs={"article_slug": self.slug})
	
	class Meta:
		ordering = ["time_create"]
		indexes = [
			models.Index(fields=["time_create"])
		]
