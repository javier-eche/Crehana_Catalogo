from django.db import models

class Course(models.Model):
    name = models.CharField(max_length = 150)
    category = models.CharField(max_length = 150)
    subcategory = models.CharField(max_length = 150)
    level = models.CharField(max_length = 50)
    username = models.CharField(max_length = 50)
    real_price = models.IntegerField(default= 0)
    discount = models.IntegerField(default= 0)
    score = models.FloatField(default= 3.5)

    class Meta:
        ordering = ['name']
