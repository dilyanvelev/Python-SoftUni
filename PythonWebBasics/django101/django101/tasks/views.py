from django.http import HttpResponse
from django.shortcuts import render

from django101.tasks.models import Model


# Create your views here.


# def home(request):
#     items = Model.objects.all()
#     items_string = ''.join(f'<li>{model.title}, {model.text}</li>' for model in items)
#
#     html = f'''
#     <h1>It works!</h1>
#     <ul>
#         {items_string}
#     </ul>
#     '''
#
#     return HttpResponse(html)

def home(request):
    contex = {
        'title': 'It works from the view!!!',
        'names': Model.objects.all()
    }

    return render(request, 'index.html', contex)
