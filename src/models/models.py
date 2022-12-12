from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=255)
    coords = models.CharField(max_length=255)

class Book(models.Model):
    isbn = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    resume = models.TextField()
    addedOn = models.DateField()
    bookstore = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.isbn
