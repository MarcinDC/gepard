from django.db import models

# Create your models here.


class Product(models.Model):
    code = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=100, null=False)
    desc = models.TextField()

    def __str__(self):
        return self.name


