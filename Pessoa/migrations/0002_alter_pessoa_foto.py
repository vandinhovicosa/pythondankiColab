# Generated by Django 3.2 on 2021-04-26 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotopessoal'),
        ),
    ]
