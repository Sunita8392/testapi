from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Stu(models.Model):
    roll_no=models.IntegerField()
    name=models.CharField(max_length=150)
    address=models.CharField(max_length=500)

    def __str__(self):
        
        return "{} {} {}".format(self.roll_no, self.name,self.address)
