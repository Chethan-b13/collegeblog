# Generated by Django 3.0.3 on 2020-04-14 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200409_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='user_number',
            field=models.CharField(blank=True, default='', max_length=12),
        ),
    ]