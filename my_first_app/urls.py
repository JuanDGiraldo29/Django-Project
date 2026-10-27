from django.http import HttpResponse
from django.urls import path
from .views import my_test_view,author_view,CarListView


urlpatterns = [
   path("listado/", CarListView.as_view()),
   path('detalle/<int:id>', my_test_view),
   path('marcas/<str:brand>', my_test_view),
   path('autor/<int:id>', author_view)
]
