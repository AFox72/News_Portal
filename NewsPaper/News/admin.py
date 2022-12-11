from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_name', 'author', 'type_post', 'rating')
    list_filter = ('rating', 'author', 'type_post', 'category')
    search_fields = ('post_name', )


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Comment)
