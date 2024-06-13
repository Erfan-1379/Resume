from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from core.models import CustomUser
from .models import *


class ProfileView(TemplateView):
    template_name = 'main/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_user'] = CustomUser.objects.get()
        context['user'] = User.objects.get(user__is_superuser=True)
        context['about_me'] = AboutMe.objects.first()
        context['services'] = Services.objects.all()
        context['portfolios'] = Portfolio.objects.all()
        context['categories'] = Portfolio.CATEGORY_CHOICES
        context['experiences'] = Experiences.objects.all()
        context['educations'] = Education.objects.all()
        context['abilities'] = Abilities.objects.all().order_by('-percent')
        return context


def dashboard(request):
    models_dashboard = []
    models = [Abilities, AboutMe, Services, Portfolio, Experiences, Education]
    for model_class in models:
        model_name = model_class.__name__
        model_instances = model_class.objects.all().order_by('-percent') if model_class == Abilities \
            else model_class.objects.all()
        if model_instances.exists():
            instances_data = []
            for instance in model_instances:
                first_field_name = model_class._meta.fields[1].name
                instances_data.append({'id': instance.pk, 'title': getattr(instance, first_field_name),
                                       'edit_url': reverse(f'{model_name.lower()}-update', kwargs={'pk': instance.pk}),
                                       'delete_url': reverse(f'{model_name.lower()}-delete',
                                                             kwargs={'pk': instance.pk}), })
            models_dashboard.append(
                {'name': model_name, 'instances': instances_data, 'add_url': reverse(f'{model_name.lower()}'), })
        else:
            models_dashboard.append(
                {'name': model_name, 'instances': None, 'add_url': reverse(f'{model_name.lower()}'), })
    return render(request, 'main/admins.html', {'models': models_dashboard})


class AbilityCreateView(generic.CreateView):
    model = Abilities
    fields = '__all__'
    template_name = 'forms/abilities.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AbilityUpdateView(generic.UpdateView):
    model = Abilities
    fields = '__all__'
    template_name = 'forms/abilities-update.html'


class AbilityDeleteView(generic.DeleteView):
    model = Abilities
    template_name = 'forms/abilities-delete.html'
    success_url = reverse_lazy('admin')


class AboutMeCreateView(generic.CreateView):
    model = AboutMe
    fields = '__all__'
    template_name = 'forms/aboutme.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AboutMeUpdateView(generic.UpdateView):
    model = AboutMe
    fields = '__all__'
    template_name = 'forms/aboutme-update.html'


class AboutMeDeleteView(generic.DeleteView):
    model = AboutMe
    template_name = 'forms/aboutme-delete.html'
    success_url = reverse_lazy('admin')


class ServiceCreateView(generic.CreateView):
    model = Services
    fields = '__all__'
    template_name = 'forms/service.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ServiceUpdateView(generic.UpdateView):
    model = Services
    fields = '__all__'
    template_name = 'forms/service-update.html'


class ServiceDeleteView(generic.DeleteView):
    model = Services
    template_name = 'forms/service-delete.html'
    success_url = reverse_lazy('admin')


class PortfolioCreateView(generic.CreateView):
    model = Portfolio
    fields = '__all__'
    template_name = 'forms/portfolio.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PortfolioUpdateView(generic.UpdateView):
    model = Portfolio
    fields = '__all__'
    template_name = 'forms/portfolio_update.html'


class PortfolioDeleteView(generic.DeleteView):
    model = Portfolio
    template_name = 'forms/portfolio_delete.html'
    success_url = reverse_lazy('admin')


class ExperiencesCreateView(generic.CreateView):
    model = Experiences
    fields = '__all__'
    template_name = 'forms/experiences.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExperiencesUpdateView(generic.UpdateView):
    model = Experiences
    fields = '__all__'
    template_name = 'forms/experiences-update.html'


class ExperiencesDeleteView(generic.DeleteView):
    model = Experiences
    template_name = 'forms/experiences-delete.html'
    success_url = reverse_lazy('admin')


class EducationCreateView(generic.CreateView):
    model = Education
    fields = '__all__'
    template_name = 'forms/education.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EducationUpdateView(generic.UpdateView):
    model = Education
    fields = '__all__'
    template_name = 'forms/education-update.html'


class EducationDeleteView(generic.DeleteView):
    model = Education
    template_name = 'forms/education-delete.html'
    success_url = reverse_lazy('admin')
