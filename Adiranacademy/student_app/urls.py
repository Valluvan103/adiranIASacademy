from django.contrib import admin
from django.urls import path
from student_app import views
from django.contrib.auth.views import LoginView


urlpatterns = [
	path('studentclick',views.studentclick_view),
	path('studentlogin',LoginView.as_view(template_name='student/student_login.html'),name='studentlogin'),
	path('student_signup',views.student_signup_view,name='student_signup'),
	path('student_dashboard',views.student_dashboard_view,name='student_dashboard'),
	path('student_exam_view',views.student_exam_view,name='student_exam_view'),
	path('take_exam/<int:pk>',views.take_exam_view,name='take_exam'),
	path('start_exam/<int:course_id>',views.start_exam_view,name='start_exam'),
	#path('calculate_marks',views.calculate_marks_view,name='calculate_marks'),
	#path('view_result',views.view_result_view,name='view_result'),
	path('check_marks/<int:pk>',views.check_marks_view,name='check_marks'),
	path('student_marks_view',views.student_marks_view,name='student_marks_view'),

]