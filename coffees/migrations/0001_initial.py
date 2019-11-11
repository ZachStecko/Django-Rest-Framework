# Generated by Django 2.2.5 on 2019-09-15 02:03

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
            name='Coffees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of beverage', max_length=24)),
                ('temperature', models.CharField(choices=[('H', 'Hot'), ('C', 'Cold'), ('T', 'Tepid')], help_text='The degree or intensity of heat present in the coffee', max_length=1)),
                ('description', models.TextField(help_text='Appealing description of beverage')),
                ('price', models.DecimalField(decimal_places=2, help_text='The amount of money expected for the coffee', max_digits=4)),
                ('user', models.ForeignKey(help_text='The person who needs coffee', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Coffee',
                'verbose_name_plural': 'Coffees',
            },
        ),
    ]