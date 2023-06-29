# Generated by Django 4.2.2 on 2023-06-29 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_blogpostcategory_blogpost_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Enquiries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('message', models.TextField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name_plural': 'Contact Enquiries',
            },
        ),
        migrations.CreateModel(
            name='Contact_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'verbose_name_plural': 'Contact Info',
            },
        ),
        migrations.RenameModel(
            old_name='BlogPost',
            new_name='Blog_Post',
        ),
        migrations.RenameModel(
            old_name='BlogPostCategory',
            new_name='Blog_Post_Category',
        ),
        migrations.RenameModel(
            old_name='BlogPostComment',
            new_name='Blog_Post_Comment',
        ),
    ]
