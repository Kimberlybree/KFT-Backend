# Generated by Django 3.2.7 on 2021-09-24 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='keepfit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('goal_description', models.TextField()),
                ('goal_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
