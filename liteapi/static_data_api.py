# views
from rest_framework.response import Response
from rest_framework.decorators import api_view
import liteapi_client
from liteapi_client.apis.tags import static_data_api
from . import configuration

with liteapi_client.ApiClient(configuration.configuration) as api_client:
    api_instance = static_data_api.StaticDataApi(api_client)


@api_view(['GET'])
def get_cities(request):
    countryCode = "US",
    api_response = api_instance.get_cities(countryCode)
    return Response(api_response)


@api_view(['GET'])
def get_countries(request):
    api_response = api_instance.get_countries()
    return Response(api_response)


@api_view(['GET'])
def get_currencies(request):
    api_response = api_instance.get_currencies()
    return Response(api_response)


@api_view(['GET'])
def get_hotels(request):
    countryCode = "IT"
    cityName = "Rome"
    # Optional values
    offset = 10
    limit = 10
    longitude = "-115.16988"
    latitude = "36.12510"
    distance = 1000
    #api_response = api_instance.get_hotels(countryCode=countryCode, cityName=cityName,
    #                                       offset=offset, limit=limit, longitude=longitude, latitude=latitude, distance=distance)
   
    api_response = api_instance.get_hotels(countryCode=countryCode, cityName=cityName)
    return Response(api_response)


@api_view(['GET'])
def get_hotel_details(request):
    hotelId =  "lp24373"
    api_response = api_instance.get_hotel_details(hotelId)
    return Response(api_response)


@api_view(['GET'])
def get_iata_codes(request):
    api_response = api_instance.get_iata_codes()
    return Response(api_response)