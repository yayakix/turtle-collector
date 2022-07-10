from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Turtle, Toy

# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# Add the following import
from django.http import HttpResponse

from .forms import FeedingForm

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
    toys_turtle_doesnt_have = Toy.objects.exclude(id__in = turtle.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'turtles/detail.html', {
        'turtle': turtle, 'feeding_form': feeding_form,
        'toys': toys_turtle_doesnt_have
    })

def add_feeding(request, turtle_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.turtle_id = turtle_id
        new_feeding.save()
    return redirect('detail', turtle_id=turtle_id)

def assoc_toy(request, turtle_id, toy_id):
    Turtle.objects.get(id=turtle_id).toys.add(toy_id)
    return redirect('detail', turtle_id=turtle_id)

def assoc_toy_delete(request, turtle_id, toy_id):
    Turtle.objects.get(id=turtle_id).toys.remove(toy_id)
    return redirect('detail', turtle_id=turtle_id)

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

class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'

class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'

class ToyCreate(CreateView):
    model = Toy
    fields = ['name', 'color']


class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']


class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'
