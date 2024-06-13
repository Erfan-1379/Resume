from django.urls import path

from .views import *

urlpatterns = [
    path('home/', ProfileView.as_view(), name='home'),
    path('admin/', dashboard, name='admin'),
    path('portfolio/', PortfolioCreateView.as_view(), name='portfolio'),
    path('portfolio/edit/<int:pk>', PortfolioUpdateView.as_view(), name='portfolio-update'),
    path('portfolio/delete/<int:pk>', PortfolioDeleteView.as_view(), name='portfolio-delete'),
    path('abilities/', AbilityCreateView.as_view(), name='abilities'),
    path('abilities/edit/<int:pk>', AbilityUpdateView.as_view(), name='abilities-update'),
    path('abilities/delete/<int:pk>', AbilityDeleteView.as_view(), name='abilities-delete'),
    path('aboutme/', AboutMeCreateView.as_view(), name='aboutme'),
    path('aboutme/edit/<int:pk>', AboutMeUpdateView.as_view(), name='aboutme-update'),
    path('aboutme/delete/<int:pk>', AboutMeDeleteView.as_view(), name='aboutme-delete'),
    path('education/', EducationCreateView.as_view(), name='education'),
    path('education/edit/<int:pk>', EducationUpdateView.as_view(), name='education-update'),
    path('education/delete/<int:pk>', EducationDeleteView.as_view(), name='education-delete'),
    path('services/', ServiceCreateView.as_view(), name='services'),
    path('services/edit/<int:pk>', ServiceUpdateView.as_view(), name='services-update'),
    path('services/delete/<int:pk>', ServiceDeleteView.as_view(), name='services-delete'),
    path('experiences/', ExperiencesCreateView.as_view(), name='experiences'),
    path('experiences/edit/<int:pk>', ExperiencesUpdateView.as_view(), name='experiences-update'),
    path('experiences/delete/<int:pk>', ExperiencesDeleteView.as_view(), name='experiences-delete'),
]
