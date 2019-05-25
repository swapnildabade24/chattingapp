from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

# Create your views here.

def index(request):
	return render(request, 'chat/index.html', {})

def room(request, room_name):
	return render(request, 'chat/room.html', {
	'room_name_jason': mark_safe(jason_dumps(room_name))
	})
