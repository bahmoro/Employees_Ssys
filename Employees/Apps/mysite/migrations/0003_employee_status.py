# Generated by Django 2.1.2 on 2018-10-13 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_employee_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.BooleanField(default=False, verbose_name='finalizado'),
        ),
    ]