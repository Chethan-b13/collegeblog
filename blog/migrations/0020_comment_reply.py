# Generated by Django 3.0.3 on 2020-04-24 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='Reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='blog.Comment'),
        ),
    ]