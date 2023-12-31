# Generated by Django 3.0.7 on 2020-06-13 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0003_auto_20200610_0917'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMarketPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_time', models.DateTimeField()),
                ('open', models.DecimalField(decimal_places=4, max_digits=32)),
                ('high', models.DecimalField(decimal_places=4, max_digits=32)),
                ('low', models.DecimalField(decimal_places=4, max_digits=32)),
                ('close', models.DecimalField(decimal_places=4, max_digits=32)),
                ('volume', models.BigIntegerField()),
                ('close_time', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
