from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_type=models.CharField(max_length=10)
    email = models.EmailField()
    line = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode=models.IntegerField()
    profile=models.ImageField(upload_to="media",default="profile.png",null=True,blank=True)

    def __str__(self):
        return self.username