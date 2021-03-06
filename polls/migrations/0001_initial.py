# Generated by Django 3.1 on 2020-08-28 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=150)),
                ('agreement_template', models.TextField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.userss')),
            ],
        ),
    ]
