# Generated by Django 4.0.6 on 2023-02-11 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_productimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default='static/resume.png', help_text='Upload a product image', upload_to='images/', verbose_name='image'),
        ),
    ]
