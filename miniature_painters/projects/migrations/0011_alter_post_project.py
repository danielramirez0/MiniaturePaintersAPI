# Generated by Django 3.2.8 on 2021-12-14 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20211214_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
    ]
