# Generated by Django 5.0 on 2023-12-24 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verif_code',
            field=models.CharField(default='698444837708', max_length=15, verbose_name='Проверочный код'),
        ),
    ]