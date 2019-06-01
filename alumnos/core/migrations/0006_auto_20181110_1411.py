# Generated by Django 2.0.8 on 2018-11-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_persona_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='codigo',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='materia',
            name='siglas',
            field=models.CharField(max_length=32, null=True),
        ),
    ]