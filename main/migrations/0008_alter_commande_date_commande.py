# Generated by Django 5.0.1 on 2024-08-15 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_commande_date_commande'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='date_commande',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date de commande'),
        ),
    ]
