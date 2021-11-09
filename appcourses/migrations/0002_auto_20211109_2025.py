# Generated by Django 3.2.8 on 2021-11-09 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcourses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['name'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AddField(
            model_name='course',
            name='about',
            field=models.TextField(blank=True, verbose_name='Sobre o curso'),
        ),
        migrations.AlterField(
            model_name='course',
            name='descricao',
            field=models.TextField(blank=True, verbose_name='Descricao Simples'),
        ),
    ]
