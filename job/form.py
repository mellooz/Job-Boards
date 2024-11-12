from django import forms
from .models import Apply
from .models import Job


class ApplyForm(forms.ModelForm):
    class Meta :
        model = Apply
        fields = ['name', 'email' , 'website' , 'cv' , 'cover_letter']




class JobForm(forms.ModelForm):
    class Meta :
        model = Job
        fields = '__all__'
        # all but exclude this fields slug and owner
        exclude = ('slug' , 'owner')

