# Generated by Django 4.2.4 on 2023-08-05 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_customuser_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='GSTINID',
        ),
    ]
