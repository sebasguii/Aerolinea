# Generated by Django 4.1 on 2025-06-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nserie', models.IntegerField()),
                ('compañia', models.CharField(max_length=50)),
                ('modelo', models.IntegerField()),
                ('caracteristicasT', models.CharField(max_length=50)),
                ('capacidad', models.IntegerField()),
                ('antiguedad', models.IntegerField()),
                ('nhorasvuelo', models.IntegerField()),
            ],
        ),
    ]
