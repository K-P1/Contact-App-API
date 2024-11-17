from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    nickname = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, unique=True)
    phone_2 = models.CharField(max_length=50, unique=True, null=True, blank=True)
    phone_3 = models.CharField(max_length=50, unique=True, null=True, blank=True)
    email = models.EmailField(max_length=50, unique=True, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    relation = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"