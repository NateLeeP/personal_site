# Generated by Django 4.2.3 on 2023-11-09 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_post_post_preview"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="post_preview",
            field=models.TextField(null=True),
        ),
    ]