# Generated by Django 4.0.3 on 2022-04-07 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=256)),
                ("version", models.CharField(max_length=64)),
                ("link", models.CharField(max_length=256)),
                ("guid", models.CharField(max_length=256, null=True)),
                ("description", models.TextField(max_length=256, null=True)),
                ("author_name", models.CharField(max_length=256, null=True)),
                ("author_email", models.CharField(max_length=256, null=True)),
                ("pub_date", models.DateTimeField()),
            ],
        ),
    ]
