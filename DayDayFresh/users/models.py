from django.db import models

# Create your models here.

class userInfo(models.Model):
    user_name = models.CharField(max_length=30)
    upassword = models.CharField(max_length=30)
    umail = models.CharField(max_length=30)
    uconsignee = models.CharField(max_length=30,default='')
    uaddress = models.CharField(max_length=100,default='')
    upostcode = models.IntegerField(default='')
    uphone = models.CharField(max_length=30,default='')
    isDelete = models.BooleanField(default=False)
