# Generated by Django 5.0.1 on 2024-08-14 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_categorieproduit_intitule_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='gerant',
        ),
    ]
