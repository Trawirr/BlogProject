# Generated by Django 5.0.6 on 2024-05-28 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0006_alter_article_date_alter_author_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posty'},
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Autor', 'verbose_name_plural': 'Autorzy'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': 'Tag', 'verbose_name_plural': 'Tagi'},
        ),
        migrations.AlterModelOptions(
            name='variable',
            options={'verbose_name': 'Zmienna', 'verbose_name_plural': 'Zmienne'},
        ),
        migrations.AddField(
            model_name='author',
            name='role',
            field=models.CharField(choices=[('normal', 'Normal'), ('admin', 'Admin')], default='normal', max_length=10),
        ),
    ]
