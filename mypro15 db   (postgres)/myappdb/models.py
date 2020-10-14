from django.db import models

# Creating table registerinfo

class registerinfo(models.Model):

    Name=models.CharField(max_length=15,blank=True,null=True)
    Age=models.IntegerField(blank=True,null=True)
    Address=models.CharField(max_length=50,blank=True,null=True)
    Phone=models.CharField(max_length=10,blank=True,null=True)
    Email=models.EmailField(max_length=20,blank=True,null=True)
    Zip=models.IntegerField(blank=True,null=True)