# Generated by Django 5.0 on 2024-10-10 09:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_options'),
        ('profiles', '0002_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='profiles.profile'),
        ),
    ]