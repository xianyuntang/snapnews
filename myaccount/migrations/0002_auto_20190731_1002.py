# Generated by Django 2.2.3 on 2019-07-31 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userkeyword',
            old_name='keyword_group',
            new_name='keyword',
        ),
        migrations.RemoveField(
            model_name='userkeyword',
            name='keyword_excluded',
        ),
        migrations.RemoveField(
            model_name='userkeyword',
            name='keyword_included',
        ),
    ]
