# -*- coding: utf-8 -*-
from django import forms
from StudentWebsite.StudentApp.models import Subject

class SubjectForm(forms.Form):
    subjects = forms.ModelChoiceField(queryset=Subject.objects.values('pk','name').order_by('name'))