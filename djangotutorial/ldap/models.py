from django.db import models


class Domainname(models.Model):
    domainname = models.CharField(max_length=50)

    def __str__(self):
        return self.domainname


class Ldapprovider(models.Model):
    basedn = models.CharField(max_length=300)
    name = models.CharField(max_length=50)
    domainname = models.ForeignKey(Domainname, on_delete=models.CASCADE)
    enabled = models.BooleanField(max_length=1)
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.name

