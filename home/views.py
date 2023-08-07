from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth import get_user_model
import datetime
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
import re
import os
import csv
import pandas as pd
import json
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth import get_user_model
# user = get_user_model().objects.get()
# Create your views here.


def index(request):
    print(datetime.datetime.now())
    return render(request, 'index.html')


@login_required
def home(request):
    # print(request.user.usertype)
    if request.user.usertype == "1":
        return render(request, "admin/userd.html")
    if request.user.usertype == "2":
        return render(request, "faculty/selfd.html")
    if request.user.usertype == "3":
        return render(request, "student.html")
    # return render(request, 'home.html')


def handlelogin(request):
    if request.method == 'POST':
        # getting the post parameters
        lid = request.POST['loginid']
        lpassword = request.POST['loginpassword']

        # authenticating users
        user = authenticate(username=lid, password=lpassword)

        if user != None:
            utype = user.usertype
            login(request, user)
            # messages.success(request, "Succesfully Logged in")
            if user.usertype == '1':
                return render(request, 'admin.html')
            elif user.usertype == '2':
                return render(request, 'faculty.html')
            elif user.usertype == '3':
                return render(request, 'student.html')
        else:
            return HttpResponse('Invalid Credentials <br><a href="/">Back</a>')
            # messages.success(request, "Invalid Credentials")s
            return redirect('index')

    return HttpResponse('ERROR 404 - NOT FOUND')
    # messages.success(request, "ERROR 404 - NOT FOUND")
    return redirect('index')


@login_required
def handlelogout(request):
    # for sesskey in request.session.keys():
    #     del request.session[sesskey]
    # request.session.flush()
    logout(request)
    return redirect('index')
    return HttpResponse('Not logged out')


@login_required
def rcountry(request):
    list1 = countrym.objects.all()
    return render(request, 'admin/registration.html', {'list1': list1})


@login_required
def registration(request):
    # return render(request, )
    # form = UserCreationForm()
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('admins')
    # else:
    #     form = UserCreationForm()

    list = citym.objects.all()
    return render(request, 'admin/registration.html', {'list': list})
    # country = request.POST.get('country')
    # try:
    #     if(country):
    #         list = statem.objects.filter(countryid=country)
    #         state = request.POST.get('state')
    # except:
    #     pass
    # try:
    #     if(state):
    #         list = ciym.objects.filter(stateid=state)
    #         city = request.POST.get('city')
    # except:
    #     pass
    # return render(request, 'admin/registration.html', {'list': list})


@login_required
def douserregistration(request):
    first_name = request.POST.get('first_name')
    middle_name = request.POST.get('middle_name')
    last_name = request.POST.get('last_name')
    dob = request.POST.get("dob")
    dob = dob.format('Y-m-d')
    gender = request.POST.get("gender")
    emailid = request.POST.get("emailid")
    altemailid = request.POST.get("altemailid")
    contact = request.POST.get("contact")
    altcontact = request.POST.get("altcontact")
    paddressline1 = request.POST.get("paddressline1")
    paddressline2 = request.POST.get("paddressline2")
    plandmark = request.POST.get("plandmark")
    ppincode = request.POST.get("ppincode")
    pcityid = citym.objects.get(cityid=request.POST.get("pcity"))
    caddressline1 = request.POST.get("caddressline1")
    caddressline2 = request.POST.get("caddressline2")
    clandmark = request.POST.get("clandmark")
    cpincode = request.POST.get("cpincode")
    ccityid = request.POST.get("ccityid")
    password = request.POST.get("password")
    usertype = request.POST.get("usertype")
    if customuser.objects.filter(email=emailid).exists():
        return redirect('registration')
        HttpResponse(request, "email is already taken")
        return redirect('registration')
    else:
        user = customuser(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            dob=dob,
            gender=gender,
            email=emailid,
            altemailid=altemailid,
            contact=contact,
            altcontact=altcontact,
            paddressline1=paddressline1,
            paddressline2=paddressline2,
            plandmark=plandmark,
            ppincode=ppincode,
            pcityid=pcityid,
            caddressline1=caddressline1,
            caddressline2=caddressline2,
            clandmark=clandmark,
            cpincode=cpincode,
            ccityid=ccityid,
            username=emailid
        )
    user.set_password(password)
    user.save()
    return redirect('userd')


