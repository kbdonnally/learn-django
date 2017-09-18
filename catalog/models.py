# models for locallibrary

from django.db import models
from django.urls import reverse

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
	isbn = models.CharField('ISBN', max_length=13, help_text='Enter the 13-digit <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
	# NB: 'ISBN' gets assigned to verbose_name attribute of field; is optional 1st arg
	genre = models.ManyToManyField(Genre, help_text="Please choose one or more genres for this title.")

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('book-details', args=[str(self.id)])
		# we need to write URL handler called 'book-details'
		# also create template for handler to use
		# (basically an artifact entry page)
