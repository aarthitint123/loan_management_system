# Generated by Django 3.0 on 2020-07-10 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application_form',
            fields=[
                ('applicant_name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('pan_no', models.IntegerField()),
                ('adhaar_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('parent_name', models.CharField(max_length=50)),
                ('parent_occ', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=50)),
                ('institution_name', models.CharField(max_length=30)),
                ('inst_code', models.IntegerField()),
                ('year_of_passing', models.DateField()),
                ('fee', models.IntegerField()),
                ('loanamt', models.IntegerField()),
                ('tenure', models.IntegerField()),
                ('bank_name', models.CharField(max_length=50)),
                ('acc_no', models.CharField(max_length=20)),
                ('ifsc', models.CharField(max_length=20)),
            ],
        ),

    ]
