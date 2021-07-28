
from django.http import HttpResponse
from django.http.response import Http404, JsonResponse
from django.shortcuts import render
from .models import Product

# Create your views here.

def home_view(request):
    #return HttpResponse("<h1>hi there</h1>")
    context={"name": "nitta"}
    return render(request, "home.html", context)

def product_detail_view(request, pk):
    try:
        obj= Product.objects.get(pk=pk)
    except:
        raise Http404
    #return HttpResponse(f"product id is {obj.pk}")
    return render(request, 'details.html', {"object": obj} )

def product_api_detail_view(request, pk):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "not found"})
    return JsonResponse({"id":pk})