# Generated by Django 5.1.1 on 2024-10-01 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
