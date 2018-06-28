# Generated by Django 2.0.6 on 2018-06-14 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productline',
            options={'ordering': ['name'], 'verbose_name': 'product Line'},
        ),
        migrations.AlterField(
            model_name='maintenanceitem',
            name='fund_source',
            field=models.IntegerField(blank=True, help_text='Funding Source'),
        ),
        migrations.AlterField(
            model_name='maintenanceitem',
            name='maintenanceRequirementList',
            field=models.ManyToManyField(blank=True, help_text='Applicable Maintenance Requirement List', to='apm.maintenanceRequirementList', verbose_name='Maintenance Requirement List'),
        ),
        migrations.AlterField(
            model_name='maintenanceitem',
            name='periodicity',
            field=models.IntegerField(blank=True, help_text='Time Inteval for Maintenance Item Period'),
        ),
        migrations.AlterField(
            model_name='maintenanceitem',
            name='shipInstance',
            field=models.ManyToManyField(help_text='Applicable Ship', to='apm.shipInstance', verbose_name='ship Instance'),
        ),
        migrations.AlterField(
            model_name='supplypart',
            name='maintenanceItem',
            field=models.ManyToManyField(blank=True, help_text='Applicable Maintenance Item', to='apm.maintenanceItem', verbose_name='maintenance Item'),
        ),
    ]