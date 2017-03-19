# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0008_cart_tax_percentage'),
        ('orders', '0002_auto_20170312_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_total', models.DecimalField(max_digits=50, decimal_places=2)),
                ('cart', models.ForeignKey(to='carts.Cart')),
                ('user', models.ForeignKey(to='orders.UserCheckout')),
            ],
        ),
    ]
