from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    description=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.name