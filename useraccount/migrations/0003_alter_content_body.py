# Generated by Django 5.0.2 on 2024-02-21 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0002_content_created_at_content_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='body',
            field=models.TextField(max_length=300),
        ),
    ]
