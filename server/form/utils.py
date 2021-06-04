import re
from dotenv import load_dotenv
import os
import jwt
import time
import random
from jinja2 import Template
import pathlib


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
    token = encjwt.split()[1]
    load_dotenv()
    secret = os.getenv('SECRET')
    decoded = jwt.decode(token, secret, algorithms=["HS256"])
    if decoded['otp'] == otp and (time.time()-decoded['time']) < 300:
        return True
    return False


def createjwt(otp):
    load_dotenv()
    secret = os.getenv('SECRET')
    encoded_jwt = jwt.encode({
        "otp": otp, "time": time.time()
    }, secret, algorithm="HS256")
    return encoded_jwt


def createotp():
    digits = [1,2,3,4,5,6,7,8,9,0]
    return ''.join(list(map(str, random.choices(digits, k=6))))


def emailbody(name, file, otp=None):
    with open(f'{pathlib.Path.cwd()}/form/{file}') as file_:
        template = Template(file_.read())
        if otp:
            return template.render(name=name, otp=otp)
        return template.render(name=name)
