# Generated by Django 2.2.1 on 2019-06-18 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190618_1355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', 'updated', 'timestamp']},
        ),
    ]
