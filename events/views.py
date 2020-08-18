# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.shortcuts import render
from events.models import Events
# Create your views here.
def event(request):
    all_events = Events.objects.all()
    get_event_types = Events.objects.only('event_type')
    event_arr = []
    if request.GET.get('event_type') == "all":
        all_events = Events.objects.all()
    else:
        all_events = Events.objects.filter(event_type__icontains=request.GET.get('event_type'))

    for i in all_events:
        event_sub_arr = {}
        event_sub_arr['title'] = i.event_name
        start_date = datetime.strptime(str(i.start_date.date()), "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")
        end_date = datetime.strptime(str(i.end_date.date()), "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")
        event_sub_arr['start'] = start_date
        event_sub_arr['end'] = end_date
        event_arr.append(event_sub_arr)
    return HttpResponse(json.dumps(event_arr))

    
        

    context = {
        "events": all_events,
        "get_event_types": get_event_types,

    }
    return render(request, 'events/calendar.html', context)