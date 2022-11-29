# Generated by Django 4.1.3 on 2022-11-28 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='model')),
                ('model', models.FileField(upload_to='model')),
            ],
            options={
                'db_table': 'image_model',
            },
        ),
        migrations.AddField(
            model_name='image',
            name='model',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='before_image',
            field=models.ImageField(blank=True, null=True, upload_to='before_image'),
        ),
    ]