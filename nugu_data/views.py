from rest_framework.decorators import api_view
from rest_framework.response import Response

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
        "actionName": "aw_calorie",
        "parameters": {
            "FOOD": {
                "type": "FOODS",
                "value": "치킨"
            }
        }
    },
    "context": {
        "accessToken": "{{string}}",
        "device": {
            "type": "{{string}}",
            "state": {
                "KE"Y: "VALUE"
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

@api_view()
def index(request):
    return Response({"message": "Candy Diary!"})


@api_view(["GET"])
def health(request):
    if request.status_code == 200:
        return Response({"status":"OK"})
    else:
        return Response({"status":"error " + request.status_code})


# actionName: aw_calorie
# return: Calorie
@api_view(["POST"])
def aw_calorie(request):
    if request.data:
        data = request.data
        fb = Firebase()
        params = data.get("action").get("parameters")
        if params is not None:
            fb.set_cal([params.get("FOOD").get("value")])
            result = fb.ret.get("result").get("cal").get("kal")
            if result is not None:
                output = {
                    "FOOD":fb.ret.get("result").get("cal").get("name"),
                    "Calorie":result
                }
                return Response({"resultCode":"OK", "output":output})
            else:
                return Response({"resultCode": "10"})    
        else:
            return Response({"resultCode": "404"})    
    else:
        return Response({"resultCode": "404"})

# actionName: aw_bmi
# return: BMI
@api_view(["POST"])
def aw_bmi(request):
    if request.data:
        return Response({"message": request.data})
    else:
        request.state
        return Response({"message": "error!"})