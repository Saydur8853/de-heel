# Generated by Django 5.1.4 on 2025-01-02 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product_latest'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_us/banner/', verbose_name='Banner Image')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Title (Optional)')),
                ('subtitle', models.TextField(blank=True, null=True, verbose_name='Subtitle')),
            ],
        ),
        migrations.CreateModel(
            name='ChairmanMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('image', models.ImageField(upload_to='about_us/chairman/', verbose_name='Chairman Image')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyVoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
            ],
        ),
        migrations.CreateModel(
            name='FactoryDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('image', models.ImageField(upload_to='about_us/factory/', verbose_name='Factory Image')),
            ],
        ),
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/', verbose_name='Gallery Image')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Title (Optional)')),
                ('caption', models.TextField(blank=True, null=True, verbose_name='Caption (Optional)')),
            ],
        ),
        migrations.CreateModel(
            name='MissionVision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='mission_vision/', verbose_name='Image')),
                ('text', models.TextField(verbose_name='Text')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='our_team/', verbose_name='Member Image')),
                ('name', models.CharField(max_length=200, verbose_name='Member Name')),
                ('designation', models.CharField(max_length=200, verbose_name='Designation')),
            ],
        ),
        migrations.CreateModel(
            name='VideoSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Title')),
                ('video_link', models.URLField(blank=True, null=True, verbose_name='Video Link')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='about_us/videos/', verbose_name='Video File')),
            ],
        ),
    ]
