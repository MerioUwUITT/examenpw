# Generated by Django 2.2.3 on 2022-09-19 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player_register', '0006_auto_20220919_0908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stadium', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='matches_drawn',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='matches_lost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='matches_played',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='matches_won',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='stadium',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='player_register.Stadium'),
        ),
    ]
