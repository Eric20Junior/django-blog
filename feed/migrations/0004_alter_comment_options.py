# Generated by Django 4.1.2 on 2022-10-11 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
