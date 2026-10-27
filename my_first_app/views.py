from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from .models import Author, Profile

# Create your views here.
def myView(request):
    car_list = [
        {"title": "BMW"},
        {"title": "Mazda"},
        {"title": "Toyota"},
        {"title": "Honda"},
        {"title": "Ford"},
        {"title": "Mercedes-Benz"},
        {"title": "Audi"},
        {"title": "Volkswagen"},
        {"title": "Nissan"},
        {"title": "Chevrolet"}
    ]
      
    context = {
        "car_list": car_list
    } 

    return render(request, 'my_first_app/car_list.html', context)

class CarListView(TemplateView):
    template_name = 'my_first_app/car_list.html'

    def get_context_data(self):
        car_list = [
                {"title": "BMW"},
                {"title": "Mazda"},
                {"title": "Toyota"},
                {"title": "Honda"},
        ]
        return {
            "car_list":car_list
        }

def my_test_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")

def author_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    author = Author.objects.get(id=kwargs['id'])
    profile = Profile.objects.get(author_id=kwargs['id'])
    return HttpResponse(f"Author: {author.name} - Website: {profile.website} - Biografia: {profile.biography} ")
