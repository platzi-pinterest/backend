# Generated by Django 3.0.10 on 2020-10-01 01:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('status', models.CharField(choices=[('active', 'Active element'), ('inactive', 'Inactive element')], default='active', help_text='Status of the object base.', max_length=32, verbose_name='status')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('deleted', models.DateTimeField(auto_now=True, help_text='Date time on which the object was delete.', verbose_name='deleted at')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='name of board')),
                ('date', models.DateTimeField(blank=True, max_length=250, null=True, verbose_name='date to keep the board')),
                ('secret', models.BooleanField(default=False, verbose_name='the board is secret?')),
            ],
            options={
                'ordering': ['-status', '-created', '-modified', '-deleted'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
