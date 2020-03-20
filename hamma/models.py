from django.db import models


class Usuario(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    email = models.EmailField(max_length=25)

    def Registro(self):
        self.save()
    
    # def __str__(self):
    #     return self.username