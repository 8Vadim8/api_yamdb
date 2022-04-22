# Generated by Django 2.2.16 on 2022-04-22 07:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220422_0528'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий к отзыву', 'verbose_name_plural': 'Комментарии к отзыву'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Отзыв о произведении', 'verbose_name_plural': 'Отзывы о произведении'},
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Минимальная оценка - 1'), django.core.validators.MaxValueValidator(10, message='Максимальная оценка - 10')]),
        ),
    ]