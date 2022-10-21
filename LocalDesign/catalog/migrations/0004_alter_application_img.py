# Generated by Django 4.1.2 on 2022-10-21 12:07

import catalog.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_application_comment_application_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='img',
            field=models.ImageField(blank=True, max_length=254, null=True, upload_to=catalog.models.get_name_file, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp'])]),
        ),
    ]