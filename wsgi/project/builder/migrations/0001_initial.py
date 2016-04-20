# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-19 00:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('order', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('href', models.URLField(max_length=500)),
                ('title', models.CharField(max_length=150)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.Block')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.URLField(max_length=500)),
                ('alt', models.CharField(max_length=150)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.Block')),
            ],
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.Block')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=150)),
                ('order', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(max_length=500)),
                ('title', models.CharField(max_length=150)),
                ('button_title', models.CharField(max_length=150)),
                ('button_url', models.URLField(max_length=500)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.Block')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.Block')),
            ],
        ),
        migrations.AddField(
            model_name='block',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.Section'),
        ),
    ]
