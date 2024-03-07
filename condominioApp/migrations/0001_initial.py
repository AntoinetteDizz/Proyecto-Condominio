# Generated by Django 4.2.2 on 2024-03-07 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condominio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('year_construction', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Condominios',
            },
        ),
        migrations.CreateModel(
            name='RoleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'RoleType',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=40)),
                ('acess', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominioApp.roletype')),
            ],
            options={
                'db_table': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_pago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.TextField(blank=True)),
                ('condominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominioApp.condominio')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominioApp.users')),
            ],
            options={
                'db_table': 'Mantenimiento',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('age', models.PositiveBigIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('charge', models.CharField(max_length=100)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('condominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominioApp.condominio')),
            ],
            options={
                'db_table': 'Empleados',
            },
        ),
        migrations.CreateModel(
            name='Edificios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloque', models.CharField(max_length=50, unique=True)),
                ('year_construction', models.CharField(max_length=30)),
                ('condominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominioApp.condominio')),
            ],
            options={
                'db_table': 'Edificios',
            },
        ),
        migrations.CreateModel(
            name='Directivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=40)),
                ('acess', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominioApp.roletype')),
            ],
            options={
                'db_table': 'Directivos',
            },
        ),
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_dpto', models.PositiveBigIntegerField()),
                ('telefono_casa', models.CharField(max_length=20)),
                ('status', models.BooleanField(default=False)),
                ('edificios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominioApp.edificios')),
            ],
            options={
                'db_table': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Departamento_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateField()),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominioApp.departamentos')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominioApp.users')),
            ],
            options={
                'db_table': 'Departamento_user',
            },
        ),
    ]
