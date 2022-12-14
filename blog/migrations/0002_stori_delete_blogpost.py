# Generated by Django 4.1.3 on 2023-01-02 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_merge_20230102_2059'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.account')),
            ],
            options={
                'verbose_name_plural': 'Mastori',
            },
        ),
        migrations.DeleteModel(
            name='Blogpost',
        ),
    ]
