from django.db import models
from django.contrib.auth.models import User


class Types(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class Kebab(models.Model):
    Name = models.CharField(max_length=100)
    types = models.ForeignKey(Types, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    Price = models.FloatField(blank=True, null=True)
    mas = models.FloatField(blank=True, null=True)
    col_buttons = models.IntegerField(blank=True, null=True)
    col = models.IntegerField(blank=True, null=True)
    kebab_url = models.ImageField(upload_to='kebab/')

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Шаурма"

        verbose_name_plural = "Шаурма"

class Drink(models.Model):
    Name = models.CharField(max_length=100)
    types = models.ForeignKey(Types, on_delete=models.CASCADE, default=1)
    price = models.FloatField(blank=True, null=True)
    col = models.IntegerField(blank=True, null=True)
    mass = models.FloatField(blank=True, null=True)
    drink_url = models.ImageField(upload_to='kebab/', default='')

    def __str__(self):
        return f" {self.Name}:"

    class Meta:
        verbose_name = "Напитки и тд"
        verbose_name_plural = "Напитки и тд"



class Saved(models.Model):
    Name = models.CharField(max_length=100)
    types = models.ForeignKey(Types, on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField(max_length=200)
    dop_text = models.CharField(max_length=200, blank=True, null=True)
    Price = models.FloatField(blank=True, null=True)
    mas = models.FloatField(blank=True, null=True)
    col_buttons = models.IntegerField(blank=True, null=True)
    col = models.IntegerField(blank=True, null=True)
    kebab_url = models.ImageField(upload_to='kebab/', blank=True, null=True)
    def __str__(self):
        return f" {self.Name}:"

    class Meta:
        verbose_name = "Индивидуальные"
        verbose_name_plural = "Индивидуальные"

class Orders(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=50)
    email = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return f" {self.Name}: {self.Phone}: {self.email}: "

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class Card(models.Model):
    Order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    Kebab = models.ForeignKey(Saved, on_delete=models.CASCADE)
    TotalPrice = models.FloatField(blank=True, null=True)
    dop_text = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return f" {self.Kebab}: {self.Order.Name}: {self.TotalPrice}:"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

# Create your models here.
