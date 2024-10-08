from django.contrib import admin
from .models import Uploads, Commenting
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Uploads)
class UploadsAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'author', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Commenting)