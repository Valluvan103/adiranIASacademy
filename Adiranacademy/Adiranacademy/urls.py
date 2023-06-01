"""Adiranacademy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from onlineExam import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_app/',include('student_app.urls')),


    #path('',views.home,name='home'),
    path('',views.home_view,name=''),
    path('logout', LogoutView.as_view(template_name='logout.html'),name='logout'),

    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='admin_login.html'),name='adminlogin'),
    path('afterlogin', views.after_login_view,name='afterlogin'),
    
    path('studentbase',views.studentbase,name='studentbase'),
    path('adminbase',views.adminbase,name='adminbase'),
    #path('admin_home',views.admin,name='admin_home'),
    path('admin_dashboard',views.admin_dashboard_view,name='admin_dashboard'),
    
    path('admin_student',views.admin_student_view,name='admin_student'),
    path('admin_view_student',views.admin_view_student_view,name='admin_view_student'),
    path('admin_view_student_marks',views.admin_view_student_marks_view,name='admin_view_student_marks'),
    path('admin_view_marks_view/<int:pk>',views.admin_view_marks_view,name='admin_view_marks_view'),
    path('admin_check_marks_view/<int:pk>',views.admin_check_marks_view,name='admin_check_marks_view'),
    path('update_student/<int:pk>',views.update_student_view,name='update_student'),
    path('delete_student/<int:pk>',views.delete_student_view,name='delete_student'),

    path('admin_course',views.adminbase_course_view,name='admin_course'),
    path('admin_add_course',views.admin_add_course_view,name='admin_add_course'),
    path('admin_view_course/<int:pk>',views.admin_view_course_view,name='admin_view_course'),
    path('admin_course_view',views.admin_course_view,name='admin_course_view'),
    path('update_course/<int:pk>',views.update_course_view,name='update_course'),
    path('delete_course/<int:pk>',views.delete_course_view,name='delete_course'),
    
    path('admin_question',views.admin_question_view,name='admin_question'),
    path('admin_add_question',views.admin_add_question_view,name='admin_add_question'),
    path('admin_view_question',views.admin_view_question_view,name='admin_view_question'),
    path('view_question_view/<int:pk>',views.view_question_view,name='view_question_view'),
    path('update_question/<int:pk>',views.update_question_view,name='update_question'),
    path('delete_question/<int:pk>',views.delete_question_view,name='delete_question'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
