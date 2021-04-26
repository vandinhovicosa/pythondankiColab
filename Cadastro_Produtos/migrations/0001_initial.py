# Generated by Django 3.2 on 2021-04-26 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Enderecos', '0001_initial'),
        ('Pessoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro_Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotodpesoal')),
                ('produto', models.CharField(max_length=255)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15)),
                ('data_pedido', models.DateField()),
                ('descricao', models.FileField(blank=True, null=True, upload_to='descricao/')),
                ('relatorio', models.FileField(blank=True, null=True, upload_to='relatorios/')),
                ('obs', models.TextField()),
                ('endereco_entrega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Enderecos.endereco')),
                ('outro_remetente', models.ManyToManyField(blank=True, to='Pessoa.Pessoa')),
            ],
        ),
    ]
