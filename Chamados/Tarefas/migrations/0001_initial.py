# Generated by Django 3.2.9 on 2021-11-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('setor', models.CharField(choices=[('manutencao', 'Manutenção'), ('ti', 'TI'), ('marketing', 'Marketing'), ('logistica', 'Logistica')], max_length=10)),
                ('situacao', models.CharField(choices=[('doing', 'Pendente'), ('done', 'Feito')], max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
