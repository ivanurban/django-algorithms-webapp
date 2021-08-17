from django.contrib import admin
from .models import Post
from django.db import models
from tinymce.widgets import TinyMCE



# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status', 'difficulty')
    list_filter = ('status', 'created', 'publish', 'author', 'difficulty')
    search_fields = ('title', 'body','difficulty')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

    formfield_overrides = {

        models.TextField: {'widget': TinyMCE()}

   }



