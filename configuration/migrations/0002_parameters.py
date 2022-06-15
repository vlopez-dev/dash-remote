# Generated by Django 4.0.4 on 2022-06-15 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_check', models.IntegerField(choices=[(10, '10min'), (20, '20min'), (30, '30min')])),
            ],
        ),
    ]
