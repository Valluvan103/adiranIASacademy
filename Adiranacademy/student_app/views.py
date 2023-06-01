from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponseBadRequest
from student_app.forms import StudentUserForm,StudentForm
from django.contrib.auth.models import Group
from django.db.models import Sum
from django.conf import settings
from datetime import date, timedelta
from onlineExam.models import Questions,Course,Result
from student_app.models import Student

# Create your views here.

def studentclick_view(request):
	#if request.user.is_authenticated:
	#	return HttpResponseRedirect('afterlogin')
	return render(request,'student/studentclick.html')


def student_signup_view(request):
	userForm = StudentUserForm()
	studentForm=StudentForm()
	mydict={'userForm':userForm,'studentForm':studentForm}
	if request.method=='POST':
		userForm=StudentUserForm(request.POST)
		studentForm=StudentForm(request.POST,request.FILES)
		if userForm.is_valid() and studentForm.is_valid():
			user=userForm.save()
			user.set_password(user.password)
			user.save()
			student=studentForm.save(commit=False)
			student.user=user
			student.save()
			my_student_group = Group.objects.get_or_create(name='STUDENT')
			my_student_group[0].user_set.add(user)
		return HttpResponseRedirect('studentlogin')
	return render(request,'student/student_signup.html',context=mydict)


def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

def student_dashboard_view(request):
	dict={
	'total_course':Course.objects.all().count(),
	'total_questions':Questions.objects.all().count(),
	}
	return render(request,'student/student_dashboard.html',context=dict)

def student_exam_view(request):
	courses=Course.objects.all()
	return render(request,'student/student_exam_view.html',{'courses':courses})

def take_exam_view(request,pk):
	course=Course.objects.get(id=pk)
	total_questions=Questions.objects.all().filter(course=course).count()
	questions=Questions.objects.all().filter(course=course)
	total_marks=0
	for q in questions:
		total_marks=total_marks + q.marks
	return render(request,'student/take_exam_view.html',{'course':course,'total_questions':total_questions,'total_marks':total_marks})

"""def start_exam_view(request,pk):
	course=Course.objects.get(id=pk)
	questions=Questions.objects.all().filter(course=course)
	if request.method=='POST':
		pass
	return render(request,'student/start_exam.html',{'course':course,'questions':questions})
	#response.set_cookie('course_id',course.id)
	#return response
"""
def start_exam_view(request, course_id):
	courses=Course.objects.all()
	course = Course.objects.get(id=course_id)
	questions = Questions.objects.all().filter(course=course)

	total_marks = 0
	obtained_marks = 0

	if request.method == 'POST':
		for q in questions:
			selected_option = request.POST.get(str(q.id))
			print(selected_option)
			if selected_option == q.answer:
				obtained_marks += q.marks
			total_marks += q.marks
		student = Student.objects.get(user_id=request.user.id)
		result=Result()
		result.marks=obtained_marks
		result.exam=course
		result.student=student
		result.save()

		return render(request, 'student/view_result.html', {'courses':courses})

	return render(request, 'student/start_exam.html', {'course': course, 'questions': questions})


def check_marks_view(request,pk):
	#marks=Result.objects.get(marks=marks)
	course=Course.objects.get(id=pk)
	student=Student.objects.get(user_id=request.user.id)
	results=Result.objects.all().filter(exam=course).filter(student=student)
	return render(request,'student/check_marks_view.html',{'results':results})

def student_marks_view(request):
	courses=Course.objects.all()
	return render(request,'student/student_marks_view.html',{'courses':courses})