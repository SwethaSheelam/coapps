# Generated by Django 5.0.4 on 2024-05-06 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20240504_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='proof',
            field=models.CharField(choices=[('Aadhar', 'Aadhar Card'), ('Pan', 'Pan Card'), ('Passport', 'Passport')], default='Aadhar', max_length=100),
        ),
        migrations.AddField(
            model_name='document',
            name='proof_file',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='document',
            name='resume',
            field=models.FileField(default=123, upload_to='documents/'),
            preserve_default=False,
        ),
    ]
