# Generated by Django 3.1.1 on 2020-10-25 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_tweet_parent_tweet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='parent_tweet_id',
            field=models.IntegerField(blank=True),
        ),
    ]
