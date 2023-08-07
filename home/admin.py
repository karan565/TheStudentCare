from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from home.models import customuser, countrym, statem, citym, studentm, studentprogramt, programm, programsemestert, semesterm, semestercourset, coursem, coursetypem, coursecategorym, assignmentm, studentassignmentt, courseexamt, examm, studentexamt, crmcomponentm, voicem, imagem, studentsmsm, chatbotquestionm, chatbotanswerm, facultym, adminsmst, adminsmsm

admin.site.site_header = 'LJ IGNOU Admin'
admin.site.index_title = 'Welcome'
admin.site.site_title = ' Admin'
# admin.site.unregister(Group)


# class display(admin.ModelAdmin):
#     list_display = ('userid', 'first_name')

admin.site.register(customuser)
admin.site.register(countrym)
admin.site.register(statem)
admin.site.register(citym)
admin.site.register(studentm)
admin.site.register(studentprogramt)
admin.site.register(programm)
admin.site.register(programsemestert)
admin.site.register(semesterm)
admin.site.register(semestercourset)
admin.site.register(coursem)
admin.site.register(coursetypem)
admin.site.register(coursecategorym)
admin.site.register(assignmentm)
admin.site.register(studentassignmentt)
admin.site.register(courseexamt)
admin.site.register(examm)
admin.site.register(studentexamt)
admin.site.register(crmcomponentm)
admin.site.register(voicem)
admin.site.register(imagem)
admin.site.register(studentsmsm)
admin.site.register(chatbotquestionm)
admin.site.register(chatbotanswerm)
admin.site.register(facultym)
admin.site.register(adminsmst)
admin.site.register(adminsmsm)
