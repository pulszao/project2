# Generated by Django 3.0.8 on 2020-10-04 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20201002_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bids',
            name='listing_id',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='listing_id',
        ),
        migrations.AddField(
            model_name='bids',
            name='listing_title',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='listing_title',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
    ]
