# Generated by Django 3.1.7 on 2021-03-07 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0003_product_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='distributor.product')),
            ],
        ),
    ]
