# Generated by Django 3.0.8 on 2020-12-17 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_closed'),
    ]

    operations = [
        migrations.AddField(
            model_name='closed',
            name='category',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='closed',
            name='description',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='closed',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='closed',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='closed',
            name='winning_bid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]