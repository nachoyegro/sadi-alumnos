# Generated by Django 2.0.8 on 2019-09-12 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20190905_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materiacursada',
            name='nota',
            field=models.CharField(choices=[('C', 'Cursando'), ('EQ', 'Equivalencia'), ('AP', 'Aprobado'), ('D', 'Desaprobado'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='C', max_length=3, null=True),
        ),
    ]
