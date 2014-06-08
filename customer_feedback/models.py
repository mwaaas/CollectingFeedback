from django.contrib import admin
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db.models import permalink
from customer_feedback import CustomModelField


class Employee(models.Model):
    fname = models.CharField(verbose_name="First name",max_length=255)
    lname = models.CharField(verbose_name="Last name", max_length=255)
    password = models.CharField(verbose_name="Password", max_length=255)

    def __unicode__(self):
        return self.fname

    class Meta:
        unique_together = ("fname", "lname")

class Company(models.Model):
    companyName = models.CharField(verbose_name="Company Name", max_length=255, unique=True)
    tagLine = models.CharField(verbose_name="Tag line", max_length=255)
    logo = CustomModelField.ThumbnailImageField(upload_to='photos', verbose_name="Logo")
    description = models.CharField(verbose_name="Description", max_length=255)

    def __unicode__(self):
        return self.companyName


    def delete(self, *args, **kwargs):
        self.logo.delete(False)
        super(Company, self).delete(*args, **kwargs)



class Assigned(models.Model):
    companyName = models.ForeignKey(Company)
    employee = models.ForeignKey(Employee)

    class Meta:
        unique_together = ("companyName", "employee")


class Feedback(models.Model):
    company = models.ForeignKey(Company)
    fname = models.CharField(verbose_name="First name", max_length=255)
    lname = models.CharField(verbose_name="Last name", max_length=255)
    phoneNumber = models.CharField(verbose_name="Phone number", max_length=255)
    comment = models.TextField(verbose_name="Comment")

class Admin(models.Model):
    admin_name = models.CharField(verbose_name="admin name", max_length=255)
    password = models.CharField(verbose_name="Password", max_length=255)




admin.site.register(Company)
admin.site.register(Feedback)
admin.site.register(Employee)
admin.site.register(Assigned)

