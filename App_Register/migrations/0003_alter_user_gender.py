# Generated by Django 4.2.6 on 2023-10-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Register', '0002_alter_user_gender_alter_user_technologies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=100, null=True),
        ),
    ]