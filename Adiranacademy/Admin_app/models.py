from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

"""class Teacher(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	address=models.CharField(max_length=50)
	mobile=models.CharField(max_length=10,null=False)
	status=models.BooleanField(default=False)

    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name"""