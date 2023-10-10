from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customers
from .serializers import CustomersSerializers


@api_view(['GET', 'POST'])
def item_list(request):
    if request.method == 'GET':
        items = Customers.objects.all()
        serializer = CustomersSerializers(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomersSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

