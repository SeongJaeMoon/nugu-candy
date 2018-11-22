from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from nugu_data.models import Calorie 
from nugu_data.firebase import Firebase


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
# Request Param: FOOD
# return: Calorie
@api_view(["POST"])
def awCalorie(request):
    if request.data:
        fb = Firebase()
        data = request.data
        params = data.get("action").get("parameters")
        if params is not None:
            fb.set_cal(params.get("FOOD").get("value"))
            try:
                result = fb.ret.get("result")
            except (ValueError, TypeError):
                return Response({"resultCode": "10"})    
            
            if result is None:
                return Response({"resultCode": "10"})    

            if result:
                na_mg = result.get("content")
                if na_mg is not None:
                    content = result.get("content")
                else:
                    content = ""
                output = {
                    "FOOD": params.get("FOOD").get("value"),
                    "FOODREET": result.get("cal").get("name"),
                    "Calorie": result.get("cal").get("kal"),
                    "Content": content
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


# actionName: awBmi
# Request Param: weight_kg, height_cm
# return: BMI
@api_view(["POST"])
def awBmi(request):
    if request.data:
        fb = Firebase()
        data = request.data
        params = data.get("action").get("parameters")
        if params is not None:
            weight = params.get("WEIGHTS").get("value")
            height = params.get("HEIGHTS").get("value")
            fb.set_bmi(weight_kg=weight, 
                       height_cm=height)    
            if fb.bmi:
                if fb.bmi.get("bmi") is None:
                    return Response({"resultCode": "11"}) # 키 or 몸무게 정보 부족
                output = {
                    "WEIGHT": params.get("WEIGHT").get("value"),
                    "HEIGHT": params.get("HEIGHT").get("value"),
                    "WEIGHTS": weight,
                    "HEIGHTS": height,
                    "bmi": fb.bmi.get("bmi")[0],
                    "content": fb.bmi.get("bmi")[1]
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


# actionName: awClt
# Request Param: weight_kg, height_cm, age, gender, _mins, _cals, _type
# return: Energy
@api_view(["POST"])
def awClt(request):
    if request.data:
        fb = Firebase()
        data = request.data
        params = data.get("action").get("parameters")
        if params is not None:
            weight = params.get("WS").get("value")
            height = params.get("HS").get("value")
            age = params.get("AS").get("value")
            gender = params.get("GS").get("value")
            _mins = params.get("MINS").get("value")
            _cals = params.get("CALS").get("value")
            _type = params.get("TYPE").get("value")
            fb.user_info['height'] = height
            fb.user_info['weight'] = weight
            fb.user_info['age'] = age
            
            if gender == "남성" or gender == "남자":
                fb.user_info['gender'] = 1
            elif gender == "여성" or gender == "여자":
                fb.user_info['gender'] = 0
            else:
                return Response({"resultCode": "12"}) # 성별 정보 부족
            
            if mins is not None:
                result = fb.cal_clt(_type=_type, _mins=_mins)
            elif clas is not None:
                result = fb.cal_clt(_type=_type, _cals=_cals)
            else:
                return Response({"resultCode": "13"}) # 시간 or 칼로리 정보 부족
            
            if result in [11, 12, 13, 14]:
                return Response({"resultCode": str(result)}) # 정보 부족

            if result:
                output = {
                    "WEIGHT" :params.get("WEIGHT").get("value"),
                    "HEIGHT": params.get("WEIGHT").get("value"),
                    "AGE": params.get("AGE").get("value"),
                    "GENDER": params.get("GENDER").get("value"),
                    "WEIGHTS": weight,
                    "HEIGHTS": height,
                    "AGES": age,
                    "GENDERS": gender,
                    "_mins": _mins,
                    "_cals": _cals,
                    "_type": _type,
                    "content": result
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


# actionName: awEnergy
# Request Param: weight_kg, height_cm, age, gender, (pa)
# return: Daily Energy
@api_view(["POST"])
def awEnergy(request):
    if request.data:
        fb = Firebase()
        data = request.data
        params = data.get("action").get("parameters")
        if params is not None:
            weight = params.get("WS").get("value")
            height = params.get("HS").get("value")
            age = params.get("AGES").get("value")
            gender = params.get("GENDERS").get("value")
            fb.user_info['height'] = height
            fb.user_info['weight'] = weight
            fb.user_info['age'] = age

            if gender == "남성" or gender == "남자":
                fb.user_info['gender'] = 1
                fb.user_info['pa'] = fb.m_pa_list[1]
            elif gender == "여성" or gender == "여자":
                fb.user_info['gender'] = 0
                fb.user_info['pa'] = fb.fm_pa_list[1]
            else:
                return Response({"resultCode": "12"}) # 성별 정보 부족
            
            output = {
                "W" :params.get("W").get("value"),
                "H": params.get("H").get("value"),
                "AGE": params.get("AGE").get("value"),
                "GENDER": params.get("GENDER").get("value"),
                "WS": weight,
                "HS": height,
                "AGES": age,
                "GENDERS": gender,
                "energy": str(fb.get_energy())+"kcal",
                "major_tan": fb.major_nutrients().get("tan_g"),
                "major_dan": fb.major_nutrients().get("dan_g"),
                "major_ji": fb.major_nutrients().get("ji_g")
            }
            return Response(data={"version":"1.0.0", 
                                  "resultCode":"OK", 
                                  "output":output},
                            content_type="application/json")    
        else:
            return Response({"resultCode": "404"})    
    else:
        return Response({"resultCode": "404"})


