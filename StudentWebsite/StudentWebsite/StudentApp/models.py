#-*- encoding=UTF-8 -*-
from django.db import models
from django.core.exceptions import ValidationError
import re

class Student(models.Model):
    firstname = models.CharField(max_length=30, null=False, blank=False)
    lastname = models.CharField(max_length=30, null=False, blank=False)

    def clean(self):
        if re.match(r'^\s+$', self.firstname):
            raise ValidationError('Firstname should contain some characters, only spaces not allowed')
        if re.match(r'^\s+$', self.lastname):
            raise ValidationError('Lastname should contain some characters, only spaces not allowed')	
	
    def __unicode__(self):
        return u'%s %s' % (self.firstname, self.lastname)

    class Meta:
        unique_together = (("firstname", "lastname"),)
        ordering = ['firstname']

class Subject(models.Model):
    name = models.CharField(max_length=10, unique=True, null=False, blank=False)
    
    def clean(self):
        if re.match(r'^\s+$', self.name):
            raise ValidationError('Subject should contain some characters, only spaces not allowed')
    
    def __unicode__(self):
        return u'%s' % (self.name)

class StudentMarks(models.Model):
    student = models.ForeignKey(Student)
    subject = models.ForeignKey(Subject)
    marks   = models.IntegerField(max_length=3, null=False, blank=False)

    class Meta:
        unique_together = (("student", "subject"),)