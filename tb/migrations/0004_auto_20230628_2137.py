# Generated by Django 3.0.5 on 2023-06-28 14:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tb', '0003_auto_20230628_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='kdsoal',
            name='id_kelas',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='jawaban',
            name='tgl_ujian',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterModelTable(
            name='jawaban',
            table=None,
        ),
    ]