from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.validators import FileExtensionValidator
# Create your models here.


class countrym(models.Model):
    countryid = models.AutoField(primary_key=True)
    countryname = models.CharField(max_length=50)

    def __str__(self):
        return (self.countryname)


class statem(models.Model):
    stateid = models.AutoField(primary_key=True)
    statename = models.CharField(max_length=50)
    countryid = models.ForeignKey(countrym, on_delete=models.CASCADE)

    def __str__(self):
        return (self.statename)


class citym(models.Model):
    cityid = models.AutoField(primary_key=True)
    cityname = models.CharField(max_length=50)
    stateid = models.ForeignKey(statem, on_delete=models.CASCADE)

    def __str__(self):
        return (self.cityname)


class customuser(AbstractUser):
    USER = (('1', "Admin"), ('2', "Faculty"), ('3', "Student"))
    GENDER = (('1', 'Female'), ('2', 'Male'), ('3', 'Other'))
    userid = models.AutoField(primary_key=True)
    middle_name = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(choices=GENDER, max_length=50)
    altemailid = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    altcontact = models.CharField(max_length=50, null=True, blank=True)
    paddressline1 = models.CharField(max_length=50)
    paddressline2 = models.CharField(max_length=50)
    plandmark = models.CharField(max_length=50)
    ppincode = models.CharField(max_length=50)
    pcityid = models.ForeignKey(
        "citym", related_name='pcityid', on_delete=models.CASCADE)
    caddressline1 = models.CharField(max_length=50, null=True, blank=True)
    caddressline2 = models.CharField(max_length=50, null=True, blank=True)
    clandmark = models.CharField(max_length=50, null=True, blank=True)
    cpincode = models.CharField(max_length=50, null=True, blank=True)
    ccityid = models.ForeignKey(
        'citym', related_name='ccityid', on_delete=models.CASCADE, null=True, blank=True)
    usertype = models.CharField(choices=USER, default=3, max_length=50)

    def __str__(self):
        return (str(self.userid)+". "+self.first_name+" "+self.last_name)


class studentm(models.Model):
    studentid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('customuser', on_delete=models.CASCADE)
    # courseid = models.ForeignKey('coursem', on_delete=models.CASCADE)
    enrollnumber = models.IntegerField()
    regionalcentre = models.CharField(max_length=50)
    studentstudycentre = models.CharField(max_length=50)
    medium = models.CharField(max_length=50)

    def __str__(self):
        return (str(self.studentid))


class studentprogramt(models.Model):
    studentid = models.ForeignKey(studentm, on_delete=models.CASCADE)
    programid = models.ForeignKey('programm', on_delete=models.CASCADE)
    enrolldate = models.DateField(auto_now=False, auto_now_add=False)
    admissionyear = models.IntegerField()
    admissionvalidtill = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return (str(self.studentid)+" - "+str(self.programid))


class programm(models.Model):
    programid = models.AutoField(primary_key=True)
    programname = models.CharField(max_length=50)
    programcode = models.CharField(max_length=20)
    minduration = models.IntegerField()
    maxduration = models.IntegerField()

    def __str__(self):
        return (str(self.programcode)+" - "+self.programname)


class programsemestert(models.Model):
    programid = models.ForeignKey(programm, on_delete=models.CASCADE)
    semesterid = models.ForeignKey('semesterm', on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.programid)+" | "+str(self.semesterid))


class semesterm(models.Model):
    semesterid = models.AutoField(primary_key=True)
    semestername = models.CharField(max_length=50)

    def __str__(self):
        return (self.semestername)


class semestercourset(models.Model):
    semesterid = models.ForeignKey(semesterm, on_delete=models.CASCADE)
    courseid = models.ForeignKey('coursem', on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.semesterid)+" | "+str(self.courseid))


class coursem(models.Model):
    courseid = models.AutoField(primary_key=True)
    coursecode = models.CharField(max_length=20)
    coursename = models.CharField(max_length=50)
    coursemaxmarks = models.IntegerField()
    courseminmarks = models.IntegerField()
    programid = models.ForeignKey(programm, on_delete=models.CASCADE)
    semesterid = models.ForeignKey(semesterm, on_delete=models.CASCADE)
    coursetypeid = models.ForeignKey('coursetypem', on_delete=models.CASCADE)
    coursecategoryid = models.ForeignKey(
        'coursecategorym', on_delete=models.CASCADE)

    def __str__(self):
        return (self.coursecode+" - "+self.coursename)


class coursetypem(models.Model):
    coursetypeid = models.AutoField(primary_key=True)
    coursetype = models.CharField(max_length=50, )

    def __str__(self):
        return (self.coursetype)


class coursecategorym(models.Model):
    coursecategoryid = models.AutoField(primary_key=True)
    coursecategory = models.CharField(max_length=50)

    def __str__(self):
        return (self.coursecategory)


class assignmentm(models.Model):
    assignmentid = models.AutoField(primary_key=True)
    subjectname = models.CharField(max_length=50)

    def __str__(self):
        return (str(self.assignmentid)+" - "+self.subjectname)


