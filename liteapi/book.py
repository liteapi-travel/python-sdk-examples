# views
from rest_framework.response import Response
from rest_framework.decorators import api_view
import liteapi_client
from liteapi_client.apis.tags import book_api
from . import configuration

with liteapi_client.ApiClient(configuration.configuration) as api_client:
    api_instance = book_api.BookApi(api_client)


@api_view(['GET'])
def prebook(request):

    rateId = "NRYDGOBQGNRXYMRQGIZS2MJRFUYTK7BSGAZDGLJRGEWTCNT4GF6HYVKTPRDVKM2UKFHFUUSHJEZUGR2OJJKEMWKZKRAU2QSRI5AVSQ2HJZFFQSCBGNKEGTKSK5GDIWSEJFHFUVKHIVNEIR2OKJIUYNCZKY3E2QZXI5AVEVCLJZNFSRZULFJUOVSLKR6FKU2EPR6HYOBVFYYTA7D4IJHXYNJXHA3TC7BR"
    api_response = api_instance.prebook(rateId)
    
    return Response(api_response)


@api_view(['GET'])
def book(request):
    prebookId = "Qh1l16Tiu"
    guestFirstName = "Kim"
    guestLastName = "James"
    guestEmail = "test@nlite.ml"

    holderName = "Kim James"
    paymentMethod = "CREDIT_CARD"
    cardNumber = "4242424242424242"
    expireMonth = "11"
    expireYear = "23"
    cvc = "123"

    api_response = api_instance.book(prebookId=prebookId, guestFirstName=guestFirstName, guestLastName=guestLastName, guestEmail=guestEmail,
                                     holderName=holderName, paymentMethod=paymentMethod, cardNumber=cardNumber, expireMonth=expireMonth, 
                                     expireYear=expireYear, cvc=cvc)


    #token = "NOJJK&!EMWKZKRAUN34L10#%!RAU"
    #api_response = api_instance.book(prebookId=prebookId, guestFirstName=guestFirstName, guestLastName=guestLastName, guestEmail=guestEmail,
    #                                 holderName=holderName, paymentMethod=paymentMethod, token=token)


    return Response(api_response)
