# Generated by Django 3.1 on 2020-08-11 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='added_date',
            field=models.DateTimeField(),
        ),
    ]