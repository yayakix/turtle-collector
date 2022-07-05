from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')
def about(request):
  return render(request, 'about.html')

class Turtle:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

turtles = [
  Turtle('Lolo', 'tabby', 'foul little demon', 3),
  Turtle('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Turtle('Raven', 'black tripod', '3 legged cat', 4),
  Turtle('Lolo', 'tabby', 'foul little demon', 3),
  Turtle('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Turtle('Raven', 'black tripod', '3 legged cat', 4)
]

def turtles_index(request):
  return render(request, 'turtles/index.html', { 'turtles': turtles })