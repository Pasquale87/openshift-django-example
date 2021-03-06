# Create your views here.

from myapp.models import Station
from rest_framework import viewsets
from django.shortcuts import render_to_response
from django.template import RequestContext
from myapp.serializers import StationSerializer
import requests
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#from blog.models import Entry

class StationViewSet(viewsets.ModelViewSet):
	queryset = Station.objects.all()
	serializer_class = StationSerializer
	
#@api_view(['GET', 'POST'])
@csrf_exempt
def login_user(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'],  password=request.POST['password'])
		if user is not None:
			login(request, user)
			#Add a new record
			#temp=Station.objects.create(name=request.POST['name'], timestamp=request.POST['timestamp'], temperature=request.POST['temperature'], lat=request.POST['lat'], lon=request.POST['lon'])
			#Update a record
			#t = Station.objects.get(id=0)
			t = Station.objects.order_by('id')[0]
			t.name=request.POST['name']			
			t.timestamp=request.POST['timestamp']
			t.temperature=request.POST['temperature']
			t.lat=request.POST['lat']
			t.lon=request.POST['lon']
			t.save()
			#entry.Station.add(temp)
			return HttpResponse("Logged In-POSTED")
		else:
			return HttpResponse(request.POST['username'])
	else:
		return HttpResponse("Che vuoi")
	
#Restituisce solamente i valori dell'ultimo record 
@api_view(['GET', 'POST'])
def index(request):
	if request.method == 'GET':
		queryset = Station.objects.order_by('-id')[0]
		serializer_class = StationSerializer(queryset)
		return Response(serializer_class.data)
	#return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	#r=request.get('http://192.168.1.3:8000/station/',auth=('username','password'))
	#result = r.text
	#output = json.loads(result)
	#count = output['count']
	#count=int(count)-1
	
	#name=output['results'][count]['name']
	#temperature=output['results'][count]['temperature']
	#lat=output['results'][count]['lat']
	#lon=output['results'][count]['lon']
	
#Rikiama get.html che ad intervalli regolari rikiama index per dare i valori aggiornati dell'ultimo
#@csrf_exempt
def home(request):
	stat = Station.objects.order_by('-id')[0]
	temperature = stat.temperature
	name = stat.name
	lat = stat.lat
	lon = stat.lon
	
	return render_to_response('get.html',{'name':name,'temperature':temperature,'lat':lat,'lon':lon},context_instance=RequestContext(request))
	#return render(request,'myapp/index.html',context)