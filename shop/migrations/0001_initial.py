# Generated by Django 5.0.4 on 2024-05-06 09:25

import django.core.validators
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
                ('category', models.CharField(choices=[('gold', 'gold'), ('silver', 'silver'), ('bronza', 'bronza')], help_text='Maxsulot kategoriyasi!', max_length=50)),
                ('price', models.FloatField(default=0.0, help_text='Maxsulot narxi', validators=[django.core.validators.MinValueValidator(0.0, "Narx manfiy son bo'lishi mumkin emas")])),
                ('description', models.TextField(help_text='Maxsulot uchun tarif')),
                ('image', models.ImageField(help_text='Maxsulot rasmi', upload_to='product/images/')),
            ],
        ),
    ]