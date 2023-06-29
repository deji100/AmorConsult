# Generated by Django 4.2.2 on 2023-06-29 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_name_home_client_section_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home_overwhelmed_section',
            old_name='content',
            new_name='content1',
        ),
        migrations.RenameField(
            model_name='home_overwhelmed_section',
            old_name='img',
            new_name='img1',
        ),
        migrations.AddField(
            model_name='home_overwhelmed_section',
            name='content2',
            field=models.TextField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='home_overwhelmed_section',
            name='content3',
            field=models.TextField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='home_overwhelmed_section',
            name='content4',
            field=models.TextField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='home_overwhelmed_section',
            name='img2',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='home_overwhelmed_section',
            name='img3',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='home_overwhelmed_section',
            name='img4',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='home_proposal_section',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]