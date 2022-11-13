from celery import shared_task


from .models import Post, Category
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
import datetime
from django.conf import settings


@shared_task
def send_notifications(preview, pk, post_name, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=post_name,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def week_notification():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(publication_date__gte=last_week)
    categories = set(posts.values_list('category__category', flat=True))
    subscribers = set(Category.objects.filter(category__in=categories).values_list('subscribers__email', flat=True))
    html_content = render_to_string(
        'account/email/weekly_posts.html',
        {
            'link': settings.SITE_URL,
            'posts': posts
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

