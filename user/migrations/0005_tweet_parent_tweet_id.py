# Generated by Django 3.1.1 on 2020-10-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20201025_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='parent_tweet_id',
            field=models.IntegerField(null=True),
        ),
    ]
