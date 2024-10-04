# Generated by Django 5.1.1 on 2024-10-03 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('five', '0002_rename_yourmodel_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
