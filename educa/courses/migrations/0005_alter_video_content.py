# Generated by Django 5.1 on 2024-09-05 05:32

import embed_video.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='content',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
