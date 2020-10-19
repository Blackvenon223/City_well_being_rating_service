from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Field,Layout,Div
from django.forms.widgets import NumberInput

class RateForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['zone_crime_level','zone_roads_health','zone_ecology_level','zone_medicine_level']
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Rate'))
		for field in self.fields:
			self.fields[field].widget = NumberInput(attrs={'type':'range', 'list':'range' , 'step': '2','class':'custom-range','min':'1','max':'100'})

		
class SignupForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']



