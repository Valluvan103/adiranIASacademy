from django.shortcuts import render,redirect,reverse
from onlineExam.forms import QuestionForm,CourseForm
from django.http import HttpResponseRedirect
from onlineExam.models import Questions,Course,Result
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from student_app.models import Student
from django.db.models import Sum
from student_app.forms import StudentUserForm,StudentForm
# Create your views here.

# home page 

def home_view(request):
	#if request.user.is_authenticated:
	#	return HttpResponseRedirect('after_login')
	return render(request,'index.html')
"""def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()
"""
def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

def after_login_view(request):
	if is_student(request.user):
		return redirect('studentbase')
	else:
		return redirect('adminbase')

def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')

# admin dashboad 
def adminbase(request):
	return render(request,'adminbase.html')

def admin_dashboard_view(request):
	total_students=Student.objects.all().count()
	total_course=Course.objects.all().count()
	total_questions=Questions.objects.all().count()
	dict={
	'total_students':total_students,
	'total_course':total_course,
	'total_questions':total_questions,
	}
	

	return render(request,'admin_dashboard.html',context=dict)

def admin_student_view(request):
	dict={
	'total_students':Student.objects.all().count()
	}
	return render(request,'admin_student.html',context=dict)

def admin_view_student_view(request):
	students=Student.objects.all()
	return render(request,'admin_view_student_view.html',{'students':students})

def update_student_view(request,pk):
	student=Student.objects.get(id=pk)
	user=User.objects.get(id=student.user_id)
	userForm=StudentUserForm(instance=user)
	studentForm=StudentForm(request.FILES,instance=student)
	mydict={'userForm':userForm,'studentForm':studentForm}
	if request.method=='POST':
		userForm=StudentUserForm(request.POST,instance=user)
		studentForm=StudentForm(request.POST,request.FILES,instance=student)
		if userForm.is_valid() and studentForm.is_valid():
			user=userForm.save()
			user.set_password(user.password)
			user.save()
			studentForm.save()
			return redirect('admin_view_student')
	return render(request,'update_student.html',context=mydict)

def delete_student_view(request,pk):
	student=Student.objects.get(id=pk)
	user=User.objects.get(id=student.user_id)
	user.delete()
	student.delete()
	return redirect('admin_view_student')


def studentbase(request):
	return render(request,'student/studentbase.html')

def adminbase(request):
	return render(request,'adminbase.html')
#def admin(request):
#	return render(request,'admin.html')

# course Page 

def adminbase_course_view(request):
	return render(request,'admin_course.html')

def admin_add_course_view(request):
	courseForm=CourseForm()
	if request.method=='POST':
		courseForm=CourseForm(request.POST)
		if courseForm.is_valid():
			courseForm.save()
		else:
		    print("form is invalid")
		return HttpResponseRedirect('/admin_course_view')
	return render(request,'admin_add_course.html',{'courseForm':courseForm})
def update_course_view(request, pk):
    course = Course.objects.get(id=pk)
    courseForm = CourseForm(instance=course)
    

    if request.method == 'POST':
        courseForm = CourseForm(request.POST, instance=course)
        if courseForm.is_valid():
            courseForm.save()
            return redirect('/admin_course_view',pk=pk)
        else:
            print("form is invalid")
            
    return render(request, 'admin_update_course.html', {'courseForm': courseForm, 'course': course})

def admin_course_view(request):
	courses = Course.objects.all()
	
	return render(request,'admin_course_view.html',{'courses':courses})


def admin_view_course_view(request,pk):
	#courses = Course.objects.annotate(total_marks_sum=Sum('questions__marks'))
	
	course=Course.objects.get(id=pk)
	total_questions=Questions.objects.all().filter(course=course).count()
	questions=Questions.objects.all().filter(course=course)
	
	total_marks=0
	for q in questions:
		total_marks=total_marks + q.marks

	url = reverse('admin_view_course', args=[pk])
	return render(request,'admin_view_course.html',{'url':url,'course':course,'total_questions':total_questions,'total_marks':total_marks})

	
def delete_course_view(request,pk):
	course=Course.objects.get(id=pk)
	course.delete()
	return HttpResponseRedirect('/admin_course_view')

# question page

def admin_question_view(request):
	return render(request,'admin_question.html')

def admin_add_question_view(request):
    questionForm = QuestionForm()
    if request.method == 'POST':
        questionForm = QuestionForm(request.POST)
        if questionForm.is_valid():
            question = questionForm.save(commit=False)
            course = Course.objects.get(id=request.POST.get('courseID'))
            question.course = course
            question.save()
            return HttpResponseRedirect('/admin_add_question')
        else:
            print("form is invalid")
            print(questionForm.errors)
    return render(request, 'admin_add_question.html', {'questionForm': questionForm})



"""def update_question_view(request, pk):
    question = Question.objects.get(id=pk)
    questionForm = QuestionForm(instance=question)
    
    if request.method == 'POST':
        questionForm = QuestionForm(request.POST, instance=question)
        if questionForm.is_valid():
            question = questionForm.save(commit=False)
            course = Course.objects.get(id=request.POST.get('courseID'))
            question.course = course
            question.save()
            return HttpResponseRedirect('/admin_view_question/')
        else:
            print("form is invalid")
            print(questionForm.errors)
            
    return render(request, 'admin_update_question.html', {'questionForm': questionForm, 'question': question})"""


def update_question_view(request,pk):
	question=Questions.objects.get(id=pk)
	questionForm=QuestionForm(instance=question)

	if request.method=='POST':
		questionForm=QuestionForm(request.POST,instance=question)
		if questionForm.is_valid():
			question=questionForm.save(commit=False)
			course=Course.objects.get(id=request.POST.get('courseID'))
			question.course=course
			question.save()
			return redirect('admin_view_question')
		else:
			print('form is invalid')
			print(questionForm.errors)
	return render(request,'admin_update_question.html',{'questionForm':questionForm,'question':question})

def admin_view_question_view(request):
	courses = Course.objects.all()
	return render(request,'admin_view_question_view.html',{'courses':courses})

def delete_question_view(request,pk):
	question=Questions.objects.get(id=pk)
	question.delete()
	return HttpResponseRedirect('/admin_view_question')

def view_question_view(request,pk):
    questions=Questions.objects.all().filter(course_id=pk)
    return render(request,'view_question.html',{'questions':questions})


def admin_view_student_marks_view(request):
	students=Student.objects.all()
	return render(request,'admin_view_student_marks.html',{'students':students})

def admin_view_marks_view(request,pk):
	courses=Course.objects.all()
	response= render(request,'admin_view_marks_view.html',{'courses':courses})
	response.set_cookie('student_id',pk)
	return response

def admin_check_marks_view(request,pk):
	course=Course.objects.get(id=pk)
	student_id=request.COOKIES.get('student_id')
	student=Student.objects.get(id=student_id)
	results=Result.objects.all().filter(exam=course).filter(student=student)

	return render(request,'admin_check_marks_view.html',{'results':results})









"""
def admin_add_course_view(request):
    subjectForm=SubjectForm()
    if request.method=='POST':
        subjectForm=SubjectForm(request.POST)
        if subjectForm.is_valid():        
            subjectForm.save()
        #else:
         #   print("form is invalid")
       # return HttpResponseRedirect('/admin-view-course')
    return render(request,'admin_add_course.html',{'subjectForm':subjectForm})
"""
