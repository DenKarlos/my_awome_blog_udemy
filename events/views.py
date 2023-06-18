from django.shortcuts import render

from events.models import Event


def index(request):
    context = {'events': Event.objects.all(),}
    return render(request, 'events/index.html', context)
