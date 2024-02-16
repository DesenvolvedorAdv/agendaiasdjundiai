# from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.http import JsonResponse 
from .models import Evento
import datetime
import pytz

# Create your views here.
def index(request):  
    all_events = Evento.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'index.html',context)

def all_events(request):
    all_events = Evento.objects.all()
    events_list = []
    
    # Definindo o fuso horário desejado
    tz = pytz.timezone('America/Sao_Paulo')
    
    for event in all_events:
        # Converte as datas para o fuso horário desejado antes de formatar
        start_local = event.start.astimezone(tz).strftime("%Y-%m-%dT%H:%M:%S")
        end_local = event.end.astimezone(tz).strftime("%Y-%m-%dT%H:%M:%S")
        events_list.append({
            'id': event.id,
            'title': event.name,
            'start': start_local,
            'end': end_local,
            'backgroundColor': event.cor,  # Se você quer usar o campo 'cor' para definir a cor do evento no calendário
        })
    
    return JsonResponse(events_list, safe=False)


            # 'start': event.start.strftime("%Y-%m-%dT%H:%M:%S"),
            # 'end': event.end.strftime("%Y-%m-%dT%H:%M:%S"),

    # all_events = Evento.objects.all()
    # out = []                                                                                                             
    # for event in all_events:                                                                                             
    #     out.append({                                                                                                     
    #         'title': event.name,                                                                                         
    #         'id': event.id,                                                                                              
    #         'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
    #         'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
    #     })                                                                                                               
                                                                                                                      
    # return JsonResponse(out, safe=False) 
 
def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Evento(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)
 
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Evento.objects.get(id=id)
    event.start = start
    event.end = end 
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)
 
def remove(request):
    id = request.GET.get("id", None)
    event = Evento.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)