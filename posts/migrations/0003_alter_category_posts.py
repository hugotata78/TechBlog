# Generated by Django 4.2.1 on 2023-05-23 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='posts',
            field=models.ManyToManyField(blank=True, related_name='categories', to='posts.post'),
        ),
    ]