import re
from dotenv import load_dotenv
import os
import jwt
import time
import math
import random
from jinja2 import Template


def validate(name, data):
    if name == 'Email':
        regex = '^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$'
        if re.search(regex, data):
            return True
        return False
    elif name == 'Registration Number':
        regex = '^RA[0-9]{13}$'
        if re.search(regex, data):
            return True
        return False
    else:
        if len(data) == 0 or data == '':
            return False
        return True


def checkData(formdata):
    a = 0
    for k, v in formdata.items():
        if not validate(k, v):
            print(k, v)
            a += 1
    if a == 0:
        return True
    return False


def checkotp(encjwt, otp):
    split = encjwt.split()
    load_dotenv()
    secret = os.getenv('SECRET')
    decoded = jwt.decode(split[1], secret, algorithms=["HS256"])
    if decoded['otp'] == otp and (time.time()-decoded['time']) < 300:
        return True
    return False


def createjwt(otp):
    load_dotenv()
    secret = os.getenv('SECRET')
    encoded_jwt = jwt.encode(
        {"otp": otp, "time": time.time()}, secret, algorithm="HS256")
    return encoded_jwt


def createotp():
    otp = ""
    digits = "0123456789"
    for i in range(6):
        otp += digits[math.floor(random.random() * 10)]
    return otp


def emailbody(otp, name, path):
    with open(path) as file_:
        template = Template(file_.read())
        if otp:
            return template.render(name=name, otp=otp)
        return template.render(name=name)
