from base import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from blog.views import page_not_found

urlpatterns = [
	path('admin/', admin.site.urls),
	path("", include("blog.urls"))
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found

admin.site.site_header = "Blog WebSite"
admin.site.index_title = "Blog Around The World"
