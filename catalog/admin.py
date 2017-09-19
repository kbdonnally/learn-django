# admin site config

from django.contrib import admin
from .models import Book, BookInstance, Author, Genre, Language

''' Original:
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
'''

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	pass

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
	pass
