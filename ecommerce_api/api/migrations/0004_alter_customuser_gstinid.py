# Generated by Django 4.2.4 on 2023-08-05 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_customuser_gstinid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='GSTINID',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
