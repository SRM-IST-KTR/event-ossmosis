from rest_framework.permissions import BasePermission
import re
import requests
from dotenv import load_dotenv
import os
import jwt
import time
import math
import random
from rest_framework.decorators import permission_classes

def validate(name,data):
    if name=='Email':
        regex = '^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$'
        if re.search(regex, data):
            return True
        return False
    elif name=='Registration Number':
        regex = '^RA[0-9]{13}$'
        if re.search(regex, data):
            return True
        return False
    else:
        if len(data)==0 or data=='':
            return False
        return True

def checkData(formdata):
    print(formdata)
    a=0
    for k,v in formdata.items():
        if not validate(k,v):
            print(k,v)
            a+=1
    if a==0:
        return True
    return False


# Create your views here.
# def checkToken(token):
#     url = "https://www.google.com/recaptcha/api/siteverify"
#     load_dotenv()
#     secret_key = os.getenv('SECRET_KEY')
#     payload = {
#         'secret': secret_key,
#         'response': token,
#     }
#     response = requests.post(url, data=payload)
#     return response.json()["score"] >= 0.5 and response.json()["success"]

def checkotp(encjwt,otp):
    split=encjwt.split()
    load_dotenv()
    secret = os.getenv('SECRET')
    decoded=jwt.decode(split[1], secret, algorithms=["HS256"])
    if decoded['otp'] == otp and (time.time()-decoded['time']) < 300:
        return True
    return False

def createjwt(otp):
    load_dotenv()
    secret = os.getenv('SECRET')
    encoded_jwt = jwt.encode({"otp":otp,"time":time.time()}, secret, algorithm="HS256")
    return encoded_jwt

def createotp():
    otp=""
    digits = "0123456789"
    for i in range(6):
        otp += digits[math.floor(random.random() * 10)]
    return otp


# class CustomPerms(BasePermission):
#     def has_permission(self, request,):
#         url = "https://www.google.com/recaptcha/api/siteverify"
#         load_dotenv()
#         secret_key = os.getenv('SECRET_KEY')
#         payload = {
#             'secret': secret_key,
#             'response': token,
#         }
#         response = request.post(url, data=payload)
#         return response.json()["score"] >= 0.5 and response.json()["success"] and request.user
