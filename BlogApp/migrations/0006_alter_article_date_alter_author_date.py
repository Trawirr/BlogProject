# Generated by Django 5.0.6 on 2024-05-28 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0005_alter_article_date_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
