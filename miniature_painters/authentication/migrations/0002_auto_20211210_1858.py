# Generated by Django 3.2.8 on 2021-12-10 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='middle_name',
        ),
        migrations.AddField(
            model_name='user',
            name='years_experience',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
