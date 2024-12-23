from django.contrib import admin, messages
from .models import Article, Category, Author


class AuthorFilter(admin.SimpleListFilter):
    title = "Filter Authors"
    parameter_name = "check_author"

    def lookups(self, request, model_admin):
        return [
            ("with_author", "With Author"),
            ("without_author", "Without Author"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "with_author":
            return queryset.filter(author__isnull=False)
        elif self.value() == "without_author":
            return queryset.filter(author__isnull=True)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "articles_qty"]
    list_display_links = ["name"]
    list_per_page = 25
    ordering = ["-pk"]
    search_fields = ["name"]
    search_help_text = "You can search only with author name"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # exclude = ["adv"]
    # fields = ["slug", "title", "content"]
    # readonly_fields = ["slug"]
    prepopulated_fields = {"slug": ("title", )}
    list_display = ["id", "title", "slug",
                    "is_published", "category", "brief_info", "author"]
    list_display_links = ["id", "title"]
    list_editable = ["is_published"]
    list_per_page = 25
    ordering = ["-pk"]
    actions = ["set_published", "set_draft"]
    search_fields = ["title", "content", "category__name"]
    search_help_text = "You can search only with title or content"
    list_filter = [AuthorFilter, "category__name", "is_published"]
    filter_horizontal = ["tags"]

    @admin.display(description="Short Info", ordering="content")
    def brief_info(self, article: Article):
        return f"Description {len(article.content)} symbols."

    @admin.action(description="Դարձնել Փըբլիշդ")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Article.Status.PUBLISHED)
        self.message_user(request, f"Փըբլիշ է եղել {
                          count} նյութեր", messages.INFO)

    @admin.action(description="Դարձնել Դրաֆթ")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Article.Status.DRAFT)
        self.message_user(request, f"Դրաֆթ է եղել {
                          count} նյութեր", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("id", "name")
    ordering = ["-pk"]
    list_filter = ["name"]
