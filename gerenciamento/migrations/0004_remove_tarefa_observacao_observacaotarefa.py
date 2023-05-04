# Generated by Django 4.2 on 2023-04-21 06:42

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0003_tarefa_observacao_tarefa_situacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarefa',
            name='observacao',
        ),
        migrations.CreateModel(
            name='ObservacaoTarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacao', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Observação')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('tarefa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='observacoes', to='gerenciamento.tarefa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
