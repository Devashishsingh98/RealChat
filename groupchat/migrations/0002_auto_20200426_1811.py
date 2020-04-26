# Generated by Django 3.0.5 on 2020-04-26 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groupchat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=20)),
                ('messages', models.CharField(blank=True, max_length=1000000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('room', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='groupchat.Room')),
            ],
        ),
        migrations.DeleteModel(
            name='Rooms',
        ),
    ]
