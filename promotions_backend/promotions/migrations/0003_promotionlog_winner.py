# Generated by Django 3.1.1 on 2020-09-20 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0002_promotionlog_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotionlog',
            name='winner',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
