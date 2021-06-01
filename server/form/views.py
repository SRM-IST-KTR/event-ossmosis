from email.message import EmailMessage
from .utils import checkData, checkotp, createjwt, createotp, emailbody
from django.conf import settings
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from ratelimit.decorators import ratelimit
from .mongo import database_entry
import smtplib
from .backends import CustomPerms
import boto3
import pathlib

client = boto3.client('sesv2', region_name='ap-south-1')


@ratelimit(key='ip', rate='5/m', method=ratelimit.ALL, block=True)
@api_view(['POST'])
@permission_classes([CustomPerms])
def data(request):
    formdata = {}
    for i in request.data['fields']:
        formdata[i['name']] = i['data']
    if checkotp(request.headers['Authorization'], request.data['otp']) and checkData(formdata):
        try:
            database_entry(formdata)
            response = client.send_email(
                 FromEmailAddress='GitHub Community SRM <community@githubsrm.tech>',
                 Destination={
                     'ToAddresses': [
                         formdata['College Email'],
                     ],

                 },
                 ReplyToAddresses=[
                     'community@githubsrm.tech',
                 ],

                 Content={
                     'Simple': {
                         'Subject': {
                             'Data': 'Conformation | GitHub Community SRM',
                             'Charset': 'utf-8'
                         },
                         'Body': {
                             'Text': {
                                 'Data': 'string',
                                 'Charset': 'utf-8'
                             },

                             'Html': {
                                 'Data': emailbody(formdata['Name'],'confirm_email.html'),
                                 'Charset': 'utf-8'

                             }
                         }
                     },
                 }
            )
            # TODO : base dir
            return HttpResponse("Data recieved sucessfully", status=201)
        except Exception as e:
            print(e)
            return HttpResponse("Internal Server Error", status=500)
    else:
        return HttpResponse("Bad request", status=400)


@ratelimit(key='ip', rate='5/m', method=ratelimit.ALL, block=True)
@api_view(['POST'])
def email(request):
    otp = createotp()
    jwt = createjwt(otp)
    try:
        response = client.send_email(
                FromEmailAddress='GitHub Community SRM <community@githubsrm.tech>',
                Destination={
                    'ToAddresses': [
                        f'{request.data.get("email")}',
                    ],
                    
                },
                ReplyToAddresses=[
                    'community@githubsrm.tech',
                ],

                Content={
                    'Simple': {
                        'Subject': {
                            'Data': 'OTP | GitHub Community SRM',
                            'Charset': 'utf-8'
                        },
                        'Body': {
                            'Text': {
                                'Data': 'string',
                                'Charset': 'utf-8'
                            },

                        'Html': {
                            'Data': emailbody( request.data["name"],'email.html', otp=otp),
                            'Charset': 'utf-8'
                                
                            }
                    }
                },
            }
        )
        return Response({"jwt": jwt}, status=201)
    except Exception as e:
        print(e)
        return HttpResponse("Internal Server Error", status=500)

