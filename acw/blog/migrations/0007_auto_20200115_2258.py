# Generated by Django 3.0.2 on 2020-01-15 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='articlehitcount',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
