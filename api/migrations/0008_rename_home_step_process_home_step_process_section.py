# Generated by Django 4.2.2 on 2023-06-29 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_content_home_overwhelmed_section_content1_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Home_step_process',
            new_name='Home_step_process_section',
        ),
    ]
