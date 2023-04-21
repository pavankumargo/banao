# Generated by Django 4.0.3 on 2023-04-21 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('user_type', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('line', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('profile', models.ImageField(blank=True, default='profile.png', null=True, upload_to='media')),
            ],
        ),
    ]