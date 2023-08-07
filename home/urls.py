from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('admin', admin.site.urls),
    path('home', views.home, name='home'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
    # path('admins', views.admin, name='admin'),
    # path('faculty', views.faculty, name='faculty'),
    # path('student', views.student, name='student'),
    path('registration', views.registration, name='registration'),
    path('userd', views.userd, name='userd'),
    path('studentd', views.studentd, name='studentd'),
    path('fselfd', views.fselfd, name="fselfd"),
    path('sselfd', views.sselfd, name="sselfd"),
    path('message', views.message, name="message"),
    path('queries', views.queries, name="queries"),
    path('new', views.new, name='new'),
    path('douserregistration', views.douserregistration, name="douserregistration"),
    path('sendmessage', views.sendmessage, name="sendmessage"),
    path('viewmessage', views.viewmessage, name="viewmessage"),
    path('createmessage', views.createmessage, name="createmessage"),
    path('deletemessage', views.deletemessage, name="deletemessage"),
    path('bregistration', views.bregistration, name="bregistration"),
    path('assignmentsubmission', views.assignmentsubmission, name="assignmentsubmission"),
    path('deleteuser', views.deleteuser, name="deleteuser"),
    #path('registration', admin.site.urls),
    #path('loggedin', views.loggedin, name='loggedin'),
    # path('rcountry',views.rcountry,name='rcountry')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
