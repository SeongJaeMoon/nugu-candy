import os, time
import json
from dateutil.parser import parse
from openpyxl import load_workbook
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Firebase():

    def __init__(self):
        # Initialize firebase.
        cred = credentials.Certificate("foodreet-e783e-firebase-adminsdk-6vdgn-3d49c38eed.json")
        firebase_admin.initialize_app(cred, {
            "databaseURL": "https://foodreet-e783e.firebaseio.com/"
        })
        self.db = db.reference('calories')
        self.bmi = {}
        self.ret = {}
        self.user_info = {}
        self.file_dir = "/Users/moonseongjae/python-worksapce/Nugu/nugu_data/calorie/calorie{}.xlsx"

   
    def save_cal2(self, file):
        if not file:
            raise Exception('NoFileName')
        if not os.path.exists(self.file_dir.format(file)):
            raise Exception('NoSuchFileName')
        try:
            wb = load_workbook(self.file_dir.format(file), read_only=True)
            sheet = wb['calorie']
            for r in sheet.rows:
                category = r[1].value
                name = r[3].value
                quanty = r[4].value
                kal = r[5].value
                tan_g = r[6].value
                dan_g = r[7].value
                ji_g = r[8].value
                dang_g = r[9].value
                na_mg = r[10].value
                chol_mg = r[11].value
                pho_g = r[12].value
                trans_g = r[13].value
                data = {
                    "category": category,
                    "name": name,
                    "quanty": quanty,
                    "kal": kal,
                    "tan_g": tan_g,
                    "dan_g": dan_g,
                    "ji_g": ji_g,
                    "dang_g": dang_g,
                    "na_mg": na_mg,
                    "chol_mg": chol_mg,
                    "pho_g": pho_g,
                    "trans_g": trans_g
                }
                self.db.child("calories").push(data)
            print('--- save done ---')
        except Exception as e:
            print(e)
        finally:
            wb.close()


    def save_cal13(self, file=''):
        if not os.path.exists(self.file_dir.format(FILE)):
            raise Exception('NoSuchFileName')
        try:
            wb = load_workbook(self.file_dir.format(FILE), read_only=True)
            sheet = wb['calorie']
            for r in sheet.rows:
                category = r[1].value
                name = r[2].value
                quanty = r[3].value
                kal = r[4].value
                tan_g = r[5].value
                dan_g = r[6].value
                ji_g = r[7].value
                dang_g = r[8].value
                na_mg = r[9].value
                chol_mg = r[10].value
                pho_g = r[11].value
                trans_g = r[12].value
                data = {
                    "category": category,
                    "name": name,
                    "quanty": quanty,
                    "kal": kal,
                    "tan_g": tan_g,
                    "dan_g": dan_g,
                    "ji_g": ji_g,
                    "dang_g": dang_g,
                    "na_mg": na_mg,
                    "chol_mg": chol_mg,
                    "pho_g": pho_g,
                    "trans_g": trans_g
                }
                db.child("calories").push(data, self.user['idToken'])
        except Exception as e:
            print(e)
        finally:
            wb.close()


    def edit_distance(self, s1, s2):
        l1, l2 = len(s1), len(s2)
        if l2 > l1:
            return self.edit_distance(s2, s1)
        if l2 is 0:
            return l1
        prev_row = list(range(l2 + 1))
        current_row = [0] * (l2 + 1)
        for i, c1 in enumerate(s1):
            current_row[0] = i + 1
            for j, c2 in enumerate(s2):
                d_ins = current_row[j] + 1
                d_del = prev_row[j + 1] + 1
                d_sub = prev_row[j] + (1 if c1 != c2 else 0)
                current_row[j + 1] = min(d_ins, d_del, d_sub)
            prev_row[:] = current_row[:]
        return prev_row[-1]


    def set_cal(self, name):
        '''
        Usage
            Get calroie list from Firebase and initialize self.ret.
        Param
            name: User Speech(Entities).
        '''
        try:
            save_distance = [] # temp var
            distance = [] # temp var
            data = self.db.get()
            if data is not None:
                # Loop for entities list.
                for n in name:
                    for d in data.values():
                        if n in d.get('name'):
                            temp = {
                                "category": d.get('category'),
                                "name": d.get('name'), 
                                "quanty": d.get('quanty'),
                                "kal": d.get('kal'),
                                "tan_g": d.get('tan_g'),
                                "dan_g": d.get('dan_g'),
                                "ji_g": d.get('ji_g'),
                                "dang_g": d.get('dang_g'),
                                "na_mg": d.get('na_mg'),
                                "chol_mg": d.get('chol_mg'),
                                "pho_g": d.get('pho_g'),
                                "trans_g": d.get('trans_g')   
                            }
                            save_distance.append({'cal':temp})
                    # Calculate for edit_distance.
                    distance.append(min(save_distance, key = lambda s: self.edit_distance(n, s.get("cal").get("name"))))
            if distance:
                self.ret['result'] = distance
        except Exception as e:
            print(e)


    def get_percent(self):
        
        _json = json.loads(str(self.ret).replace("\'", '"'))

        kal_sum, quanty_sum, tan_g_sum, dan_g_sum, ji_g_sum, \
        dang_g_sum, na_mg_sum, chol_mg_sum, pho_g_sum, trans_g_sum = \
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        
        # cn_list = []
        for t in _json.get('result'):
            # cn_list.append(t.get('cal').get('name'))
            # cn_list.append(t.get('cal').get('category'))
            kal_sum += int(t.get('cal').get('kal'))
            quanty_sum += int(t.get('cal').get('quanty'))
            tan_g_sum += int(t.get('cal').get('tan_g'))
            dan_g_sum += int(t.get('cal').get('dan_g'))
            ji_g_sum += int(t.get('cal').get('ji_g'))
            dang_g_sum += int(t.get('cal').get('dang_g'))
            na_mg_sum += int(t.get('cal').get('na_mg'))
            chol_mg_sum += int(t.get('cal').get('chol_mg'))
            pho_g_sum += int(t.get('cal').get('pho_g'))

        ret_list = [kal_sum, quanty_sum, tan_g_sum, dan_g_sum, ji_g_sum, \
                    dang_g_sum, na_mg_sum, chol_mg_sum, pho_g_sum, trans_g_sum]

        print(ret_list)


    def set_bmi(self, weight_kg, height_cm):
        # BMI = 몸무게(kg) / 키(m) * 키(m)
        temp_bmi = round(weight_kg / (height_cm * height_cm) * 10000, 2)
        if temp_bmi < 18.5:
            ret = "저체중"
        elif temp_bmi > 18.5 and temp_bmi < 24.9:
            ret = "정상체중"
        elif temp_bmi > 25 and temp_bmi < 29.9:
            ret = "과체중"
        else:
            ret = "비만"
        self.bmi[str(parse(time.strftime('%Y-%m-%d')))] = [temp_bmi, ret]
    
   
    def set_energe(self):    
       heigt_cm = self.user_info.get('height')
       weight_kg = self.user_info.get('weight')
       age = self.user_info.get('age')
       gender = self.user_info.get('gender')
       pa = self.user_info.get('pa')
       
       if (heigt_cm and weight_kg and age and gender) is not None:
            if age == 1:
               energe = round(662 - (9.53 * age) + pa * ((15.91 * weight_kg) + (539.6 * height_cm) / 100))
            else:
               energe = round(354 - (6.91 * age) + pa * ((9.36 * weight_kg) + (726 * height_cm) / 100))
            
            return energe
       else:
           return None


    # def cal_clt(self):


if __name__ == "__main__":
    start = time.time()

    print("--- %s seconds---" % (time.time() - start))
