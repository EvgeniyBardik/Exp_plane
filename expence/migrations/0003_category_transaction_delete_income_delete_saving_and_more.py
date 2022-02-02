# Generated by Django 4.0.1 on 2022-01-28 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expence', '0002_alter_income_date_alter_saving_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Имя типа')),
                ('amount', models.FloatField(blank=True, null=True, verbose_name='Сумма')),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='expence.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Транзакция',
                'verbose_name_plural': 'Транзакции',
                'ordering': ['-date'],
            },
        ),
        migrations.DeleteModel(
            name='Income',
        ),
        migrations.DeleteModel(
            name='Saving',
        ),
        migrations.DeleteModel(
            name='Spending',
        ),
    ]