# Generated by Django 2.0.5 on 2018-05-27 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporter', models.CharField(max_length=50)),
                ('assignee', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=400)),
                ('state', models.CharField(choices=[('CN', 'Concept'), ('OP', 'Open'), ('IP', 'In Progress'), ('RD', 'Resolved'), ('CL', 'Closed')], default='CN', max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Category')),
            ],
        ),
    ]
