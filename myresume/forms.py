from django import forms
from .models import User, AboutMe, Services, Portfolio, Experiences, Education


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user', 'phone_number', 'address', 'birth_date']


class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = ['user', 'profile_photo', 'bio', 'file_resume']


class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['title', 'description']


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['project', 'image_project']
        labels = {'project': 'Project Name', 'Image Project': 'Image'}


class ExperiencesForm(forms.ModelForm):
    class Meta:
        model = Experiences
        fields = ['title', 'description', 'start_date', 'end_date']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['title', 'description', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

