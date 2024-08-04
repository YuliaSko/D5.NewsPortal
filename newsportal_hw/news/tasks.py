import datetime

from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from newsportal import settings
from .models import Post, Category


@shared_task
def send_email_new_post(pk):
    post = Post.objects.get(pk=pk)
    categories = post.categories.all()
    title = post.title
    subscribers_emails = []

    for cat in categories:
        subscribers = cat.subscribes.all()

        for s in subscribers:
            subscribers_emails += s.email

    html_content = render_to_string(
            'new_post_email.html',
            {
                'Text': f'{post.title}',
                'link': f'{settings.SITE_URL}/news/{pk}',
            }
        )

    msg = EmailMultiAlternatives(
            subject=title,
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=subscribers_emails
        )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def send_email_weekly():
    today = datetime.datetime.now()
    week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(date_post__gte=week)
    categories = set(posts.values_list('categories__category', flat=True))
    subscribers = set(Category.objects.filter(category__in=categories).values_list('subscribes__email', flat=True))

    html_content = render_to_string(
        'weekly_email.html',
        {
            'link': settings.SITE_URL,
            'posts': posts
        }
    )

    msg = EmailMultiAlternatives(
        subject='Еженедельная рассылка новостей',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

