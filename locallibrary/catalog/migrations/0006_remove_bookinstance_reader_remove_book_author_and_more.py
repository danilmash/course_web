# Generated by Django 4.2.2 on 2023-06-18 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_book_isbn_alter_author_biography'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstance',
            name='reader',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.author'),
        ),
    ]