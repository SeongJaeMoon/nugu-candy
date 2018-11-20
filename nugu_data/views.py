from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from nugu_data.models import Calorie 
from nugu_data.firebase import Firebase

'''
- Request
- Param
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
    if status.is_success(code=200):
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# actionName: aw_calorie
# return: Calorie
@api_view(["POST"])
def awCalorie(request):
    if request.data:
        data = request.data
        fb = Firebase()
        params = data.get("action").get("parameters")
        if params is not None:
            fb.set_cal([params.get("FOOD").get("value")])
            result = fb.ret.get("result")[0]
            if result:
                output = {
                    # params.get("FOOD").get("value")
                    "FOOD": result.get("cal").get("name"),
                    "Calorie": result.get("cal").get("kal")
                }
                return Response(data={"version":"1.0.0", 
                                      "resultCode":"OK", 
                                      "output":output},
                                 content_type="application/json")
            else:
                return Response({"resultCode": "10"})    
        else:
            return Response({"resultCode": "404"})    
    else:
        return Response({"resultCode": "404"})


# actionName: aw_bmi
# return: BMI
@api_view(["POST"])
def awBmi(request):
    if request.data:
        return Response({"message": request.data})
    else:
        return Response({"message": "error!"})