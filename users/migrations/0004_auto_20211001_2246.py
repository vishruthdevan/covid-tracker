# Generated by Django 3.2.6 on 2021-10-01 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='covidaffected',
            field=models.CharField(choices=[('T', 'True'), ('F', 'False'), ('R', 'Recovered')], default='F', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='vaccinated',
            field=models.CharField(choices=[('0', 'Not vaccinated'), ('1', 'One dose'), ('2', 'Two doses')], default='1', max_length=1),
            preserve_default=False,
        ),
    ]
