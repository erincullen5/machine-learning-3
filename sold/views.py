from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from sold.models import SoldData
from sold.serializers import SoldSerializer
from django.shortcuts import render


# Create your views here.

def index(request):

    sold = SoldData.objects.all()[:5]

    context = {
      'sold': sold
    }

    return render(request, 'sold/index.html', context)

# class soldDataView(viewsets.ModelViewSet):
#     queryset = SoldData.objects.all()
#     serializer_class = SoldSerializer

def sold_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    # try:
    #   sold = SoldData.objects.get(pk=pk)
    # except SoldData.DoesNotExist:
    #   return HttpResponse(status=404)
    
    if request.method == 'GET':
      sold = SoldData.objects.all()
      serializer = SoldSerializer(sold, many=True)
      return JsonResponse(serializer.data, safe=False)