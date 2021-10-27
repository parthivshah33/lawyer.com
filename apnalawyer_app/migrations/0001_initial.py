# Generated by Django 3.2.8 on 2021-10-15 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('age', models.PositiveIntegerField(default='18')),
                ('gender', models.CharField(max_length=10)),
                ('email_id', models.EmailField(max_length=30)),
                ('phone_number', models.CharField(max_length=15)),
                ('emergency', models.CharField(max_length=10, null=True)),
                ('confirmation_code', models.CharField(default='0000', max_length=10)),
                ('l_id', models.CharField(default='1', max_length=10)),
                ('dateTime', models.CharField(default=' ', max_length=40)),
                ('confirm', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=40)),
                ('user_phone_number', models.CharField(max_length=15)),
                ('user_email_id', models.CharField(max_length=25)),
                ('user_suggestion', models.CharField(max_length=3000, null=True)),
                ('user_query', models.CharField(max_length=3000, null=True)),
                ('user_complaint', models.CharField(max_length=3000, null=True)),
                ('user_rating', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(default='', upload_to='lawyer_images')),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(default='', max_length=10)),
                ('degree', models.CharField(max_length=40)),
                ('fees', models.CharField(max_length=8)),
                ('office_address', models.CharField(max_length=150, null=True)),
                ('specializatioin', models.CharField(max_length=40, null=True)),
                ('average_time_per_client_minute', models.CharField(default='30', max_length=4)),
                ('mobile_number', models.CharField(max_length=15)),
                ('telephone_number', models.CharField(max_length=15)),
                ('email_id', models.EmailField(max_length=30)),
                ('payment_number', models.CharField(max_length=15)),
                ('emergency_charge', models.CharField(max_length=15)),
                ('achievements', models.CharField(max_length=300, null=True)),
                ('username', models.CharField(max_length=18, unique=True)),
                ('password', models.CharField(max_length=14)),
            ],
        ),
    ]