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

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


@login_required
def turtles_index(request):
    turtles = Turtle.objects.filter(user=request.user)
    return render(request, 'turtles/index.html', { 'turtles': turtles })


@login_required
def turtles_detail(request, turtle_id):
    turtle = Turtle.objects.get(id=turtle_id)
    toys_turtle_doesnt_have = Toy.objects.exclude(id__in = turtle.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'turtles/detail.html', {
        'turtle': turtle, 'feeding_form': feeding_form,
        'toys': toys_turtle_doesnt_have
    })
@login_required
def add_feeding(request, turtle_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.turtle_id = turtle_id
        new_feeding.save()
    return redirect('detail', turtle_id=turtle_id)
@login_required
def assoc_toy(request, turtle_id, toy_id):
    Turtle.objects.get(id=turtle_id).toys.add(toy_id)
    return redirect('detail', turtle_id=turtle_id)
@login_required
def assoc_toy_delete(request, turtle_id, toy_id):
    Turtle.objects.get(id=turtle_id).toys.remove(toy_id)
    return redirect('detail', turtle_id=turtle_id)
# signup
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class TurtleCreate(LoginRequiredMixin, CreateView):
    model = Turtle
    fields = ['name', 'breed', 'description', 'age']
    success_url = '/turtles/'
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  
    # Let the CreateView do its job as usual
        return super().form_valid(form)


class TurtleUpdate(LoginRequiredMixin, UpdateView):
    model = Turtle
    fields = ['breed', 'description', 'age']

class TurtleDelete(LoginRequiredMixin, DeleteView):
    model = Turtle
    success_url = '/turtles/'

class ToyList(LoginRequiredMixin, ListView):
    model = Toy
    template_name = 'toys/index.html'

class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy
    template_name = 'toys/detail.html'

class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields = ['name', 'color']


class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ['name', 'color']


class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = '/toys/'
