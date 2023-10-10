from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products
from .serializers import ProductsSerializers


@api_view(['GET', 'POST'])
def item_list(request):
    if request.method == 'GET':
        items = Products.objects.all()
        serializer = ProductsSerializers(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)






