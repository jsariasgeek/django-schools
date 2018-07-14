# Generated by Django 2.0.1 on 2018-01-18 18:07

from django.db import migrations


def create_subjects(apps, schema_editor):
    Subject = apps.get_model('quizzes', 'Subject')
    Subject.objects.create(name='Arts', color='#343a40')
    Subject.objects.create(name='Computing', color='#007bff')
    Subject.objects.create(name='Math', color='#28a745')
    Subject.objects.create(name='Biology', color='#17a2b8')
    Subject.objects.create(name='History', color='#ffc107')

def create_schools(apps, schema_editor):
    School = apps.get_model('schools', 'School')
    School.objects.create(name='ASMMHSS')
    School.objects.create(name='Mary Matha')
    School.objects.create(name='PKHS')
    School.objects.create(name='NES')

class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_subjects),
        migrations.RunPython(create_schools),
    ]
