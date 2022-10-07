from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pessoa._meta.fields if field.name not in ('id' )]
    
@admin.register(Tarefas)
class TarefasAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tarefas._meta.fields if field.name not in ('id' )]
    
@admin.register(Formulario)
class FormularioAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Formulario._meta.fields if field.name not in ('id' )]
    
@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Mensagem._meta.fields if field.name not in ('id' )]
    
@admin.register(Selo)
class SeloAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Selo._meta.fields if field.name not in ('id' )]
    