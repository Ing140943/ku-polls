# Generated by Django 3.2.6 on 2021-09-12 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_vote_choice_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(default=None, null=True, verbose_name='end dated'),
        ),
    ]
