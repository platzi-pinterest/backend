# Generated by Django 3.0.10 on 2020-10-01 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_board_user'),
        ('pin', '0002_pin_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='board.Board'),
        ),
    ]
