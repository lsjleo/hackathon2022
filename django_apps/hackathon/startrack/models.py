from random import choices
from django.db import models

# Create your models here.


class Pessoa(models.Model):
    
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=250)
    genero = models.CharField(max_length=250)
    etnia = models.CharField(max_length=250)
    especial = models.BooleanField()
    categoria = models.CharField(choices=[(x,x) for x in ['Aplicante','Contratante']],max_length=250)

    class Meta:
        
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.nome

class Tarefas(models.Model):
    
    id = models.IntegerField(primary_key=True)
    descricao = models.TextField()
    uploads = models.FileField(upload_to=None, max_length=100, blank=True, null=True)
    aplicante = models.ManyToManyField(Pessoa, related_name='aplicante',blank=True)
    contratante = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='contratante')
    situacao = models.TextField(choices=[(x,x) for x in ('OPEN','ON GOING','DONE')], default=None)
    
    
    class Meta:
        
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'

    def __str__(self):
        return f"{self.aplicante} : {self.descricao[:100]}"
    
class Mensagem(models.Model):
    
    id = models.IntegerField(primary_key=True)
    categoria = models.TextField(choices=[(x,x) for x in ('Aplicante','Contratante')], default=None)
    texto = models.TextField()
    autor = models.ManyToManyField(Pessoa)
    data = models.DateField(auto_now=True)
    tarefa = models.ForeignKey(Tarefas, on_delete=models.CASCADE)
    
    class Meta:
        
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'

    def __str__(self):
        return f"[{self.data}] {self.autor} : {self.texto[:100]}"





    
class Formulario(models.Model):
    
    id = models.IntegerField(primary_key=True)
    avaliacao = models.IntegerField(choices=[(x,x) for x in (1,2,3,4,5)], default=None)
    agilidade = models.IntegerField(choices=[(x,x) for x in (1,2,3,4,5)], default=None)
    funcionalidade = models.IntegerField(choices=[(x,x) for x in (1,2,3,4,5)], default=None)
    consideracoes = models.TextField()
    tarefa = models.ForeignKey(Tarefas, on_delete=models.CASCADE)
    

    class Meta:
        
        verbose_name = 'Formulário'
        verbose_name_plural = 'Formulários'

    def __str__(self):
        return self.tarefa
