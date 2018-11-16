from rest_framework import serializers
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

from nugu_data.models import Calorie 
from nugu_data.firebase import Firebase

'''
- Request
Param
    FOOD

POST /action_name HTTP/1.1
Accept: application/json, */*
Content-Length: 400
Content-Type: application/json
Host: builder.open.co.kr
Authorization: token TOKEN_STRING

{
    "version": "2.0",
    "action": {
        "actionName": "{{string}}",
        "parameters": {
            KEY: {
                "type": "{{string}}",
                "value": VALUE
            }
        }
    }
    "context": {
        "accessToken": "{{string}}",
        "device": {
            "type": "{{string}}",
            "state": {
                KEY: VALUE
            }
        }
    }
}

- Response
{
    "version": "2.0",
    "resultCode": "{{string}}",
    "output": {
        "datetime": "오늘",
        KEY1: VALUE1,
        KEY2: VALUE2,
        ...
    }
}
'''

# actionName: aw_calorie

@api_view(["POST"])
def calroie(request):
    if request.data:
        print(request.data)
        return Response({"message": "Hello, world!"})
    else:
        return Response({"message": "error!"})

