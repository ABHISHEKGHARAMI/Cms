# Generated by Django 5.1 on 2024-09-16 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_video_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='content',
            field=models.ImageField(upload_to='images'),
        ),
    ]
