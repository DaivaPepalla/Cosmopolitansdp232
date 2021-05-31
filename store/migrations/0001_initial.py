# Generated by Django 3.2.2 on 2021-05-08 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'menu',
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(upload_to='images/')),
                ('slug', models.SlugField(max_length=255)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_creator', to=settings.AUTH_USER_MODEL)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='store.menu')),
            ],
            options={
                'verbose_name_plural': 'Items',
            },
        ),
    ]