# models for locallibrary

from django.db import models
from django.urls import reverse
import uuid

# Genre: (list skeleton/maker)
class Genre(models.Model):
	name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Historical Fiction)")

	def __str__(self):
		return self.name

# Book: (title, not physical object)
class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book.")
	isbn = models.CharField('ISBN', max_length=13, 
		help_text='Enter the 13-digit <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
	genre = models.ManyToManyField(Genre, help_text="Please choose one or more genres for this title.")
	# MDN challenge:
	language = models.ManyToManyField('Language', help_text="Languages available for this title")

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('book-details', args=[str(self.id)])
		# we need to write URL handler called 'book-details'
		# also create template for handler to use
		# (basically an artifact entry page)

# BookInstance: (physical object)
class BookInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this book copy.")
	book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=200) # ???
	due_back = models.DateField(null=True, blank=True) # null/blank when book not checked out
	# MDN challenge:
	language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

	LOAN_STATUS = (
		('m', 'Maintenance'),
		('o', 'On loan'),
		('r', 'Reserved'),
		('a', 'Available'),
	) # ('db val', 'Display Text')

	status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

	class Meta:
		ordering = ["due_back"]

	def __str__(self):
		return '{0} ({1})'.format(self.id, self.book.title)

# Author:
class Author(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateField(null=True, blank=True)
	date_of_death = models.DateField('Died', null=True, blank=True) # 1st arg = verbose_name

	def get_absolute_url(self):
		return reverse('author-details', args=[str(self.id)]) # need to create URL handler 'author-details'

	def __str__(self):
		return '{0}, {1}'.format(self.last_name, self.first_name)

# Language: (list of all languages in library, subject to change so is model)
class Language(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name