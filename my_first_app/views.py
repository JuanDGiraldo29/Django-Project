from django.shortcuts import render

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

    return render(request, 'my_First_App/car_list.html', context)