# from django.http import HttpResponse
from django.shortcuts import redirect, render

from base.forms import RoomForm

from .models import Room

# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Python Room'},
#     {'id': 2, 'name': 'JAVA Room'},
#     {'id': 3, 'name': 'Frontend Room'},
# ]


def home(request):
    # return HttpResponse('Hello World')
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    # return HttpResponse('Hello Room')
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)
