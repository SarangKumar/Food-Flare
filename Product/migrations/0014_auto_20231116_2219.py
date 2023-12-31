# Generated by Django 2.2.28 on 2023-11-16 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0013_auto_20231116_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=3)),
                ('item_name', models.CharField(max_length=15)),
                ('item_desc', models.CharField(max_length=100)),
                ('item_price', models.FloatField(blank=True, null=True)),
                ('item_image', models.ImageField(blank=True, null=True, upload_to='media/Product-images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Items',
        ),
    ]
