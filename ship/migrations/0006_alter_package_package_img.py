# Generated by Django 4.0.4 on 2023-03-01 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0005_alter_package_map_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='package_img',
            field=models.ImageField(upload_to=''),
        ),
    ]