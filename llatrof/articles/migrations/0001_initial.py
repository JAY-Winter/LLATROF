# Generated by Django 4.1.2 on 2022-12-01 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_title', models.TextField()),
                ('goods_price', models.IntegerField()),
                ('goods_url', models.TextField()),
                ('goods_img_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecommendArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='goods_brand',
            field=models.ForeignKey(db_column='goods_brand', on_delete=django.db.models.deletion.CASCADE, to='articles.brand', to_field='brand'),
        ),
        migrations.AddField(
            model_name='article',
            name='goods_category',
            field=models.ForeignKey(db_column='goods_category', on_delete=django.db.models.deletion.CASCADE, to='articles.category', to_field='category'),
        ),
    ]
