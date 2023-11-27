# Generated by Django 4.2 on 2023-11-26 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_book_publication_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=20)),
                ('content', models.TextField(max_length=100)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
        ),
    ]
