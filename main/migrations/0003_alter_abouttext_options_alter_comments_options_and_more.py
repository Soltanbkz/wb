# Generated by Django 4.2.1 on 2023-05-11 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_abouttext_date_created_comments_date_created_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abouttext',
            options={'verbose_name': 'О нас', 'verbose_name_plural': 'О нас'},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='generalpage',
            options={'verbose_name': 'Главная', 'verbose_name_plural': 'Главная'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name': 'Портфолио', 'verbose_name_plural': 'Портфолио'},
        ),
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.CharField(max_length=300),
        ),
    ]
