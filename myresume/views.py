from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import JsonResponse, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from core.forms import CustomUserCreationForm
from core.models import CustomUser
from .forms import (ContactForm, AboutMeForm, SocialMediaForm, AbilityForm, ServicesForm, PortfolioForm,
                    ExperiencesForm, EducationForm)
from .models import *


# class ProfileView(TemplateView):
#     template_name = 'main/main.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['custom_user'] = CustomUser.objects.get()
#         context['user'] = User.objects.get(user__is_superuser=True)
#         context['about_me'] = AboutMe.objects.first()
#         context['services'] = Services.objects.all()
#         context['portfolios'] = Portfolio.objects.all()
#         context['categories'] = Portfolio.CATEGORY_CHOICES
#         context['experiences'] = Experiences.objects.all()
#         context['educations'] = Education.objects.all()
#         context['abilities'] = Abilities.objects.all().order_by('-percent')
#         return context


def profile_view(request):
    superuser = get_object_or_404(CustomUser, username=settings.USERNAME_FOR_FILTER, is_superuser=True)
    about_me = AboutMe.objects.filter(user=superuser).first()
    abilities = Abilities.objects.filter(user=superuser)
    services = Services.objects.filter(user=superuser)
    portfolios = Portfolio.objects.filter(user=superuser)
    categories = Portfolio.CATEGORY_CHOICES
    experiences = Experiences.objects.filter(user=superuser)
    educations = Education.objects.filter(user=superuser)
    social_medias = SocialMedias.objects.filter(user=superuser)

    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})

    context = {'custom_user': superuser, 'about_me': about_me, 'abilities': abilities, 'services': services,
               'portfolios': portfolios, 'categories': categories, 'experiences': experiences, 'educations': educations,
               'social_medias': social_medias, 'contact_form': contact_form, }

    return render(request, 'main/main.html', context)


def superuser_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise Http404("Page not found")
        return view_func(request, *args, **kwargs)

    return _wrapped_view_func


def custom_404_view(request, exception):
    return render(request, 'management/404.html', status=404)


@superuser_required
def dashboard(request):
    models_dashboard = []
    models = [Abilities, AboutMe, Services, Portfolio, Experiences, Education, SocialMedias]
    for model_class in models:
        model_name = model_class.__name__
        model_instances = model_class.objects.all().order_by('-percent') if model_class == Abilities \
            else model_class.objects.all()
        if model_instances.exists():
            instances_data = []
            for instance in model_instances:
                if model_class == AboutMe:
                    display_value = instance.user.username
                elif model_class == SocialMedias:
                    display_value = instance.platform
                else:
                    first_field_name = model_class._meta.fields[2].name
                    display_value = getattr(instance, first_field_name)
                instances_data.append({
                    'id': instance.pk,
                    'title': display_value,
                    'edit_url': reverse(f'{model_name.lower()}-update', kwargs={'pk': instance.pk}),
                    'delete_url': reverse(f'{model_name.lower()}-delete', kwargs={'pk': instance.pk}),
                })
            models_dashboard.append({
                'name': model_name,
                'instances': instances_data,
                'add_url': reverse(f'{model_name.lower()}'),
            })
        else:
            models_dashboard.append({
                'name': model_name,
                'instances': None,
                'add_url': reverse(f'{model_name.lower()}'),
            })
    return render(request, 'main/admins.html', {'models': models_dashboard})


class SuperuserRequiredMixin(UserPassesTestMixin):
    request: HttpRequest

    def test_func(self):
        if not self.request.user.is_authenticated or not self.request.user.is_superuser:
            raise Http404("Page not found")
        return True


class AbilityCreateView(SuperuserRequiredMixin, generic.CreateView):
    model = Abilities
    form_class = AbilityForm
    template_name = 'forms/abilities.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AbilityUpdateView(SuperuserRequiredMixin, generic.UpdateView):
    model = Abilities
    form_class = AbilityForm
    template_name = 'forms/abilities-update.html'


class AbilityDeleteView(SuperuserRequiredMixin, generic.DeleteView):
    model = AbilityForm
    template_name = 'forms/abilities-delete.html'
    success_url = reverse_lazy('admin')


class AboutMeCreateView(SuperuserRequiredMixin, generic.CreateView):
    model = AboutMe
    form_class = AboutMeForm
    template_name = 'forms/aboutme.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AboutMeUpdateView(SuperuserRequiredMixin, generic.UpdateView):
    model = AboutMe
    form_class = AboutMeForm
    template_name = 'forms/aboutme-update.html'


class AboutMeDeleteView(SuperuserRequiredMixin, generic.DeleteView):
    model = AboutMe
    template_name = 'forms/aboutme-delete.html'
    success_url = reverse_lazy('admin')


class ServiceCreateView(SuperuserRequiredMixin, generic.CreateView):
    model = Services
    form_class = ServicesForm
    template_name = 'forms/service.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ServiceUpdateView(SuperuserRequiredMixin, generic.UpdateView):
    model = Services
    form_class = ServicesForm
    template_name = 'forms/service-update.html'


class ServiceDeleteView(SuperuserRequiredMixin, generic.DeleteView):
    model = Services
    template_name = 'forms/service-delete.html'
    success_url = reverse_lazy('admin')


class PortfolioCreateView(SuperuserRequiredMixin, generic.CreateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = 'forms/portfolio.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PortfolioUpdateView(SuperuserRequiredMixin, generic.UpdateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = 'forms/portfolio_update.html'


class PortfolioDeleteView(SuperuserRequiredMixin, generic.DeleteView):
    model = Portfolio
    template_name = 'forms/portfolio_delete.html'
    success_url = reverse_lazy('admin')


class ExperiencesCreateView(SuperuserRequiredMixin, generic.CreateView):
    model = Experiences
    form_class = ExperiencesForm
    template_name = 'forms/experiences.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExperiencesUpdateView(SuperuserRequiredMixin, generic.UpdateView):
    model = Experiences
    form_class = ExperiencesForm
    template_name = 'forms/experiences-update.html'


class ExperiencesDeleteView(SuperuserRequiredMixin, generic.DeleteView):
    model = Experiences
    template_name = 'forms/experiences-delete.html'
    success_url = reverse_lazy('admin')


class EducationCreateView(SuperuserRequiredMixin, generic.CreateView):
    model = Education
    form_class = EducationForm
    template_name = 'forms/education.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EducationUpdateView(SuperuserRequiredMixin, generic.UpdateView):
    model = Education
    form_class = EducationForm
    template_name = 'forms/education-update.html'


class EducationDeleteView(SuperuserRequiredMixin, generic.DeleteView):
    model = Education
    template_name = 'forms/education-delete.html'
    success_url = reverse_lazy('admin')


class SocialMediasCreateView(SuperuserRequiredMixin, generic.CreateView):
    model = SocialMedias
    form_class = SocialMediaForm
    template_name = 'forms/social-medias.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SocialMediasUpdateView(SuperuserRequiredMixin, generic.UpdateView):
    model = SocialMedias
    form_class = SocialMediaForm
    template_name = 'forms/social-medias-update.html'


class SocialMediasDeleteView(SuperuserRequiredMixin, generic.DeleteView):
    model = SocialMedias
    template_name = 'forms/social-medias-delete.html'
    success_url = reverse_lazy('admin')


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
