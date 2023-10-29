# Generated by Django 4.2.6 on 2023-10-29 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_checkout_book_copy_alter_checkout_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='book_copy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserves', to='core.bookcopy', verbose_name='Book Copy'),
        ),
    ]
