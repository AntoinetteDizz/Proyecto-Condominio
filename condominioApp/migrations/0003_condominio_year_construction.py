# Generated by Django 5.0.2 on 2024-03-02 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominioApp', '0002_remove_condominio_year_of_construction'),
    ]

    operations = [
        migrations.AddField(
            model_name='condominio',
            name='year_construction',
            field=models.CharField(default=200, max_length=30),
            preserve_default=False,
        ),
    ]