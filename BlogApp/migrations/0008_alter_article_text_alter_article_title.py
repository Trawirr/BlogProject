# Generated by Django 5.0.6 on 2024-05-28 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0007_alter_article_options_alter_author_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='Tytuł nowego posta', max_length=50),
        ),
    ]
