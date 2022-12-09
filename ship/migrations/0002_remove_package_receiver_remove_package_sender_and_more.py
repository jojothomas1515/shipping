# Generated by Django 4.0.4 on 2022-11-21 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='package',
            name='sender',
        ),
        migrations.AddField(
            model_name='reciever',
            name='package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ship.package'),
        ),
        migrations.AddField(
            model_name='sender',
            name='package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ship.package'),
        ),
    ]