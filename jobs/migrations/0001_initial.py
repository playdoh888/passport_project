# Generated by Django 3.0.6 on 2020-08-12 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=64)),
                ('contactName', models.CharField(max_length=64)),
                ('contactEmail', models.EmailField(max_length=254)),
                ('companyAddress', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'jobs_client',
                'verbose_name_plural': 'jobs_clients',
                'permissions': (('can_edit_postings', 'Edit Postings'),),
            },
        ),
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
                ('deadline', models.DateField()),
                ('postedDate', models.DateField()),
                ('position', models.CharField(max_length=64)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='jobs.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('posting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posting', to='jobs.Posting')),
            ],
        ),
    ]
