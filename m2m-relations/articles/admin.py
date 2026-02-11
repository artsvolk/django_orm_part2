from django.contrib import admin
from .models import Article, Tag, Scope


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    list_display = ('title', 'published_at')
    ordering = ['-published_at']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ('article', 'tag', 'is_main')
    list_filter = ('is_main', 'tag')