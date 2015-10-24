from myapp.models import Station
from rest_framework import serializers

class StationSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=10)
	temperature = serializers.CharField(max_length=5)
	lat = serializers.CharField(max_length=10)
	lon = serializers.CharField(max_length=10)
	def create(self, validated_data):
		return Station.objects.create(**validated_data)

#class StationSerializer(serializers.HyperlinkedModelSerializer):
	#class Meta:
		#model = Station
		#fields=('url','name','timestamp','temperature','lat','lon')