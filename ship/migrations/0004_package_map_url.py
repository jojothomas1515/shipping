# Generated by Django 4.0.4 on 2023-03-01 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0003_package_package_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='map_url',
            field=models.URLField(blank=True, default='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d63418.72762958233!2d3.321469527912889!3d6.563212688714463!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x103b8b2ae68280c1%3A0xdc9e87a367c3d9cb!2sLagos!5e0!3m2!1sen!2sng!4v1664918175697!5m2!1sen!2sng', null=True),
        ),
    ]
