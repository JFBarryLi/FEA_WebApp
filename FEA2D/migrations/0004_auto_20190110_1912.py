# Generated by Django 2.1.5 on 2019-01-11 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FEA2D', '0003_inputstructure_force_vector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputstructure',
            name='inner_diameter',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inputstructure',
            name='modulus_elasticity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inputstructure',
            name='outer_diameter',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inputstructure',
            name='yield_strength',
            field=models.FloatField(),
        ),
    ]
