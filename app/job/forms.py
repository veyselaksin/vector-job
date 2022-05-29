from django import forms
from .models import ApplyJob, Job

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [ 'title', 'description', 'job_tag' ]


        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'job_tag': forms.Select(attrs={'class': 'form-control'})
        }

class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = ApplyJob
        fields = ["content", "experience"]

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'experience': forms.Textarea(attrs={'class': 'form-control'})
        }

    