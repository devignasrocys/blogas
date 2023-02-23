# Generated by Django 4.1.7 on 2023-02-21 13:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(db_index=True, max_length=50, verbose_name='last name')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for ', primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('article', models.TextField(max_length=100, verbose_name='article')),
                ('post', models.TextField(max_length=4000, verbose_name='post')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='blogas_app.author', verbose_name='author')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=4000, verbose_name='comment')),
                ('date', models.DateField(verbose_name='date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='blogas_app.author', verbose_name='author')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='blogas_app.post', verbose_name='post')),
            ],
        ),
    ]
