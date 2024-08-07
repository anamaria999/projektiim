# Generated by Django 5.0 on 2024-07-04 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(blank=True, max_length=250, null=True)),
                ('product_description', models.TextField(blank=True, max_length=2000, null=True)),
                ('product_week', models.IntegerField(blank=True, null=True)),
                ('product_hours', models.FloatField(blank=True, null=True)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product/')),
            ],
        ),
    ]
