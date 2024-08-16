from django.contrib import admin
from .models import User, Abilities, AboutMe, Services, Portfolio, Experiences, Education, Contact, SocialMedias


class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'birth_date')


class AbilitiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'percent')


class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('user', 'file_resume', 'profile_photo')


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('project',)


class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_year', 'end_year')


class ExperiencesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_year', 'end_year')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('user', 'platform', 'url')


admin.site.register(User, UserAdmin)
admin.site.register(Abilities, AbilitiesAdmin)
admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Experiences, ExperiencesAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(SocialMedias, SocialMediaAdmin)
