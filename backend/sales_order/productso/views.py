from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Productso
from .serializers import ProductsoSerializers

@api_view(['GET', 'POST'])
def item_list(request):
    if request.method == 'GET':
        items = Productso.objects.all()
        serializer = ProductsoSerializers(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        products_data = request.data.get('products', [])  # Retrieve the array of products (default to empty list)
        serializer = ProductsoSerializers(data=products_data, many=True)  # Serialize multiple products
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    





@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, pk):
    try:
        item = Productso.objects.get(id=pk)
    except Productso.DoesNotExist:
        return Response({"error": "Item not found"}, status=404)

    if request.method == 'GET':
        serializer = ProductsoSerializers(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductsoSerializers(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)
