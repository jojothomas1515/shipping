# Generated by Django 4.0.4 on 2023-03-01 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0002_remove_package_receiver_remove_package_sender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='package_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
