# Generated by Django 4.2 on 2023-04-22 13:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0005_tarefa_data_conclusao_alter_tarefa_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='descricao',
            field=ckeditor.fields.RichTextField(verbose_name='Descrição'),
        ),
    ]
