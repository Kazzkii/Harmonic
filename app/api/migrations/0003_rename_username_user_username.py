# Generated by Django 3.2.14 on 2022-07-22 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_user_login_loc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='userName',
            new_name='username',
        ),
    ]