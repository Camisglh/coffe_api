from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Card(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(default=0, max_length=3)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
