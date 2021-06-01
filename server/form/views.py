from email.message import EmailMessage
from .utils import checkData, checkotp, createjwt, createotp, emailbody
from django.conf import settings
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from ratelimit.decorators import ratelimit
from .mongo import database_entry
from .backends import CustomPerms
import boto3

client = boto3.client('sesv2', region_name='ap-south-1')


<< << << < HEAD


class DataEntry(APIView):
    """ 

    Class to handle data entry

    """

    permission_classes = [CustomPerms]
    throttle_scope = 'emails'

    def post(self, request, **kwargs):
        formdata = {}
        for i in request.data['fields']:
            formdata[i['name']] = i['data']
        if checkotp(request.headers['Authorization'], request.data['otp']) and checkData(formdata):
            try:
                if database_entry(formdata):
                    response = client.send_email(
                        FromEmailAddress='GitHub Community SRM <community@githubsrm.tech>',
                        Destination={
                            'ToAddresses': [
                                formdata['Email'],
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
                                        'Data': emailbody(formdata['name'], otp=None),
                                        'Charset': 'utf-8'

                                    }
                                }
                            },
                        }
                    )
                return HttpResponse("Data recieved sucessfully", status=201)
            except Exception as e:
                print(e)
                return HttpResponse("Internal Server Error", status=500)
        else:
            return HttpResponse("Bad request", status=400)


class Email(APIView):
    """ 

    Class to handle emails

    """

    throttle_scope = 'emails'

    def post(self, request, **kwargs):

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
                                'Data': emailbody(otp, request.data["name"]),
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
