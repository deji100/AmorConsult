# Generated by Django 4.2.2 on 2023-06-28 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_home_client_section_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(blank=True, max_length=100, null=True)),
                ('header_text', models.CharField(blank=True, max_length=100, null=True)),
                ('service_section1_header', models.CharField(blank=True, max_length=50, null=True)),
                ('service_section1_content', models.TextField(blank=True, max_length=500, null=True)),
                ('service_section1_image', models.FileField(blank=True, null=True, upload_to='')),
                ('service_section2_header', models.CharField(blank=True, max_length=50, null=True)),
                ('service_section2_content', models.TextField(blank=True, max_length=500, null=True)),
                ('service_section2_image', models.FileField(blank=True, null=True, upload_to='')),
                ('service_section3_header', models.CharField(blank=True, max_length=50, null=True)),
                ('service_section3_content', models.TextField(blank=True, max_length=500, null=True)),
                ('service_section3_image', models.FileField(blank=True, null=True, upload_to='')),
                ('service_section4_header', models.CharField(blank=True, max_length=50, null=True)),
                ('service_section4_content', models.TextField(blank=True, max_length=500, null=True)),
                ('service_section4_image', models.FileField(blank=True, null=True, upload_to='')),
                ('service_section5_header', models.CharField(blank=True, max_length=50, null=True)),
                ('service_section5_content', models.TextField(blank=True, max_length=500, null=True)),
                ('service_section5_image', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Service_why_amorserv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(blank=True, max_length=100, null=True)),
                ('point1', models.CharField(blank=True, max_length=150, null=True)),
                ('point2', models.CharField(blank=True, max_length=150, null=True)),
                ('point3', models.CharField(blank=True, max_length=150, null=True)),
                ('point4', models.CharField(blank=True, max_length=150, null=True)),
                ('point5', models.CharField(blank=True, max_length=150, null=True)),
                ('point6', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]