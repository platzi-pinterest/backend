# Generated by Django 3.0.10 on 2020-09-30 02:36

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('status', models.CharField(choices=[('active', 'Active element'), ('inactive', 'Inactive element')], default='active', help_text='Status of the object base.', max_length=32, verbose_name='status')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('deleted', models.DateTimeField(auto_now=True, help_text='Date time on which the object was delete.', verbose_name='deleted at')),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True, verbose_name='email address')),
                ('age', models.IntegerField(default=15, help_text='Age of the user 10 > x > 100.', verbose_name='Age of the user')),
                ('is_client', models.BooleanField(default=True, help_text='Help easily distinguish users and perform queries. Clients are the main type of user.', verbose_name='client')),
                ('is_verified', models.BooleanField(default=False, help_text='Set to true when the user have verified its email address.', verbose_name='verified')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Name of User')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Lastnme of User')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-status', '-created', '-modified', '-deleted'],
                'get_latest_by': 'created',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'Active element'), ('inactive', 'Inactive element')], default='active', help_text='Status of the object base.', max_length=32, verbose_name='status')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('deleted', models.DateTimeField(auto_now=True, help_text='Date time on which the object was delete.', verbose_name='deleted at')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='users/pictures/', verbose_name='profile picture')),
                ('biography', models.TextField(blank=True, max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-status', '-created', '-modified', '-deleted'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
