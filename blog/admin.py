from django.contrib import admin, messages
from .models import Article, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ["id", "title", "slug", "is_published", "category", "brief_info"]
	list_display_links = ["id", "title"]
	list_editable = ["is_published"]
	list_per_page = 25
	ordering = ["-pk"]
	actions = ["set_published", "set_draft"]
	search_fields = ["title", "content", "category__name"]
	search_help_text = "You can search only with title or content"
	list_filter = ["category__name", "is_published"]
	
	# class chgitem (admin.SimpleListFilter) + lookups queryset
	
	@admin.display(description="Short Info", ordering="content")
	def brief_info(self, article: Article):
		return f"Description {len(article.content)} symbols."
	
	@admin.action(description="Դարձնել Փըբլիշդ")
	def set_published(self, request, queryset):
		count = queryset.update(is_published=Article.Status.PUBLISHED)
		self.message_user(request, f"Փըբլիշ է եղել {count} նյութեր", messages.INFO)
	
	@admin.action(description="Դարձնել Դրաֆթ")
	def set_draft(self, request, queryset):
		count = queryset.update(is_published=Article.Status.DRAFT)
		self.message_user(request, f"Դրաֆթ է եղել {count} նյութեր", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ("id", "name", "slug")
	list_display_links = ("id", "name")
	ordering = ["-pk"]
	list_filter = ["name"]
