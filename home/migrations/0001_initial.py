# Generated by Django 3.2.8 on 2021-10-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=50)),
                ('mostrar', models.BooleanField(default=True)),
                ('foto', models.ImageField(blank=True, upload_to='fotos/%y/%m/%d/')),
            ],
        ),
    ]
