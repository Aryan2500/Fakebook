# Generated by Django 3.1.2 on 2020-11-23 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailOrPhone', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
