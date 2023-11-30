from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import categoriaHab, trabajadores, tipoPago, cliente, habitaciones, reservaciones

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def clients(request):
    myclients = cliente.objects.all().values()
    template = loader.get_template('clients.html')
    context = {
        'myclients': myclients,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mydetails = cliente.objects.get(id=id)
    template = loader.get_template('clientDetail.html')
    context = {
        'mydetails': mydetails,
    }
    return HttpResponse(template.render(context, request))

def reservations(request):
    myreservations = reservaciones.objects.select_related().all()
    template = loader.get_template('reservations.html')
    context = {
        'myreservations': myreservations,
    }
    return HttpResponse(template.render(context, request))

# Mostrar los cuartos
def rooms(request):
    myrooms = habitaciones.objects.select_related().all()
    template = loader.get_template('rooms.html')
    context = {
        'myrooms': myrooms,
    }
    return HttpResponse(template.render(context, request))

# Mostrar los detalles del cuarto seleccionado
def room_detail(request, id):
    myroom_detail = habitaciones.objects.get(id=id)
    template = loader.get_template('roomDetail.html')
    context = {
        'myroom_detail': myroom_detail,
    }
    return HttpResponse(template.render(context, request))

# Mostrar los tipos de cuarto
def roomt(request):
    myroom_types = categoriaHab.objects.select_related().all()
    template = loader.get_template('roomtypes.html')
    context = {
        'myroom_types': myroom_types,
    }
    return HttpResponse(template.render(context, request))


# Mostrar a los Trabajadores

def workers(request):
    myworkers = trabajadores.objects.select_related().all()
    template = loader.get_template('workers.html')
    context = {
        'myworkers': myworkers,
    }
    return HttpResponse(template.render(context, request))

def worker_detail(request, id):
    myworker_detail = trabajadores.objects.get(id=id)
    template = loader.get_template('workerDetail.html')
    context = {
        'myworker_detail': myworker_detail,
    }
    return HttpResponse(template.render(context, request))

def paymenttype(request):
    mypaymenttype = tipoPago.objects.select_related().all()
    template = loader.get_template('payments.html')
    context = {
        'mypaymenttype': mypaymenttype,
    }
    return HttpResponse(template.render(context, request))