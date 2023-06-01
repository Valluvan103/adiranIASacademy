from django.db import models
from django.contrib.auth.models import User
#from onlineExam.models import Course,Questions,Result

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_pic= models.ImageField(upload_to='profile_pic',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
   
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name

"""class Examsubmission(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    questions=models.CharField(max_length=600)
    marks=models.CharField(max_length=10)
    selected_ans=models.CharField(max_length=400)

"""