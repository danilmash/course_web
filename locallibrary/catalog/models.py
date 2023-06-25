from django.db import models
from django.urls import reverse
from datetime import date
import uuid
# Create your models here.
class Book(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1500, help_text="Enter a brief description of the book")
    genre = models.ManyToManyField("Genre", help_text="Select a genre for this book")
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def display_genre(self):
            
            return ', '.join([ genre.title for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'

    def __str__(self):

        return self.title
    
    def get_absolute_url(self):

        return reverse('book-detail', args=[str(self.id)])
    



class Language(models.Model):

    title = models.CharField(max_length=100, help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):

        return self.title
    




class Genre(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the genre")

    def __str__(self):

        return self.title
    

from django.contrib.auth.models import User
from datetime import date

class BookInstance(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    imprint = models.CharField(max_length=100)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On rent'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]


    def __str__(self):
        
        return self.book.title
    
    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False




class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    biography = models.TextField(max_length=1800, help_text="Enter an author's biography")

    def __str__(self):

        return '{0}, {1}'.format(self.last_name, self.first_name)

    def get_absolute_url(self):

        return reverse('author-detail', args=[str(self.id)])



