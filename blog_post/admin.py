from django.contrib import admin

from .models import Post, Rubric
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'content', 'published', 'rubric')
    list_display_links = ('nickname', 'content')
    search_fields = ('nickname', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(Rubric)