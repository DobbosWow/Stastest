from django.db import models

class RegNewUser(models.Model):
    userName = models.CharField(max_length=40)
    userPass = models.CharField(max_length=20)


    def __str__(self):
        mystr = "Name: "+self.userName+" Pass: "+self.userPass
        return mystr