# Generated by Django 3.1.4 on 2020-12-21 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('idade', models.IntegerField(max_length=3)),
                ('endereco', models.CharField(max_length=255)),
                ('cpf', models.IntegerField(max_length=11)),
            ],
        ),
    ]