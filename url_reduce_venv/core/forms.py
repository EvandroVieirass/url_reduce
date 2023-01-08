from django import forms
from core.models import Links

class FormLink(forms.ModelForm):
	class Meta:
		model = Links
		fields = '__all__'