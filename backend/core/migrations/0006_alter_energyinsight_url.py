# Generated by Django 5.0.7 on 2024-07-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_energyinsight_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energyinsight',
            name='url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
