from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Event
from .forms import EventForm

def index(request):
    event=Event.objects.all().order_by('-created')
    response = {'event':event}
    return render(request, 'event.html', response)

def event_detail(request,id):
    response={'event':get_object_or_404(Event,pk=id)}
    return render(request, 'detail.html', response)

def event_form(request):
    form = EventForm(request.POST or None, request.FILES or None)
    data = {}
    if request.is_ajax():
        if form.is_valid():
            form.save()
            data['Nama'] = form.cleaned_data.get('Nama')
            data['status'] = 'ok'
            return JsonResponse(data)
            
    response = {
        'form': form,
    }
    return render(request,'Event_Form.html', response) #Return NoteForm ke dalam bentuk html