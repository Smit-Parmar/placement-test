# Generated by Django 3.2.8 on 2021-10-13 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_alter_student_college'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='college_name',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='college',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='student.college'),
        ),
    ]
