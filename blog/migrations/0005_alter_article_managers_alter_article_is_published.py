# Generated by Django 4.2.15 on 2024-12-09 17:37

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_article_slug'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='article',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
    ]
