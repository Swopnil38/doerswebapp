from statistics import mode
from django.db import models

# Create your models here.
class doersdetails(models.Model):
    doers_name = models.CharField(max_length=50)
    doers_profession = models.CharField(max_length=50)
    doers_timeinfield = models.CharField(max_length=50)
    doers_impactdesc = models.CharField(max_length=1000)
    doers_willingness = models.CharField(max_length=200)
    doers_contact = models.CharField(max_length=50)
    class Meta:
        db_table = "doersdetails"
        

class willingdoersdetails(models.Model):
    willingdoers_name = models.CharField(max_length=50)
    willingdoers_experties = models.CharField(max_length=100)
    willingdoers_skillset = models.CharField(max_length=100)
    willingdoers_want = models.CharField(max_length=500)
    willingdoers_education = models.CharField(max_length=100)
    willingdoers_contact = models.CharField(max_length=50)
    class Meta:
        db_table = "willingdoersdetails"
        
        
class emaillist(models.Model):
    email = models.EmailField(max_length=255)
    class Meta:
        db_table = "emaillist" 
