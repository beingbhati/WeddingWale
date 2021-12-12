from django.db import models

# Create your models here.
class post(models.Model):
    desc = models.CharField(max_length=122)
    price = models.IntegerField()
    img = models.ImageField(upload_to="pics")



class Contact(models.Model):  
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    feedback = models.TextField()  

    def __str__(self):
        return self.name



