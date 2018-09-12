# Generated by Django 2.1 on 2018-09-12 14:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('price', models.IntegerField(default=0)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('seller', models.CharField(max_length=10)),
            ],
        ),
    ]
