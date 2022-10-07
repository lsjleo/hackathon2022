from django.shortcuts import render
import pandas as pd
from .models import *
import boto3
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Create your views here.

def get_sentiments(x):
    client = boto3.client(
        'comprehend', 
        region_name='us-west-2',
        aws_access_key_id = 'AKIA5ZXJKRTQJFYRNUOY',
        aws_secret_access_key = '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'  
    )
    response = client.detect_sentiment(
        Text=x,
        LanguageCode='pt'
    )
    return response['SentimentScore']

def index(request):
    obj = {
        'forms':Formulario.objects.select_related('tarefa').all(),
        'tarefas':Tarefas.objects.select_related('contratante').all()
    }
    
    return render(request, 'header.html', obj)

def ia(request):
    form = pd.DataFrame(list(Formulario.objects.all().values()))
    pessoa = pd.DataFrame(list(Pessoa.objects.all().values())).rename(columns={'id':'contratante_id'})
    tarefa = pd.DataFrame(list(Tarefas.objects.select_related('aplicante').all().values())).rename(columns={'id':'tarefa_id'})
    
    
    df = pd.merge(
        form,
        tarefa,
        how='inner',
        left_on='tarefa_id',
        right_on='tarefa_id'
    )
    
    df = pd.merge(
        df,
        pessoa,
        how='inner',
        left_on='contratante_id',
        right_on='contratante_id'
    )
    
    df['sentimentos'] = df['consideracoes'].apply(get_sentiments)
    
    if 'pkid' in request.GET.keys():
        df = df[df['contratante_id'].map(str)==request.GET['pkid'][0]]
       
    df2 = df.groupby('contratante_id').agg({'avaliacao':'mean','agilidade':'mean','funcionalidade':'mean'}).reset_index()
     
    a = ctrl.Antecedent(np.arange(0, 5, 1), 'avaliacao')
    b = ctrl.Antecedent(np.arange(0, 5, 1), 'agilidade')
    c = ctrl.Antecedent(np.arange(0, 5, 1), 'funcionalidade')
    skill = ctrl.Consequent(np.arange(0, 26, 1), 'skill')

    # Auto-membership function population is possible with .automf(3, 5, or 7)
    a.automf(3)
    b.automf(3)
    c.automf(3)

    # Custom membership functions can be built interactively with a familiar,
    # Pythonic API
    skill['low'] = fuzz.trimf(skill.universe, [0, 0, 13])
    skill['medium'] = fuzz.trimf(skill.universe, [0, 13, 25])
    skill['high'] = fuzz.trimf(skill.universe, [13, 25, 25])

    rule1 = ctrl.Rule(a['poor'] | b['poor'], skill['low'])
    rule2 = ctrl.Rule(a['average'], skill['medium'])
    rule3 = ctrl.Rule(c['good'] | b['good'], skill['high'])

    tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
    tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

    tipping.input['avaliacao'] = df2.to_dict()['avaliacao'][0]
    tipping.input['agilidade'] = df2.to_dict()['agilidade'][0]
    tipping.input['funcionalidade'] = df2.to_dict()['funcionalidade'][0]

    # Crunch the numbers
    tipping.compute()
    fuzzyout = (tipping.output['skill'] / 25) * 100
    
    if fuzzyout < 33:
        cat = 'JUNIOR'
    elif fuzzyout >= 33 and fuzzyout < 66:
        cat = 'PLENO'
    else:
        cat = 'SENIOR'
    
    obj = {
        'form':df.to_dict(),
        'pessoa':df2.to_dict(),
        'skill':{'fuzzyout':fuzzyout,'result':cat},
    }
    return render(request, 'ia.html', obj)