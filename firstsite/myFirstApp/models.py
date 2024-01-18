from django.db import models



class Customer(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField

class CustomerSettings(models.Model):
    preffered_color = models.CharField()
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE,related_name='cus')

class Publications(models.Model):
    title = models.CharField(max_length=120)

    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=120)
    publications = models.ManyToManyField(Publications)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline


#//////////////////////////////////////////////

class Book(models.Model):
    name = models.CharField(max_length=120)
    col_str = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    Book = models.ManyToManyField(Book)

    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name


class Librali(models.Model):
    title = models.TextField()
    author = models.ManyToManyField(Author)

    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title

#///////////////////////////////////////////////

