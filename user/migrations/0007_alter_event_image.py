# Generated by Django 4.2.2 on 2023-09-10 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_event_image_alter_event_edate_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(default='img/eventdefault.png', upload_to='event_image/'),
        ),
    ]