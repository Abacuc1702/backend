# Generated by Django 5.0.1 on 2024-08-03 01:24

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0014_remove_user_first_name_remove_user_last_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategorieProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=50, verbose_name='Intitulé de la catégorie de produit')),
            ],
        ),
        migrations.CreateModel(
            name='TypeProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=50, verbose_name='Intitulé du type de produit')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('administrateur', 'Administrateur'), ('gerant', 'Gérant'), ('client', 'Client')], max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('email_verified', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='customuser_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='customuser_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_commande', models.DateField(verbose_name='date de commande')),
                ('cout_total', models.IntegerField(help_text='Coût de la commande', verbose_name='cout total de la commande')),
                ('statut', models.CharField(max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL, verbose_name='Client de la commande')),
                ('gerant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gerant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, verbose_name='Nom du produit')),
                ('quantite', models.IntegerField(verbose_name='Quantité en stock')),
                ('cout_unitaire', models.IntegerField(verbose_name='Prix unitaire de vente du produit')),
                ('description', models.TextField(verbose_name='Description du produit')),
                ('categorie_produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categorieproduit')),
                ('type_produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.typeproduit')),
            ],
        ),
        migrations.CreateModel(
            name='ProduitCommande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField()),
                ('cout_total', models.IntegerField()),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.commande')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Reapprovisionnement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reapprovisionnement', models.DateField(verbose_name='Date de réapprovisionnement')),
                ('fournisseur', models.CharField(max_length=50, verbose_name='Nom du fournisseur')),
                ('prix_unitaire', models.IntegerField(verbose_name='Prix unitaire du produit')),
                ('quantite', models.IntegerField(verbose_name='Quantité reçue')),
                ('prix_total', models.IntegerField()),
                ('gerant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Gerant')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.produit')),
            ],
        ),
    ]
