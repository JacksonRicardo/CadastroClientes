# Generated by Django 2.2.7 on 2019-11-25 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('apelido', models.CharField(max_length=255, verbose_name='Apelido')),
                ('snap', models.CharField(max_length=255, verbose_name='Snap')),
                ('cpf', models.CharField(max_length=255, verbose_name='CPF')),
            ],
        ),
    ]
