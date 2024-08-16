from django import forms
from .models import User, AboutMe, Services, Portfolio, Experiences, Education, Contact, SocialMedias, Abilities


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user', 'phone_number', 'address', 'birth_date']


class AbilityForm(forms.ModelForm):
    class Meta:
        model = Abilities
        fields = ['name', 'percent']


class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = ['profile_photo', 'bio', 'file_resume']


class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['title', 'description']


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['project', 'image_project', 'category']
        labels = {'project': 'Project Name', 'image_project': 'Image'}


class ExperiencesForm(forms.ModelForm):
    class Meta:
        model = Experiences
        fields = ['title', 'description', 'start_year', 'end_year']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['title', 'description', 'start_year', 'end_year']
        widgets = {
            'start_year': forms.DateInput(attrs={'type': 'date'}),
            'end_year': forms.DateInput(attrs={'type': 'date'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']


class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialMedias
        fields = ['platform', 'url']