# Generated by Django 2.2.3 on 2022-09-19 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player_register', '0003_auto_20220919_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='player',
            field=models.ManyToManyField(to='player_register.Player'),
        ),
        migrations.DeleteModel(
            name='PlayerTeam',
        ),
    ]
