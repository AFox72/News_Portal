from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.conf import settings
from .models import *
from .tasks import send_notifications

@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.post_name, subscribers)



# @receiver(m2m_changed, sender=Post.category.through)
# def notify_subscribers(instance, action, *args, **kwargs):
#     if action == 'post_add':
#         users_emails = [
#                 user.email
#                 for category in instance.category.all()
#                 for user in category.subscribers.all()
#             ]
#         for email in users_emails:
#             user = User.objects.get(email=email)
#             html_content = render_to_string('post_created_email.html', {'post_mail': instance}, )
#
#             subject=f'"Здравствуй, {user.username}. Новая статья в твоём любимом разделе(celery)!"'\
#                     f'{instance.post_name}'
#             from_email = 'settings.DEFAULT_FROM_EMAI'
#             send_notifications.delay(subject, from_email, email, html_content)
#
