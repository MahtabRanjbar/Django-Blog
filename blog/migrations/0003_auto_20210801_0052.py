# Generated by Django 3.2.5 on 2021-07-31 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210801_0019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Status',
            new_name='status',
        ),
        migrations.AddField(
            model_name='article',
            name='cateegory',
            field=models.ManyToManyField(to='blog.Category', verbose_name='دسته بندی'),
        ),
    ]
