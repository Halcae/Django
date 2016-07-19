# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 01:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('pontos_curso', models.IntegerField(default=0)),
                ('experiencia_curso', models.IntegerField(default=0)),
                ('dificuldade', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Curso_Medalha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Medalha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('icone', models.FileField(blank=True, null=True, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('nivel', models.IntegerField(default=1)),
                ('pontos', models.IntegerField(default=0)),
                ('experiencia', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_conclusao', models.DateTimeField(verbose_name=b'Data de Conclusao')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Curso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Medalha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medalha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Medalha')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='curso_medalha',
            name='medalha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Medalha'),
        ),
    ]
