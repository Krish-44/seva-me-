from django.db import models


# Create your models here.
class Userregistration(models.Model):
    id=models.AutoField(blank=False,primary_key=True)
    username = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=50,blank=False)
    password = models.CharField(max_length=20)
    repassword = models.CharField(max_length=20)

    def __str__(self):
        return self.username



