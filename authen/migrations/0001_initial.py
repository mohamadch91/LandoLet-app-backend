# Generated by Django 4.0.6 on 2022-07-24 20:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.CharField(choices=[('Tenant', 'Tenant'), ('Landlord', 'Lanlord'), ('Agency', 'Agency')], db_column='RoleName', max_length=10, null=True)),
                ('first_name', models.TextField(blank=True, db_column='FirstName', null=True)),
                ('last_name', models.TextField(blank=True, db_column='LastName', null=True)),
                ('email', models.EmailField(blank=True, db_column='Email', max_length=254, null=True, unique=True)),
                ('postal_code', models.IntegerField(blank=True, db_column='PostalCode', null=True)),
                ('full_address', models.TextField(blank=True, db_column='FullAddress', null=True)),
                ('phone_no', models.IntegerField(blank=True, db_column='PhoneNo', null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
