#-*-coding:utf8-*-
from django.db import models
#from django.contrib.auth.models import User
#from django.contrib.auth.admin import UserAdmin


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    info = models.TextField()

    def __unicode__(self):
        return u'%s %s' % (self.name, self.info)


class Stages(models.Model):
    id = models.AutoField(primary_key=True)
    index = models.IntegerField()
    info = models.TextField()
    content = models.TextField()
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return u'%s %s' % (self.info, self.content)
