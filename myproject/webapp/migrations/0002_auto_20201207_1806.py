# Generated by Django 3.1.4 on 2020-12-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='postal_address',
            field=models.TextField(default='to be defined'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employees',
            name='user_email',
            field=models.EmailField(blank=True, max_length=70, unique=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='firstname',
            field=models.CharField(max_length=50),
        ),
    ]