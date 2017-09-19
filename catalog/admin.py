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
	list_filter = ('status', 'due_back')
	fieldsets = (
		(None, {
			'fields': ('book', 'imprint', 'id')
		}),
		('Availability', {
			'fields': ('status', 'due_back', 'id')
		}),
	)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')] # tuples = inline; default = block

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
	pass
