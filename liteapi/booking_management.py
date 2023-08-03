# views
from rest_framework.response import Response
from rest_framework.decorators import api_view
import liteapi_client
from liteapi_client.apis.tags import booking_management_api
from . import configuration

with liteapi_client.ApiClient(configuration.configuration) as api_client:
    api_instance = booking_management_api.BookingManagementApi(api_client)


@api_view(['GET'])
def get_bookings_list(request):

    guestId = "FrT56hfty"
    api_response = api_instance.get_bookings_list_by_guestId(guestId)

    return Response(api_response)


@api_view(['GET'])
def retrieved_booking(request):
    bookingId = "a5qlc92p5"
    api_response = api_instance.retrieved_booking(bookingId)
    return Response(api_response)


@api_view(['GET'])
def cancel_booking(request):
    bookingId = "a5qlc92p5"
    api_response = api_instance.cancel_booking(bookingId)

    return Response(api_response)
