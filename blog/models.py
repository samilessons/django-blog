from django.db import models
from django.urls import reverse


class ArticleManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(is_published=Article.Status.PUBLISHED)


class Article(models.Model):
	class Status(models.IntegerChoices):
		DRAFT = 0, "Draft"
		PUBLISHED = 1, "Published"
	
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True)
	content = models.TextField(blank=True)
	time_create = models.DateTimeField(auto_now_add=True)
	time_update = models.DateTimeField(auto_now=True)
	is_published = models.BooleanField(choices=Status.choices, default=Status.PUBLISHED)
	category = models.ForeignKey("Category", on_delete=models.CASCADE)
	
	objects = models.Manager()
	published = ArticleManager()
	
	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse("article", kwargs={"article_slug": self.slug})
	
	class Meta:
		ordering = ["time_create"]
		indexes = [
			models.Index(fields=["time_create"])
		]


class Category(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, unique=True, db_index=True)
	
	def __str__(self):
		return self.name
