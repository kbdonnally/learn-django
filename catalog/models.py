# models for locallibrary

from django.db import models

# Genre: (list skeleton/maker)
class Genre(models.Model):
	name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Historical Fiction)")

	def __str__(self):
		return self.name
