# Generated by Django 3.0.6 on 2020-05-28 13:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pclients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pclient',
            name='id',
        ),
        migrations.AlterField(
            model_name='pclient',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
