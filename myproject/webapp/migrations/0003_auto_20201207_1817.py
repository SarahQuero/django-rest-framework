# Generated by Django 3.1.4 on 2020-12-07 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20201207_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='emp_id',
        ),
        migrations.AddField(
            model_name='employees',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='firstname',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='employees',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employees',
            name='lastname',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='employees',
            name='postal_address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='employees',
            name='user_email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
