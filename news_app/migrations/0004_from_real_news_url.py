# Generated by Django 5.0.1 on 2024-01-12 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0003_from_real_news_remove_news_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='from_real_news',
            name='url',
            field=models.URLField(default='default'),
        ),
    ]
