# Generated by Django 4.1.7 on 2023-04-06 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_sub_cat_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('sub_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sub_cat')),
            ],
        ),
    ]
