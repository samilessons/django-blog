# Generated by Django 4.2.15 on 2024-12-27 18:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_author_alter_category_options_alter_article_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='adv',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adv', to='blog.adv', verbose_name='Գովազդներ'),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='blog.author', verbose_name='Հեղինակ'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='blog.category', verbose_name='Կատեգորիաներ'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, verbose_name='Նյութի կոնտենտ'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_published',
            field=models.BooleanField(choices=[(False, 'Draft'), (True, 'Published')], default=1, verbose_name='Հրապարակել թե՞ ոչ'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='blog.articletags', verbose_name='Թեգեր'),
        ),
        migrations.AlterField(
            model_name='article',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Հրապարակման ամսաթիվ'),
        ),
        migrations.AlterField(
            model_name='article',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Փոփոխման ամսաթիվ'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3, message='Համոզվեք որ 3 տառից ավել եք գրել')], verbose_name='Վերնագիր'),
        ),
        migrations.AlterField(
            model_name='author',
            name='articles_qty',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
