# Generated by Django 4.1.4 on 2023-04-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hcam', '0002_hospital_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='Hospital_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]