# Generated by Django 4.0 on 2024-02-09 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_type', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3)),
                ('amount_available', models.IntegerField()),
                ('donation_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('landmark', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=10)),
                ('size', models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], max_length=10)),
            ],
        ),
    ]
