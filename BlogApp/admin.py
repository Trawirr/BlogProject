from django.contrib import admin
from .models import *

class VariableAdmin(admin.ModelAdmin):
    list_display = ("nazwa", "wartość")

    def nazwa(self, obj):
        return obj.name
    
    def wartość(self, obj):
        return obj.value

class TagAdmin(admin.ModelAdmin):
    list_display = ("nazwa",)

    def nazwa(self, obj):
        return obj.name

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("użytkownik", "nazwa", "data_dodania", "typ")

    def użytkownik(self, obj):
        return obj.user
    
    def nazwa(self, obj):
        return obj.nickname
    
    def data_dodania(self, obj):
        return obj.date
    
    @admin.display(boolean=True)
    def typ(self, obj):
        return obj.role == "admin"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("tytuł", "autor", "data_dodania", "tekst", "tagi")

    def tytuł(self, obj):
        return obj.title

    def autor(self, obj):
        return obj.author
    
    def data_dodania(self, obj):
        return obj.date

    def tekst(self, obj):
        text = obj.text if len(obj.text) < 50 else obj.text[:50] + "..."
        return text

    def tagi(self, obj):
        return ", ".join(t.name for t in obj.tags.all())

class CommentAdmin(admin.ModelAdmin):
    list_display = ("autor", "data_dodania", "tekst", "post")

    def autor(self, obj):
        return obj.author
    
    def data_dodania(self, obj):
        return obj.date

    def tekst(self, obj):
        text = obj.text if len(obj.text) < 50 else obj.text[:50] + "..."
        return text

    def post(self, obj):
        return obj.article.thumbnail_title

admin.site.register(Variable, VariableAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)