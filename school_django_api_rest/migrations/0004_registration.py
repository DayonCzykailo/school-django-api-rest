# Generated by Django 5.1.3 on 2024-11-19 16:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_django_api_rest', '0003_rename_estudent_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon'), ('N', 'Night'), ('D', 'Dawn')], default='M', max_length=1)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_django_api_rest.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_django_api_rest.student')),
            ],
        ),
    ]
