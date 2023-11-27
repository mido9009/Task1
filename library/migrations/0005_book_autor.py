# Generated by Django 4.2 on 2023-11-27 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Book_author', to='library.author'),
            preserve_default=False,
        ),
    ]