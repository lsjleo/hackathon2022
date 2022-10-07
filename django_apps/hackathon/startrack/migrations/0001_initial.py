# Generated by Django 3.2.16 on 2022-10-07 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=250)),
                ('genero', models.CharField(max_length=250)),
                ('etnia', models.CharField(max_length=250)),
                ('especial', models.BooleanField()),
                ('categoria', models.CharField(choices=[('Aplicante', 'Aplicante'), ('Contratante', 'Contratante')], max_length=250)),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='Tarefas',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('descricao', models.TextField()),
                ('uploads', models.FileField(blank=True, null=True, upload_to=None)),
                ('situacao', models.TextField(choices=[('OPEN', 'OPEN'), ('ON GOING', 'ON GOING'), ('DONE', 'DONE')], default=None)),
                ('aplicante', models.ManyToManyField(blank=True, related_name='aplicante', to='startrack.Pessoa')),
                ('contratante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contratante', to='startrack.pessoa')),
            ],
            options={
                'verbose_name': 'Tarefa',
                'verbose_name_plural': 'Tarefas',
            },
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('categoria', models.TextField(choices=[('Aplicante', 'Aplicante'), ('Contratante', 'Contratante')], default=None)),
                ('texto', models.TextField()),
                ('data', models.DateField(auto_now=True)),
                ('autor', models.ManyToManyField(to='startrack.Pessoa')),
                ('tarefa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startrack.tarefas')),
            ],
            options={
                'verbose_name': 'Mensagem',
                'verbose_name_plural': 'Mensagens',
            },
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('avaliacao', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=None)),
                ('agilidade', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=None)),
                ('funcionalidade', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=None)),
                ('consideracoes', models.TextField()),
                ('tarefa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startrack.tarefas')),
            ],
            options={
                'verbose_name': 'Formulário',
                'verbose_name_plural': 'Formulários',
            },
        ),
    ]