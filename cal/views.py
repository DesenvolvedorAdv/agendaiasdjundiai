# from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.http import JsonResponse, HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View
from django.utils.dateparse import parse_datetime
from django.shortcuts import render
from .models import Evento
from home.models import Sala
import datetime
import pytz

class IndexView(TemplateView):
    template_name = 'index.html'

    # @method_decorator(ensure_csrf_cookie)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Evento.objects.all()
        return context

# def index(request):  
#     all_events = Evento.objects.all()
#     context = {
#         "events":all_events,
#     }
#     return render(request,'index.html',context)

class AllEventsView(View):
    def get(self, request, *args, **kwargs):
        tz = pytz.timezone('America/Sao_Paulo')
        eventos_aprovados = Evento.objects.filter(aprovada=True)
        events_list = []

        for event in eventos_aprovados:
            start_local = event.start.astimezone(tz).strftime("%Y-%m-%dT%H:%M:%S")
            end_local = event.end.astimezone(tz).strftime("%Y-%m-%dT%H:%M:%S")
            events_list.append({
                'id': event.id,
                'title': event.name,
                'start': start_local,
                'end': end_local,
                'salaNome': event.sala.name if event.sala else 'Sem sala',  # Adiciona o nome da sala
                'usuario': event.usuario.get_username() if event.usuario else 'Anônimo',  # Adiciona o nome do usuário
                # 'departamento': event.usuario.departamento if event.usuario else 'Sem departamento',  # Adiciona o departamento
                'backgroundColor': event.cor,
            })

        return JsonResponse(events_list, safe=False)

# class AllEventsView(View):
#     def get(self, request, *args, **kwargs):
#         tz = pytz.timezone('America/Sao_Paulo')
#         eventos_aprovados = Evento.objects.filter(aprovada=True).select_related('usuario', 'sala')
#         events_list = []

#         for event in eventos_aprovados:
#             start_local = event.start.astimezone(tz).strftime("%Y-%m-%dT%H:%M:%S")
#             end_local = event.end.astimezone(tz).strftime("%Y-%m-%dT%H:%M:%S")
#             events_list.append({
#                 'id': event.id,
#                 'title': event.name,
#                 'start': start_local,
#                 'end': end_local,
#                 'salaNome': event.sala.name if event.sala else 'Sem sala',  # Adiciona o nome da sala
#                 'usuario': event.usuario.get_username() if event.usuario else 'Anônimo',  # Adiciona o nome do usuário
#                 'departamento': event.usuario.departamento if event.usuario else 'Sem departamento',  # Adiciona o departamento
#                 'backgroundColor': event.cor,  # Cor de fundo do evento
#             })

        return JsonResponse(events_list, safe=False)




# def all_events(request):
#     all_events = Evento.objects.all()
#     events_list = []
#     # Definindo o fuso horário desejado
#     tz = pytz.timezone('America/Sao_Paulo')
#     eventos_ap = Evento.objects.filter(aprovada=True).values('id', 'start', 'end', 'title')
#     # eventos_list = list(eventos_ap)
#     for event in eventos_ap:
#         # Converte as datas para o fuso horário desejado antes de formatar
#         start_local = event.start.astimezone(tz).strftime("%Y-%m-%dT%H:%M:%S")
#         end_local = event.end.astimezone(tz).strftime("%Y-%m-%dT%H:%M:%S")
#         events_list.append({
#             'id': event.id,
#             'title': event.name,
#             'start': start_local,
#             'end': end_local,
#             'backgroundColor': event.cor,  # Se você quer usar o campo 'cor' para definir a cor do evento no calendário
#         })
#     return JsonResponse(events_list, safe=False)


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
@csrf_exempt
def add_event(request):
    # Aqui assumimos que os dados vêm via POST para melhor prática
    if request.method == "POST":
        start = request.POST.get("start")
        end = request.POST.get("end")
        title = request.POST.get("title")
        sala_id = request.POST.get("sala_id")  # ID da Sala vem do carrossel

        # Converte as strings de data e hora para objetos datetime
        start_dt = parse_datetime(start)
        end_dt = parse_datetime(end)

        if None in (start, end, title, sala_id):
            return HttpResponseBadRequest("Todos os campos são obrigatórios.")

        try:
            sala = Sala.objects.get(pk=sala_id)
        except Sala.DoesNotExist:
            return HttpResponseBadRequest("Sala não encontrada.")

        event = Evento(name=title, start=start_dt, end=end_dt, cor=sala.cor)
        event.save()
        event.sala.add(sala)  # Associa a sala ao evento

        return JsonResponse({'status': 'success', 'event_id': event.id})
    else:
        return HttpResponseBadRequest("Método não suportado.") 
# def add_event(request):
#     start = request.GET.get("start", None)
#     end = request.GET.get("end", None)
#     title = request.GET.get("title", None)
#     event = Evento(name=str(title), start=start, end=end)
#     event.save()
#     data = {}
#     return JsonResponse(data)
 
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