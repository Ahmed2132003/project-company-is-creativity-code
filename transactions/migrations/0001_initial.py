# Generated by Django 5.0.4 on 2024-10-31 10:25

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0002_servicerequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('amount_remaining', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('transaction_status', models.CharField(choices=[('25%', '25%'), ('50%', '50%'), ('75%', '75%'), ('100%', '100%')], default='25%', max_length=4)),
                ('service_request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='services.servicerequest')),
            ],
        ),
    ]
