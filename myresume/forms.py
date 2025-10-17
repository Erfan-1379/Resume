from django import forms
from .models import User, AboutMe, Services, Portfolio, Experiences, Education, Contact, SocialMedias, Abilities
import re


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
        fields = ['project', 'link_project', 'image_project', 'category']
        labels = {'project': 'Project Name', 'image_project': 'Image'}


class ExperiencesForm(forms.ModelForm):
    class Meta:
        model = Experiences
        fields = ['title', 'description', 'start_year', 'end_year']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['title', 'description', 'start_year', 'end_year']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        pattern = r'^(?:\+98|0)?9\d{9}$'
        if not re.match(pattern, phone):
            raise forms.ValidationError("شماره باید یک شماره معتبر موبایل ایران باشد.")
        return phone

class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialMedias
        fields = ['platform', 'url']