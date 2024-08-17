from django.contrib import admin
from .models import Articles, Comments
# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comments
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(Articles, ArticleAdmin)
admin.site.register(Comments)
