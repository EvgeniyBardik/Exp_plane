# Generated by Django 4.0.1 on 2022-01-27 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expence', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='saving',
            name='date',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='spending',
            name='date',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
