from django.db import models 
from django.contrib.auth.models import User

class Network(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=50, null=False)
    user = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    token = models.CharField(max_length=50, null=False)
    state = models.BooleanField(null=False)
    method = models.CharField(max_length=50, null=False)
    def __str__(self):
        txt = "{0}"
        return txt.format(self.name)

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=50, null=False)
    startDate = models.DateField(auto_now_add=True)
    endDate = models.DateField(null=True,blank=True)
    state = models.BooleanField()
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        txt = "{0}(Fecha de inicio: {1})"
        return txt.format(self.name,self.startDate)

class Schudele(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50, null=False)
    startHour = models.TimeField(null=False)
    endHour = models.TimeField(null=False)
    frecuencyHour = models.TimeField(null=False)
    Periodicity = models.TimeField(null=False)
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    Network = models.ForeignKey(Network, null=False, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        txt = "Schudele {0} (start:{1}, end:{2})"
        return txt.format(self.id,self.startHour,self.endHour)


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    urlname = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=50, null=False)
    type = models.CharField(max_length=50, null=False)
    state = models.BooleanField(null=False)
    Schudele = models.ForeignKey(Schudele,  blank=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.urlname)


class Data(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=50, null=False)
    date = models.DateField(null=False)
    Account = models.ForeignKey(Account, null=False, blank=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        txt = "Data {0}"
        return txt.format(self.id)