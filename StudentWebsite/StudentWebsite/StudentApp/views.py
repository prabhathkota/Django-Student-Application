#-*- encoding=UTF-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404
#from django.http import *
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from StudentWebsite.StudentApp.models import Subject, Student, StudentMarks
from django.db.models import Avg, Count

def subjectView(request):
    subjectList = Subject.objects.values('pk', 'name')
    side_bar = {'Home':'home', 'Admin' : 'admin:index'}
    return render(request, 'StudentsMain.html', {'subjects' : subjectList, 'side_bar' : side_bar})

def getMarksDetailsView(request, subjectName):
    subjectStudentDetails = StudentMarks.objects.filter(subject__name=subjectName).values('student__firstname', 'student__lastname', 'subject__name', 'marks')
    avgSubjectMarks = Subject.objects.filter(name=subjectName).annotate(average_rating=Avg('studentmarks__marks'))[0].average_rating
    side_bar = {'Home':'home', 'Admin' : 'admin:index'}
    ranges = [ '0-40', '41-60', '61-80', '81-90', '91-100']
    marksRange = {}
    for eachRange in ranges:
        count = StudentMarks.objects.filter(subject__name=subjectName).filter(marks__range=(eachRange.split('-'))).count()
        marksRange[eachRange] = count 
    return render(request, 'StudentSubjectDetails.html', {'subjectStudentDetails' : subjectStudentDetails, 'avgSubjectMarks' : avgSubjectMarks, 'side_bar' : side_bar, 'marksRange' : marksRange, 'subjectName' : subjectName.title() })

