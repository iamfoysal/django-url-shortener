# Generated by Django 5.0 on 2023-12-17 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorter', '0002_url_created_at_url_last_click_url_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
