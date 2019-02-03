# Generated by Django 2.0.1 on 2019-02-03 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('population', models.BigIntegerField()),
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('destination', models.ForeignKey(blank=True, help_text='desitnation tour to destination table', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destination_goal', to='web.City', verbose_name='destination')),
            ],
            options={
                'verbose_name': 'tour',
                'verbose_name_plural': 'tours',
            },
        ),
    ]