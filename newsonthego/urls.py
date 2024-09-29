from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("news.urls"), name="news-urls"),
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),
]
