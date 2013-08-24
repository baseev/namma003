from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save

class UserType(models.Model):
    name        = models.CharField(max_length=250)
    slug        = models.SlugField(unique=True)
    created     = models.DateTimeField(default=datetime.datetime.now())
    enabled     = models.BooleanField(default=True)
    comment     = models.TextField(null=True);
    
    def __unicode__(self):
        return self.name

    

class UserInfo(models.Model):
    user        = models.OneToOneField(User)
    user_type   = models.ForeignKey(UserType)
    posts       = models.IntegerField(default=0)
    created     = models.DateTimeField(default=datetime.datetime.now())
    updated     = models.DateTimeField(default=datetime.datetime.now())
    comment     = models.TextField(null=True);




    