class studentassignmentt (models.Model):
    studentid = models.ForeignKey(studentm, on_delete=models.CASCADE)
    assignmentid = models.ForeignKey(assignmentm, on_delete=models.CASCADE)
    assignmentname = models.CharField(max_length=20)
    assignmenfile = models.CharField(max_length=50)
    submissiondate = models.DateField(auto_now=True, auto_now_add=False)
    marks = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return (str(self.studentid)+" >> "+self.assignmentname)


class courseexamt(models.Model):
    courseid = models.ForeignKey(coursem, on_delete=models.CASCADE)
    examid = models.ForeignKey('examm', on_delete=models.CASCADE)

    def __str__(self):
        return (self.courseid+" - "+self.examid)


class examm (models.Model):
    examid = models.AutoField(primary_key=True)
    examname = models.CharField(max_length=50)
    examschedule = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return (self.examname+" - "+self.examschedule)


class studentexamt (models.Model):
    studentid = models.ForeignKey(studentm, on_delete=models.CASCADE)
    examid = models.ForeignKey(examm, on_delete=models.CASCADE)

    def __str__(self):
        return (self.studentid+" - "+self.examid)


class crmcomponentm(models.Model):
    crmcomponentid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(
        customuser, on_delete=models.CASCADE, null=True, blank=True)
    crmdate = models.DateTimeField()
    crmsubject = models.CharField(max_length=50)
    voice = models.IntegerField(null=True, blank=True)
    image = models.IntegerField(null=True, blank=True)
    chatbot = models.IntegerField(null=True, blank=True)
    directinquiry = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return (str(self.crmcomponentid)+" - "+self.crmsubject)


class voicem (models.Model):
    voiceid = models.AutoField(primary_key=True)
    crmcomponentid = models.ForeignKey(crmcomponentm, on_delete=models.CASCADE)
    voicefile = models.CharField(max_length=10)
    voicetype = models.CharField(max_length=10)
    resolved = models.BooleanField(default=False)
    remark = models.CharField(max_length=250)
    voicequestiontype = models.CharField(max_length=10)

    def __str__(self):
        return (self.voiceid+" - "+self.voicequestiontype)


class imagem (models.Model):
    imageid = models.AutoField(primary_key=True)
    crmcomponentid = models.ForeignKey(crmcomponentm, on_delete=models.CASCADE)
    imagefile = models.CharField(max_length=10)
    imagetype = models.CharField(max_length=10)
    resolved = models.BooleanField(default=False)
    remark = models.CharField(max_length=250)
    imagequestiontype = models.CharField(max_length=10)

    def __str__(self):
        return (self.imageid+" - "+self.imagequestiontype)


class studentsmsm (models.Model):
    smsid = models.AutoField(primary_key=True)
    crmcomponentid = models.ForeignKey(crmcomponentm, on_delete=models.CASCADE)
    smscontent = models.CharField(max_length=100)
    resolved = models.BooleanField(default=False)
    remark = models.CharField(max_length=250)
    smsquestiontype = models.CharField(max_length=10)

    def __str__(self):
        return (self.smsid+" - "+self.smsquestiontype)


class chatbotquestionm (models.Model):
    chatbotquestionid = models.AutoField(primary_key=True)
    crmcomponentid = models.ForeignKey(crmcomponentm, on_delete=models.CASCADE)
    chatbotquestion = models.CharField(max_length=30)
    chatbotquestiontype = models.CharField(max_length=20)

    def __str__(self):
        return (str(self.chatbotquestionid)+" - "+self.chatbotquestion)


class chatbotanswerm (models.Model):
    chatbotanswerid = models.AutoField(primary_key=True)
    chatbotquestionid = models.ForeignKey(
        chatbotquestionm, on_delete=models.CASCADE)
    chatbotanswer = models.CharField(max_length=60)
    isrelevent = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return (str(self.chatbotquestionid)+" -> "+str(self.chatbotanswerid)+" - "+self.chatbotanswer)


class facultym (models.Model):
    facultyid = models.AutoField(primary_key=True)
    facultyname = models.CharField(max_length=50)
    userid = models.ForeignKey('customuser', on_delete=models.CASCADE)

    def __str__(self):
        return (self.facultyname)


class adminsmst (models.Model):
    smsid = models.ForeignKey('adminsmsm', on_delete=models.CASCADE)
    userid = models.ForeignKey('customuser', on_delete=models.CASCADE)

    def __str__(self):
        return (self.smsid+" - "+self.userid)


class adminsmsm (models.Model):
    smsid = models.AutoField(primary_key=True)
    smsdate = models.DateField(
        auto_now=False, auto_now_add=False, null=True)
    smssubject = models.CharField(max_length=250, default="")
    smscontent = models.CharField(max_length=100)

    def __str__(self):
        return (self.smsid+" - "+self.smsdate)


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d',
                               validators=[FileExtensionValidator(allowed_extensions=['csv'])])
