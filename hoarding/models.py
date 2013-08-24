from django.db import models
from django.contrib.auth.models import User
import datetime


class MediaType(models.Model):
    name        = models.CharField(max_length=250)
    flag        = models.SmallIntegerField(default=0)
    created     = models.DateTimeField(default=datetime.datetime.now())
    updated     = models.DateTimeField(default=None)
    comment     = models.TextField(null=True);

    def __unicode__(self):
        return self.name
    
    
class HoardingType(models.Model):
    name        = models.CharField(max_length=250)
    flag        = models.SmallIntegerField(default=0)
    created     = models.DateTimeField(default=datetime.datetime.now())
    updated     = models.DateTimeField(default=None)
    comment     = models.TextField(null=True);

    def __unicode__(self):
        return self.name


#This sotres the user entered hoarding information
class Hoarding(models.Model):
    town                = models.CharField(max_length=250)
    user                = models.ForeignKey(User)
    media_type          = models.ForeignKey(MediaType)
    width               = models.IntegerField(default=0)
    height              = models.IntegerField(default=0)   
    hoarding_type       = models.ForeignKey(HoardingType)  
    area_particulars    = models.TextField(null=True);
    units               = models.SmallIntegerField(default=0)  
    latitude            = models.DecimalField(null=True, max_digits=30, decimal_places=25);
    longitude           = models.DecimalField(null=True, max_digits=30, decimal_places=25);
    diaplay_cost        = models.IntegerField(default=0)
    production_cost     = models.IntegerField(default=0)
    mounting_cost       = models.IntegerField(default=0)
    enabled             = models.BooleanField(default=True)
    deleted             = models.BooleanField(default=False)
    created             = models.DateTimeField(default=datetime.datetime.now())
    updated             = models.DateTimeField(default=datetime.datetime.now())
    comment             = models.TextField(null=True);
    
    def __unicode__(self):
        return self.town

    