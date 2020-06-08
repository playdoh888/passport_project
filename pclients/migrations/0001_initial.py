# Generated by Django 3.0.6 on 2020-05-28 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Paddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('ext_address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=30)),
                ('zipcode', models.CharField(max_length=5)),
                ('country', models.CharField(default='US', max_length=50)),
            ],
            options={
                'verbose_name': 'Paddress',
                'verbose_name_plural': 'Paddress',
            },
        ),
        migrations.CreateModel(
            name='Pclient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(unique=True)),
                ('name', models.CharField(max_length=80)),
                ('desc', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=32)),
                ('salutation', models.CharField(max_length=8)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pclients.Paddress')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'pclient',
            },
        ),
    ]