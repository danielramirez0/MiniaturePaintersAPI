# Generated by Django 3.2.8 on 2021-12-14 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20211213_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='posted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