def bregistration(request):
    if request.method == 'POST':
        file = request.FILES['rfile']

        name = (file.name)
        match = re.search("^.*\.(csv|CSV)$", name)
        if match:

            # df = pd.read_csv(file, delimiter=',', header=1)
            # df.style.hide_index()
            # columns = list(df)
            # for i in df.iterrows():
            # for j in columns:
            # print("hii")
            # print(df.to_string(index=False))
            # print(df)
            fs = FileSystemStorage()
            fs.save(file.name, file)
            path = "media/"+name
            with open(path, 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter='|')
                line_count = 1
                for row in csv_reader:
                    for colomn in csv_reader:
                        # print("hii")
                        print(colomn)
                        data = (colomn)
                        j = 0
                        for i in data:

                            if j == 0:
                                print(j)
                                request.session["first_name"] = i
                            if j == 1:
                                print(j)
                                request.session["middle_name"] = i
                            if j == 2:
                                print(j)
                                request.session["last_name"] = i
                            if j == 3:
                                print(j)
                                request.session["dob"] = i
                            if j == 4:
                                print(j)
                                request.session["gender"] = i
                            if j == 5:
                                print(j)
                                request.session["emailid"] = i
                            if j == 6:
                                print(j)
                                request.session["altemailid"] = i
                            if j == 7:
                                print(j)
                                request.session["contact"] = i
                            if j == 8:
                                print(j)
                                request.session["altcontact"] = i
                            if j == 9:
                                print(j)
                                request.session["paddressline1"] = i
                            if j == 10:
                                print(j)
                                request.session["paddressline2"] = i
                            if j == 11:
                                print(j)
                                request.session["plandmark"] = i
                            if j == 12:
                                print(j)
                                request.session["ppincode"] = i
                            if j == 13:
                                print(j)
                                request.session["pcityid"] = i
                            if j == 14:
                                print(j)
                                request.session["caddressline1"] = i
                            if j == 15:
                                print(j)
                                request.session["caddressline2"] = i
                            if j == 16:
                                print(j)
                                request.session["clandmark"] = i
                            if j == 17:
                                print(j)
                                request.session["cpincode"] = i
                            if j == 18:
                                print(j)
                                request.session["ccityid"] = i
                            if j == 19:
                                print(j)
                                request.session["password"] = i
                            if j == 20:
                                print(j)
                                k = i
                                k = request.session["pcityid"]
                                pcity = citym.objects.get(pk=k)

                                user = customuser(
                                    first_name=request.session["first_name"],
                                    middle_name=request.session["middle_name"],
                                    last_name=request.session["last_name"],
                                    dob=request.session["dob"],
                                    gender=request.session["gender"],
                                    email=request.session["emailid"],
                                    altemailid=request.session["altemailid"],
                                    contact=request.session["contact"],
                                    altcontact=request.session["altcontact"],
                                    paddressline1=request.session["paddressline1"],
                                    paddressline2=request.session["paddressline2"],
                                    plandmark=request.session["plandmark"],
                                    ppincode=request.session["ppincode"],
                                    pcityid=pcity,
                                    caddressline1=request.session["caddressline1"],
                                    caddressline2=request.session["caddressline2"],
                                    clandmark=request.session["clandmark"],
                                    cpincode=request.session["cpincode"],
                                    username=request.session["emailid"],
                                )
                                if(request.session["ccityid"] is not ""):
                                    m = request.session["ccityid"]
                                    user.ccityid = citym.objects.get(pk=m)
                                else:
                                    pass
                                passw = request.session["password"]
                                user.set_password(passw)
                                user.save()
                                print(j)
                            j = j+1

            print(f'Processed {line_count} lines.')
        os.remove(path)
        return redirect('userd')

    else:
        return render(request, 'admin/bregistration.html')


@login_required
def deleteuser(request):
    if request.method == "POST":
        userlist = request.POST.getlist("userlist")
        for i in userlist:
            a = customuser.objects.get(pk=i)
            a.delete()
        return redirect("userd")
    else:
        list1 = customuser.objects.filter(Q(usertype="3") | Q(usertype="2"))
        return render(request, "admin/deleteuser.html", {"list1": list1})


