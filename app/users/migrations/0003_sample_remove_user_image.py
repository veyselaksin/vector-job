# Generated by Django 4.0.3 on 2022-05-27 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]
