# Generated by Django 3.2.13 on 2022-05-26 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_article_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default=None, upload_to='articles/'),
        ),
    ]