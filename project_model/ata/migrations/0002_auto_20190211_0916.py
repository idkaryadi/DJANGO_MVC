# Generated by Django 2.1.5 on 2019-02-11 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direksi',
            name='no_telepon',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='mentee',
            name='nilai_rata_rata',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='mentee',
            name='no_absen',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='mentee',
            name='no_telepon',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='no_telepon',
            field=models.CharField(max_length=25),
        ),
    ]