@ login_required
def fselfd(request):
    cr = request.user.userid
    student_list = customuser.objects.filter(userid=cr)
    return render(request, 'faculty/selfd.html', {'data': student_list})


@ login_required
def sselfd(request):
    student_list = request.user
    # list2 = studentm.objects.filter(user=request.user)
    return render(request, 'student/selfd.html', {'data': student_list})


@ login_required
def studentd(request):
    student_list = customuser.objects.filter(usertype="3")
    return render(request, 'faculty/studentd.html', {'student_list': student_list})


@ login_required
def userd(request):
    student_list = customuser.objects.all()
    return render(request, 'admin/userd.html', {'student_list': student_list})


@ login_required
def message(request):
    return render(request, 'admin/message.html')


@ login_required
def queries(request):
    return render(request, 'admin/queries.html')


@ login_required
def new(request):
    return render(request, 'admin/new.html')


# Twilio -- twilio(num, msg) to send message
def twilio(num, msg):
    pnum = ''
    msg2snd = ''
    pnum = '+91'+num
    msg2snd = msg
    from twilio.rest import Client
    sid = 'ACb37dba56c0153279701e9ce27f032f12'
    auth_token = 'c19a6bcfb7396edb7887793887b67bde'
    client = Client(sid, auth_token)
    resp = client.messages.create(body=msg2snd, from_="+19087748645", to=pnum)
    print(num+"  :  "+msg)
    print(resp.sid)


def viewmessage(request):
    msg_list = adminsmsm.objects.all()
    return render(request, "admin/viewmessage.html", {"msg_list": msg_list})


def sendmessage(request):
    if request.method == "POST":
        if 'choosemsg' in request.POST:
            id = request.POST.get("checklist")
            request.session['msgid'] = id
            list1 = customuser.objects.filter(
                Q(usertype="3") | Q(usertype="2"))
            return render(request, "admin/sendmessage2.html", {"list1": list1})
        if 'chooseuser' in request.POST:
            tid = request.session["msgid"]
            temp = adminsmsm.objects.get(pk=tid)
            sms = temp.smscontent
            userlist = request.POST.getlist("userlist")
            for i in userlist:
                a = customuser.objects.get(pk=i)
                num = a.contact
                print(num)
                # obj = adminsmst()
                # obj.smsid = temp
                # obj.userid = a
                # obj.save()
                twilio(num, sms)
            return redirect("viewmessage")
    else:
        list2 = adminsmsm.objects.all()
        return render(request, "admin/sendmessage.html", {"list2": list2})


def createmessage(request):
    if request.method == "POST":
        msg = adminsmsm()
        msg.smssubject = request.POST.get("smssubject")
        date = request.POST.get("smsdate")
        msg.smsdate = date.format('Y-m-d')
        msg.smscontent = request.POST.get("smscontent")
        msg.save()
        return render(request, "admin/viewmessage.html")
    else:
        return render(request, "admin/createmessage.html")


def deletemessage(request):
    if request.method == "POST":
        dlist = request.POST.getlist('checklist')
        print(dlist)
        for i in dlist:
            obj = adminsmsm.objects.get(pk=i)
            obj.delete()
        return render(request, "admin/viewmessage.html")
    else:
        msg_list = adminsmsm.objects.all()
        return render(request, "admin/deletemessage.html", {"msg_list": msg_list})


def assignmentsubmission(request):
    if request.method == "POST":
        file = request.FILES['rfile']
        name = (file.name)
        match = re.search("^.*\.(pdf|PDF)$", name)
        if match:
            fs = FileSystemStorage()
            fs.save(file.name, file)
            a = studentassignmentt()
            cr = request.user
            a.studentid = studentm.objects.get(userid=cr.userid)
            a.assignmentid = assignmentm.objects.get(
                assignmentid=request.POST.get("aid"))
            one = assignmentm.objects.get(assignmentid=request.POST.get("aid"))
            a.assignmentname = one.subjectname
            a.assignmenfile = file.name
            a.save()
            return redirect('home')

    else:
        list1 = assignmentm.objects.all()
        return render(request, "student/assignmentsubmission.html", {"list1": list1})
