# Generated by Django 4.0.3 on 2022-03-12 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_account_alias_account_type_deposit_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snapshot',
            name='amount',
            field=models.IntegerField(),
        ),
    ]