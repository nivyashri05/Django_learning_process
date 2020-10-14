from django.db import models

# Create your models here.
class Studenttb(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=30)
    sage=models.IntegerField()
    saddr=models.CharField(max_length=30)

    def __str__(self):
        return 'Student Object with s_no'+str(self.sid)
