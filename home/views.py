from django.views.generic import TemplateView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from .models import Sala
from cal.models import Evento
import datetime

# from django.http import HttpResponseRedirect
# from django.urls import reverse_lazy, reverse
# Create your views here.
# def homepage(request):
#     context = {}
#     context['list_salas'] = Sala.objects.all()
#     context['hor'] = {'pad':['','','',''],'fpad':['','']}
#     return render(request, 'homepage.html', context)

class Homepage(LoginRequiredMixin,TemplateView):
    template_name = "homepage.html"
#   all_events = #filter() order_by
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_salas'] = Sala.objects.all()  # Obter todas as salas
        return context


# class detalhe_sala(LoginRequiredMixin,DetailView):#pop-up
#     model = Sala
#     template_name = "pop_up.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # self.get_object()
#         sala = self.get_object()
#         horarios_rl = sala.horarios.all()
#         context['horarios_rl'] = horarios_rl
#         return context
class detalhe_sala(LoginRequiredMixin, DetailView):
    model = Sala
    template_name = "pop_up.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sala = self.get_object()
        horarios_rl = sala.horarios.all()
        context['horarios_rl'] = horarios_rl
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():
            sala = self.get_object()
            horarios_rl = list(sala.horarios.all().values('name', 'horario_inicio', 'horario_fim'))
            return JsonResponse({'room_name': sala.name, 'horarios_rl': horarios_rl})
        else:
            return super().render_to_response(context, **response_kwargs)

# class VerificarDisponibilidadeView(View):
#     def get(self, request, sala_id, data):
#         sala = get_object_or_404(Sala, pk=sala_id)
#         data_parsed = datetime.datetime.strptime(data, '%Y-%m-%d').date()
#         eventos = Evento.objects.filter(sala=sala, start__date=data_parsed)
#         horarios_ocupados = eventos.values_list('start', 'end')

#         horarios = [{'start': horario[0].strftime('%H:%M'), 'end': horario[1].strftime('%H:%M')} for horario in horarios_ocupados]

#         return JsonResponse({'horarios': horarios})

class VerificarDisponibilidadeView(View):
    def get(self, request, sala_id, data):
        sala = get_object_or_404(Sala, pk=sala_id)
        data_parsed = datetime.datetime.strptime(data, '%Y-%m-%d').date()
        
        horarios_definidos = sala.horarios.all()
        eventos_agendados = Evento.objects.filter(sala=sala, start__date=data_parsed)

        horarios_disponiveis = []
        for horario in horarios_definidos:
            ocupado = False
            for evento in eventos_agendados:
                if horario.horario_inicio < evento.end.time() and horario.horario_fim > evento.start.time():
                    ocupado = True
                    break
            if not ocupado:
                horarios_disponiveis.append({
                    'nome': horario.name,
                    'inicio': horario.horario_inicio.strftime('%H:%M'),
                    'fim': horario.horario_fim.strftime('%H:%M')
                })

        return JsonResponse({'horarios_disponiveis': horarios_disponiveis})

class AgendarEventoView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        sala_id = data.get('sala_id')
        data_evento = data.get('data')
        inicio = data.get('inicio')
        fim = data.get('fim')
        nome_evento = data.get('name')

        data_inicio = datetime.datetime.strptime(f'{data_evento} {inicio}', '%Y-%m-%d %H:%M')
        data_fim = datetime.datetime.strptime(f'{data_evento} {fim}', '%Y-%m-%d %H:%M')
        sala = get_object_or_404(Sala, pk=sala_id)

        evento = Evento.objects.create(
            usuario=request.user if request.user.is_authenticated else None,
            name=nome_evento,
            sala=sala,
            start=data_inicio,
            end=data_fim,
            aprovada=False,
            cor=sala.cor,
        )

        return JsonResponse({'status': 'success', 'evento_id': evento.id})#", home/urls.py = "app_name = 'home'

class Paginaperfil(LoginRequiredMixin, TemplateView):
    template_name = "editarperfil.html"
    # def your_view(self):
    #     events = Events.objects.all()
    #     event_data = [
    #         {
    #             "title": event.name,
    #             "start": event.start.isoformat(),
    #             "end": event.end.isoformat(),
    #             "sala": event.sala.nome,
    #             "status": event.aprovada
    #         } for event in events
    #     ]

    #     return render(request, 'seu_template.html', {'events_data_json': json.dumps(event_data)})
    # def get(self, request):
    #     events = Events.objects.all()
    #     event_data = []
    #     for event in events:
    #         event_data.append({
    #             "title": event.name,
    #             "start": event.start.isoformat(),
    #             "end": event.end.isoformat(),
    #             "sala": event.sala.nome,
    #             "status": event.aprovada
    #         })
    #     return JsonResponse({"events": event_data})
# @login_required(login_url="signup")
# def create_event(request):
#     form = EventsForm(request.POST or None)
#     if request.POST and form.is_valid():
#         title = form.cleaned_data["title"]
#         start_time = form.cleaned_data["start_time"]
#         end_time = form.cleaned_data["end_time"]
#         Events.objects.get_or_create(
#             user=request.user,
#             name=title,
#             start=start_time,
#             end=end_time,
#         )
#         return HttpResponseRedirect(reverse(""))
#     return render(request, "pop_up.html", {"form": form})

# class DashboardView(LoginRequiredMixin, View):
#     login_url = "accounts:signin"
#     template_name = "calendarapp/dashboard.html"

#     def get(self, request, *args, **kwargs):
#         events = Event.objects.get_all_events(user=request.user)
#         running_events = Event.objects.get_running_events(user=request.user)
#         latest_events = Event.objects.filter(user=request.user).order_by("-id")[:10]
#         context = {
#             "total_event": events.count(),
#             "running_events": running_events,
#             "latest_events": latest_events,
#         }
#         return render(request, self.template_name, context)

        # horario_rl = Sala.objects.filter(horarios=self.get_object().horarios.all()[0].id)   # Primeira semana do mês
        # context['horario_rl'] = horario_rl
        # return context

# class solicitação(DetailView):#pop-up
#     model = Events
#     template_name = "pop_up.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context

#     context = {}
#     context['list_salas'] = Sala.objects.all()
    




# def index(request):
#     all_events = Events.objects.all()#filter() order_by
#     context = {
#         "events": all_events,
#     }
#     return render(request, 'index.html', context)

def all_events(request):                                                                                            
    all_events = Events.objects.all()                                                                                    
    out = []
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'title': event.name,                                                                                         
            'id': event.id,                                                                                              
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
        }) 
                                                                                                                      
    return JsonResponse(out, safe=False) 
 
def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)
 
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)
 
def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)