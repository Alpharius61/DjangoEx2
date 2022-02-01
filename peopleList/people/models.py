from django.db import models

# Create your models here.
class people(models.Model):

    name = models.CharField(max_length=50, null=False)
    Sexe = models.CharField(max_length=1, null=False)

    def __str__(self):
        return f"{self.name} - {self.Sexe}" 
    