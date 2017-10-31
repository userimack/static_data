from django.shortcuts import render
from django.core.paginator import Paginator
from web.models import CityMapping
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from web import helper 
import traceback


def __common_url_params(request):
    page = request.GET.get("page", 0)
    status = request.GET.get("status", 0)
    supplier = request.GET.get("supplier", "")
    return "page="+str(page)+"&status="+str(status) + "&supplier="+supplier

def home(request):
    return render(request, "web/home.html")


def cities(request):
    status=request.GET.get("status", 0)
    city_list = CityMapping.objects.filter(status=status)
    supplier = request.GET.get("supplier", None)
    city_list = city_list.filter(supplier=supplier) if supplier else city_list 
    paginator = Paginator(list(city_list), 25)
    page = request.GET.get('page', 0)
    try:
        cities = paginator.page(page)
    except Exception as e:
        cities = paginator.page(1)
    except EmptyPage:
        cities = paginator.page(paginator.num_pages)
    return render(request, 'web/cities_list.html', {'cities': cities, "url_params": __common_url_params(request)})

def city_mappings(request, pk):
    try:
        obj = CityMapping.objects.get(id = pk)
        cities = helper.process_city(obj)
        return render(request, 'web/city_mappings_form.html', {'cities': cities, "city_mapping": obj, "url_params": __common_url_params(request)})    
    except Exception as e:    
        print(str(e))
        messages.error(request, "Invalid Request.")
        return HttpResponseRedirect("/")

def update_city_status(request, pk, status, city_code=None):
    try:
        obj = CityMapping.objects.get(id = pk)
        obj.status = status
        obj.save()
        messages.success(request, "Successfully Mapped.")
        endpoint = "/city/mappings/?"+__common_url_params(request)
        return HttpResponseRedirect(endpoint)    
    except Exception as e:    
        traceback.print_exc()
        print(str(e))
        messages.error(request, "Invalid Request.")
        endpoint = "/city/mappings/?"+__common_url_params(request)
        return HttpResponseRedirect(endpoint)
    return city_mappings(request, cmid)