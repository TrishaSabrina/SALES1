from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sales
from .serializers import SalesSerializers


@api_view(['GET', 'POST'])
def item_list(request):
    if request.method == 'GET':
        items = Sales.objects.all()
        serializer = SalesSerializers(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        sales_data = request.data.get('sales', []) 
        serializer = SalesSerializers(data=sales_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400) 





@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, pk):
    try:
        item = Sales.objects.get(id=pk)
    except Sales.DoesNotExist:
        return Response({"error": "Item not found"}, status=404)

    if request.method == 'GET':
        serializer = SalesSerializers(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SalesSerializers(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)