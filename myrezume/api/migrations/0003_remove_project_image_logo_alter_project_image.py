# Generated by Django 5.1.5 on 2025-02-07 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_project_image_logo_project_tehnology_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image_logo',
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='products/default_image.jpg', upload_to='products/'),
        ),
    ]
