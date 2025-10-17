from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django_resized import ResizedImageField


class User(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user}'


class Abilities(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    percent = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('admin')


class AboutMe(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_photo = ResizedImageField(upload_to='profile_photos', size=[600, 600], crop=['middle', 'center'],
                                      validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    file_resume = models.FileField(upload_to='file-resume/', validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])])

    def __str__(self):
        return f'{self.bio}'

    def get_absolute_url(self):
        return reverse('admin')


class SocialMedias(models.Model):
    PLATFORM_CHOICES = [
        ('telegram', 'Telegram'),
        ('instagram', 'Instagram'),
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter'),
        ('skype', 'Skype'),
        ('github', 'GitHub')
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='social_medias')
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.platform}'

    def get_absolute_url(self):
        return reverse('admin')


class Services(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('admin')


class Portfolio(models.Model):

    CATEGORY_CHOICES = [
        ('python', 'Python'),
        ('django', 'Django'),
        ('php', 'PHP'),
    ]
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    project = models.CharField(max_length=255, null=True, blank=True)
    link_project = models.URLField(null=True, blank=True)
    image_project = ResizedImageField(upload_to='images/', size=[1000, 667], crop=['middle', 'center'])
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='all_projects')

    def __str__(self):
        return f'{self.project}'

    def get_absolute_url(self):
        return reverse('admin')


class Experiences(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start_year = models.IntegerField(
        null=True, blank=True,
        validators=[MinValueValidator(1900), MaxValueValidator(timezone.now().year)]
    )
    end_year = models.IntegerField(
        null=True, blank=True,
        validators=[MinValueValidator(1900), MaxValueValidator(timezone.now().year)]
    )

    def get_absolute_url(self):
        return reverse('admin')

    def __str__(self):
        return f'{self.title}'


class Education(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start_year = models.IntegerField(
        null=True, blank=True,
        validators=[MinValueValidator(1900), MaxValueValidator(timezone.now().year)]
    )
    end_year = models.IntegerField(
        null=True, blank=True,
        validators=[MinValueValidator(1900), MaxValueValidator(timezone.now().year)]
    )

    def get_absolute_url(self):
        return reverse('admin')

    def __str__(self):
        return f'{self.title}'


class Contact(models.Model):
    name = models.CharField(max_length=155)
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
