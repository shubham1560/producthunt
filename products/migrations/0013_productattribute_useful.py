# Generated by Django 2.2.2 on 2019-09-17 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_productfeedback_parcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='productattribute',
            name='useful',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]