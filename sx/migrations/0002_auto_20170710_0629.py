# Generated by Django 2.0.dev20170412153647 on 2017-07-10 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sx', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='uaddress',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uphone',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uposCode',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='ushou',
            field=models.CharField(default='', max_length=20),
        ),
    ]