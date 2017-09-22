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
# use with Book detail page:
class BookInstanceInline(admin.TabularInline):
	model = BookInstance
	extra = 0 # extra default = 3 blank entries, is confusing

# use with Author detail page:
class BookInline(admin.TabularInline):
	model = Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')
	inlines = [BookInstanceInline]
	prepopulated_fields = {'slug': ('id', 'title')} # new: 9/22/17

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_display = ('book', 'status', 'due_back', 'id') # default: __str__(self) = id (title)
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
	inlines = [BookInline] # NB: how to omit a field from showing inline? how to make inline non-editable?

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
	pass
