from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Item(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete= models.SET_NULL)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.title

