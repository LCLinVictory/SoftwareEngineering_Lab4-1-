from django.db import models

class Author(models.Model):
    AuthorID = models.CharField(max_length = 100)
    Name = models.CharField(max_length=30)
    Age = models.CharField(max_length=30)
    Country = models.CharField(max_length=100)
    
    def __unicode__(self):  # __!!!
        return self.Name
    class Meta:
        ordering = ['AuthorID']

class Book(models.Model):
    ISBN = models.CharField(max_length = 30)
    Title = models.CharField(max_length = 100)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length = 100)
    PublishDate = models.DateField(max_length = 30)
    Price = models.CharField(max_length = 100)
    
    def __unicode__(self):
        return self.Title
# Create your models here.
