# Generated by Django 4.0.4 on 2022-04-28 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='state',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
