# views
from rest_framework.response import Response
from rest_framework.decorators import api_view
import liteapi_client
from liteapi_client.apis.tags import guest_and_loyalty_api
from . import configuration

with liteapi_client.ApiClient(configuration.configuration) as api_client:
    api_instance = guest_and_loyalty_api.GuestAndLoyaltyApi(api_client)

@api_view(['GET'])
def get_guests(request):
    email = "johndoe@nlite.ml"
    api_response = api_instance.get_guests(email)
    return Response(api_response)