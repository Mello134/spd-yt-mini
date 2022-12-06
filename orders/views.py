from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet  # класс представления RESTfw

from orders.models import SalesOrder  # наша модель
from orders.serializers import OrderSerializer  # наш сериализатор


def orders_page(request):
    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})


# класс представления OrderView
# унаследовать функции из базового класса django REST - ModelViewSet
class OrderView(ModelViewSet):
    queryset = SalesOrder.objects.all()  # все записи модели
    serializer_class = OrderSerializer


# представление main_app.html
def orders_main_app(request):
    return render(request, 'main_app.html')
