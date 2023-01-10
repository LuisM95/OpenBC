# Generated by Django 4.1.5 on 2023-01-10 10:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Write a Genre', max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for film', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('data_release', models.DateField(blank=True, help_text='Release Date', null=True)),
                ('synopsis', models.TextField(help_text='Synopsis of film', max_length=500)),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cine.director')),
                ('genre', models.ManyToManyField(to='cine.genre')),
            ],
        ),
    ]