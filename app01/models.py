from django.db import models

# Create your models here.   类---对应 表
class User(models.Model):
    username = models.CharField(max_length=32)   #对应数据库的varchar
    password = models.CharField(max_length=32)
