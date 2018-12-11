from django.db import models


class Users(models.Model):
    userTel = models.CharField(primary_key=True, max_length=12)
    userName = models.CharField(max_length=16)
    userMail = models.CharField(max_length=20)
    userPwd = models.CharField(max_length=20)

    def __str__(self):
        return self.userName
