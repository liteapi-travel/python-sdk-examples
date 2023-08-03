from django.urls import include, path

from . import views
from . import static_data_api 
from . import guests 
from . import search 
from . import book
from . import booking_management
 
app_name='liteapi'

urlpatterns = [

    #Static Data
    path('staticData/cities',static_data_api.get_cities , name='get_cities'),
    path('staticData/countries',static_data_api.get_countries , name='get_countries'),
    path('staticData/currencies',static_data_api.get_currencies , name='get_currencies'),
    path('staticData/hotels',static_data_api.get_hotels , name='get_hotels'),
    path('staticData/hotelDetails',static_data_api.get_hotel_details , name='get_hotel_details'),
    path('staticData/iataCodes',static_data_api.get_iata_codes , name='get_iata_codes'),

    #Guest and loyalty
    path('guests',guests.get_guests , name='get_guests'),

    #Search
    path('search/minRates',search.get_minimum_rates , name='get_minimum_rates'),
    path('search/fullRates',search.get_full_rates , name='get_full_rates'),

    #Book
    path('book/prebook',book.prebook , name='prebook'),
    path('book/book',book.book , name='book'),

    #Booking management
    path('bookingManagement/bookingsList',booking_management.get_bookings_list , name='get_bookings_list'),
    path('bookingManagement/retrieve',booking_management.retrieved_booking , name='retrieved_booking'),
    path('bookingManagement/cancel',booking_management.cancel_booking , name='cancel_booking'),

]