from django.contrib import admin
from StudentWebsite.StudentApp.models import Student, Subject, StudentMarks

#This is just for dispaly order of columns for Author
class StudentAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname')
    search_fields = ('firstname', 'lastname')
    ordering = ('-firstname',)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    ordering = ('-name',)
    fields = ('name',)

class StudentMarksAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'marks')
    list_filter = ('student', 'subject', 'marks')
    ordering = ('-student',)

admin.site.register(Student, StudentAdmin) #StudentAdmin is just for display in Admin page
admin.site.register(Subject, SubjectAdmin) #SubjectAdmin is just for display in Admin page
admin.site.register(StudentMarks, StudentMarksAdmin)