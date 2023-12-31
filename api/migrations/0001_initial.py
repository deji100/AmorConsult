# Generated by Django 4.2.2 on 2023-06-28 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header_section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_type', models.CharField(blank=True, max_length=20, null=True)),
                ('header_h1_content', models.TextField(blank=True, max_length=225, null=True)),
                ('header_p_content', models.TextField(blank=True, max_length=225, null=True)),
                ('header_image', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Home_client_section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Home_happy_customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_image', models.FileField(blank=True, null=True, upload_to='')),
                ('customer_name', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_comment', models.TextField(blank=True, max_length=225, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Home_overwhelmed_section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(blank=True, null=True, upload_to='')),
                ('content', models.TextField(blank=True, max_length=225, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Home_proposal_section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph1', models.TextField(blank=True, max_length=225, null=True)),
                ('paragraph2', models.TextField(blank=True, max_length=225, null=True)),
                ('paragraph3', models.TextField(blank=True, max_length=225, null=True)),
                ('paragraph4', models.TextField(blank=True, max_length=225, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Home_service_section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.FileField(blank=True, null=True, upload_to='')),
                ('content', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Home_step_process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_header', models.CharField(blank=True, max_length=100, null=True)),
                ('step1', models.CharField(blank=True, max_length=100, null=True)),
                ('content1', models.CharField(blank=True, max_length=200, null=True)),
                ('step2', models.CharField(blank=True, max_length=100, null=True)),
                ('content2', models.CharField(blank=True, max_length=200, null=True)),
                ('step3', models.CharField(blank=True, max_length=100, null=True)),
                ('content3', models.CharField(blank=True, max_length=200, null=True)),
                ('content4', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
