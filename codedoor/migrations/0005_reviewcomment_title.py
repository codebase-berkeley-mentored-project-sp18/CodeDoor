# Generated by Django 2.0.1 on 2018-04-17 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codedoor', '0004_applicationcomment_reviewcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewcomment',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
