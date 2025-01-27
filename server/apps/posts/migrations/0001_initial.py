# Generated by Django 5.0.1 on 2024-07-16 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_created=True, auto_now=True, verbose_name='수정일')),
                ('created_date', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='작성일')),
                ('title', models.CharField(max_length=24, verbose_name='제목')),
                ('content', models.CharField(max_length=24, verbose_name='내용')),
                ('region', models.CharField(max_length=24, verbose_name='지역')),
                ('price', models.IntegerField(default=1000, verbose_name='가격')),
                ('photo', models.ImageField(blank=True, upload_to='posts/%Y%m%d', verbose_name='이미지')),
            ],
        ),
    ]
