from django.db import models


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    published_at = models.DateField(name="Published At", auto_now=True)
    summary = models.TextField(name="Summary", max_length=500, blank=True)
    country = models.CharField(name='Country', max_length=30, null=True)
    link = models.URLField(name="Book Link", null=True)


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    died_at = models.DateField(name="Died At", auto_now=True, auto_created=True)
    born_at = models.DateField(name="Born At", auto_now=True, auto_created=True)
    contact = models.TextField(name="Contact", max_length=500, blank=True)
    bio = models.TextField(name="Biography", max_length=500, blank=True)
    books = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
