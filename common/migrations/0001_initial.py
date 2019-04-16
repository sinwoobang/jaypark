# Generated by Django 2.2 on 2019-04-16 16:07

import accounts.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=accounts.utils.generate_photo_profile_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]