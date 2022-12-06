from rest_framework.serializers import ModelSerializer  # базовый сериализатор dj rest
from orders.models import SalesOrder  # наш сериализатор


class OrderSerializer(ModelSerializer):  # наш сериализатор
    class Meta:
        model = SalesOrder  # наша модель
        fields = ['amount', 'description']  # поля модели

