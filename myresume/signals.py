from decouple import config
from django.core.mail import send_mail
from django.db.models.signals import pre_delete, pre_save, post_save
from django.dispatch import receiver
import os

from myresume.models import Portfolio, AboutMe, Contact


def delete_file(path):
    if path and os.path.isfile(path):
        os.remove(path)


@receiver(pre_delete, sender=AboutMe)
@receiver(pre_delete, sender=Portfolio)
def delete_instance_files(sender, instance, **kwargs):
    if sender == AboutMe:
        delete_file(instance.file_resume.path if instance.file_resume else None)
        delete_file(instance.profile_photo.path if instance.profile_photo else None)
    elif sender == Portfolio:
        delete_file(instance.image_project.path if instance.image_project else None)


@receiver(pre_save, sender=AboutMe)
@receiver(pre_save, sender=Portfolio)
def update_instance_files(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
        except sender.DoesNotExist:
            return

        if sender == AboutMe:
            if old_instance.file_resume and instance.file_resume != old_instance.file_resume:
                delete_file(old_instance.file_resume.path)
            if old_instance.profile_photo and instance.profile_photo != old_instance.profile_photo:
                delete_file(old_instance.profile_photo.path)
        elif sender == Portfolio:
            if old_instance.image_project and instance.image_project != old_instance.image_project:
                delete_file(old_instance.image_project.path)


@receiver(post_save, sender=Contact)
def send_contact_email(sender, instance, **kwargs):
    message = f'Name: {instance.name}\nEmail: {instance.email}\nPhone: {instance.phone} \n\n{instance.message}'
    send_mail(
        f'New contact message from {instance.name}',
        message,
        instance.email,
        [config('EMAIL_RECIPIENT_LIST')],
    )