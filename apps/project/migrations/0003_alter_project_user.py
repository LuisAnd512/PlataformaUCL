# Generated by Django 4.1.13 on 2024-02-07 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.user'),
        ),
    ]
