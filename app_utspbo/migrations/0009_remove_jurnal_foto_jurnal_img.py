# Generated by Django 4.1.2 on 2022-11-01 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_utspbo', '0008_jurnal_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jurnal',
            name='foto',
        ),
        migrations.AddField(
            model_name='jurnal',
            name='img',
            field=models.CharField(max_length=40, null=True),
        ),
    ]