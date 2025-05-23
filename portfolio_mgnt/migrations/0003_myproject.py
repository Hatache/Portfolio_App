# Generated by Django 5.1.7 on 2025-03-12 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_mgnt', '0002_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=200)),
                ('project_description', models.TextField()),
                ('image', models.ImageField(upload_to='project_images/')),
                ('demo_link', models.URLField()),
                ('git_link', models.URLField()),
            ],
        ),
    ]
