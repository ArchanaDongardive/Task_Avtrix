from django.shortcuts import render
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from app1.serializers import ProductSerailizer
from app1.models import Product
from django.http import JsonResponse
from .resources import ProductResource
from django.contrib import messages
from tablib import Dataset
from rest_framework import status
from rest_framework.response import Response

def simple_upload(request):
    if request.method == 'POST':
        product_resource = ProductResource()
        dataset = Dataset()
        new_product = request.FILES['myfile']
        if not new_product.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, 'upload.html')
        imported_data = dataset.load(new_product.read(),format='xlsx')    

        for data in imported_data:
            value = Product(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
            )
            value.save()
    return render(request,'upload.html')
             

# for getting single data
import io
@api_view(['GET', 'PUT', 'POST'])
def product_api(request, pk):
    try: 
        prod = Product.objects.get(pk=pk)   
    except Product.DoesNotExist: 
        return JsonResponse({'message': 'The product does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        product_serializer =ProductSerailizer(prod) 
        return JsonResponse(product_serializer.data)    

    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerailizer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(product_serializer._errors, status=status.HTTP_400_BAD_REQUEST)
         

    elif request.method == 'PUT': 
        product_data = JSONParser().parse(request) 
        product_serializer = ProductSerailizer(prod, data=product_data, partial=True) 
        if product_serializer.is_valid(): 
            product_serializer.save() 
            return JsonResponse(product_serializer.data) 
        return JsonResponse(product_serializer.errors)

# for getting all data

def common_lines(request):
    bytes_data = request.body
    streamed_data = io.BytesIO(bytes_data)
    python_dict = JSONParser().parse(streamed_data)
    print(python_dict)      # new data
    return python_dict

@api_view(['GET', 'POST','PUT'])
def product_list(request):
    if request.method == 'GET':
        prods = Product.objects.all()
        product_serializer =ProductSerailizer(prods, many=True)
        return Response(product_serializer.data)

    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_serializer =ProductSerailizer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(product_serializer._errors, status=status.HTTP_400_BAD_REQUEST)       

    elif request.method == 'PUT':  
        python_dict = common_lines(request)
        pid = python_dict.get("id")  
        print(python_dict)  
        if pid:
        # print(python_dict)
            prod = Product.objects.get(id=pid)  

        ser = ProductSerailizer(instance=prod, data=python_dict, partial=True)
        if ser.is_valid():
            ser.save()
            return JsonResponse({"msg": "data updated successfully..!"})
        return JsonResponse({"error": ser.errors}) 

# limit page size        
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


class ProdPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10
    

class ProdtList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer
    pagination_class = ProdPagination
   
   



    