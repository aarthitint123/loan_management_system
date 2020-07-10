from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Application_form(models.Model):
    applicant_name=models.CharField(max_length=50)
    dob=models.DateField()
    pan_no=models.IntegerField()
    adhaar_no=models.CharField(max_length=10, primary_key=True)
    parent_name=models.CharField(max_length=50)
    parent_occ=models.CharField(max_length=50)
    address=models.TextField(max_length=50)

    institution_name=models.CharField(max_length=30)
    inst_code=models.IntegerField()
    year_of_passing=models.DateField()
    fee=models.IntegerField()

    loanamt = models.IntegerField()
    tenure = models.IntegerField()
    bank_name = models.CharField(max_length=50)
    acc_no = models.CharField(max_length=20)
    ifsc = models.CharField(max_length=20)








#class Registered_Users(models.Model):
#    username = models.CharField(max_length=30)
 #   email = models.CharField(max_length=50)
  #  password = models.CharField(max_length=50)
   # def __unicode__(self):
    #    return self.username

