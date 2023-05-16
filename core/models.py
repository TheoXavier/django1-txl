from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Price', decimal_places=2, max_digits=8)
    stock = models.IntegerField('Quantity in stock')

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField('Name', max_length=50)
    surname = models.CharField('Surname', max_length=50)
    email = models.EmailField('E-mail', max_length=50)

    def __str__(self):
        return f'{self.surname}, {self.name}'
