# Generated by Django 3.2 on 2021-08-12 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('in process', 'in process'), ('delivered', 'delivered')], max_length=200, null=True),
        ),
    ]