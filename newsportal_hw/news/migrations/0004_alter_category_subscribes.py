# Generated by Django 4.2.13 on 2024-07-16 13:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_category_subscribes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subscribes',
            field=models.ManyToManyField(blank=True, null=True, related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
    ]