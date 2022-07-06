from django.shortcuts import render
# Add the following import
from django.views.generic.edit import CreateView
from .models import Turtle

# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')



def turtles_index(request):
    turtles = Turtle.objects.all()
    return render(request, 'turtles/index.html', { 'turtles': turtles })



def turtles_detail(request, turtle_id):
    turtle = Turtle.objects.get(id=turtle_id)
    return render(request, 'turtles/detail.html', { 'turtle': turtle })



class TurtleCreate(CreateView):
    model = Turtle
    fields = '__all__'
    success_url = '/turtles/'


class TurtleUpdate(UpdateView):
    model = Turtle
    fields = ['breed', 'description', 'age']

class TurtleDelete(DeleteView):
    model = Turtle
    success_url = '/turtles/'