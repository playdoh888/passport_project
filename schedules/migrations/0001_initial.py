# Generated by Django 3.0.6 on 2020-06-16 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=16)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('time', models.TimeField()),
                ('hours', models.DecimalField(decimal_places=2, max_digits=4)),
                ('instructor', models.CharField(max_length=64)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]