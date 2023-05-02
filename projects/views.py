from django.shortcuts import render
import requests

def projects(request):
    response = requests.get('https://urbe.me/administracao/api/lista-projetos/').json()
    return render(request, 'projects.html', {'response': response})