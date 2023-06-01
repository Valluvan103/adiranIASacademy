from django import forms
from django.contrib.auth.models import User
from onlineExam.models import Questions,Course

class CourseForm(forms.ModelForm):
	class Meta:
		model=Course
		fields='__all__'

class QuestionForm(forms.ModelForm):
    courseID = forms.ModelChoiceField(queryset=Course.objects.all(),empty_label="Course Name", to_field_name="id")
    question = forms.CharField(label='Question', widget=forms.Textarea, required=True)
    marks = forms.IntegerField(label='Marks', required=True)
    option1 = forms.CharField(label='Option 1', max_length=500, required=True)
    option2 = forms.CharField(label='Option 2', max_length=500, required=True)
    option3 = forms.CharField(label='Option 3', max_length=500, required=True)
    option4 = forms.CharField(label='Option 4', max_length=500, required=True)
    

    class Meta:
        model = Questions
        fields = ['courseID', 'question', 'marks', 'option1', 'option2', 'option3', 'option4', 'answer']


"""class QuestionForm(forms.ModelForm):
	#this will show dropdown __str__ method course model is shown on html so override it
	#to_field_name this will fetch corresponding value  user_id present in course model and return it
	courseID=forms.ModelChoiceField(queryset=Course.objects.all(),empty_label="Course Name", to_field_name="id")
	class Meta:
		model=Questions
		fields='__all__'
		widgets = {
			'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})
		}

	def clean(self):
		cleaned_data = super().clean()
		course_id = cleaned_data.get('courseID')
		if not course_id:
			raise forms.ValidationError("Course ID is required")"""