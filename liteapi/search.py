# views
from rest_framework.response import Response
from rest_framework.decorators import api_view
import liteapi_client
from liteapi_client.apis.tags import search_api
from . import configuration



with liteapi_client.ApiClient(configuration.configuration) as api_client:
    api_instance = search_api.SearchApi(api_client)


@api_view(['GET'])
def get_minimum_rates(request):
    hotelIds =["lp3803c", "lp1f982", "lp19b70","lp19e75"]
    checkin = "2023-11-15"
    checkout = "2023-11-16"
    currency = "USD"
    guestNationality = "US"
    adults = 1

    api_response = api_instance.get_minimum_rates(hotelIds=hotelIds, checkin=checkin, checkout=checkout,
                                                       currency=currency, guestNationality=guestNationality, adults=adults)
    
    # Optional values
    children = [12,9]
    guestId = "traveler1"

    #api_response = api_instance.get_minimum_rates(hotelIds=hotelIds, checkin=checkin, checkout=checkout,
    #                                                  currency=currency, guestNationality=guestNationality, adults=adults, children=children, guestId=guestId)
    
    return Response(api_response)



@api_view(['GET'])
def get_full_rates(request):
    hotelIds =["lp3803c", "lp1f982", "lp19b70","lp19e75"]
    checkin = "2023-11-15"
    checkout = "2023-11-16"
    currency = "USD"
    guestNationality = "US"
    adults = 1

    api_response = api_instance.get_full_rates(hotelIds=hotelIds, checkin=checkin, checkout=checkout,
                                                       currency=currency, guestNationality=guestNationality, adults=adults)
    
    # Optional values
    children = [12,9]
    guestId = "traveler1"

    #api_response = api_instance.get_full_rates(hotelIds=hotelIds, checkin=checkin, checkout=checkout,
    #                                                  currency=currency, guestNationality=guestNationality, adults=adults, children=children, guestId=guestId)
    
    return Response(api_response)
