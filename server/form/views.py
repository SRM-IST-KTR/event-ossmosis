from email.message import EmailMessage
from .utils import checkData, checkotp, createjwt, createotp#, CustomPerms
from django.conf import settings
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from ratelimit.decorators import ratelimit
from .mongo import database_entry
import smtplib



# Create your views here.
# @permission_classes(CustomPerms)
@ratelimit(key='ip', rate='5/m', method=ratelimit.ALL, block=True)
@api_view(['POST'])
def data(request):
    formdata={}
    print(request.data)
    for i in request.data['fields']:
        formdata[i['name']]=i['data']
    if checkotp(request.headers['Authorization'], request.data['otp']) and checkData(formdata):
        try:
            database_entry(formdata)
            return HttpResponse("Data recieved sucessfully",status=201)
        except:
            return HttpResponse("Internal Server Error",status=500)
    else:
        return HttpResponse("Bad request",status=400)




@ratelimit(key='ip', rate='5/m', method=ratelimit.ALL, block=True)
@api_view(['POST'])
def email(request):
    otp=createotp()
    jwt=createjwt(otp)
    message= EmailMessage()
    try:
        message["Subject"] = 'OTP'
        message["From"] = f'Github Community SRM <{settings.EMAIL_HOST_USER}>'
        message['To'] = request.data["email"]
        message.set_content(f"Your OTP is {otp} which is valid for 5 minutes.")
       
        with smtplib.SMTP_SSL(settings.EMAIL_HOST, 465) as smt:
            smt.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            smt.send_message(message)

        return Response({"jwt":jwt},status=201)
    except Exception as e:
        print(e)
        return HttpResponse("Internal Server Error", status=500)
