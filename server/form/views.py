from .utils import checkData, checkotp, createjwt, createotp, emailbody
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from .mongo import database_entry
from .backends import CustomPerms
import boto3

client = boto3.client('sesv2', region_name='ap-south-1')


class DataEntry(APIView):
    """ 

    Class to handle data entry

    """

    permission_classes = [CustomPerms]
    throttle_scope = 'emails'

    def post(self, request, **kwargs):        
        if checkotp(request.headers['Authorization'], request.data['otp']) and checkData(request.data['fields']):
            try:
                if database_entry(request.data['fields']):
                    client.send_email(
                        FromEmailAddress='GitHub Community SRM <community@githubsrm.tech>',
                        Destination={
                            'ToAddresses': [
                                request.data['fields']['College Email'],
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
                                        'Data': emailbody(file='confirm_email.html', name=request.data['fields']['Name'], otp=None),
                                        'Charset': 'utf-8'

                                    }
                                }
                            },
                        }
                    )
                return HttpResponse("Data received successfully", status=201)
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
                                'Data': emailbody(file='email.html', otp=otp, name=request.data["name"]),
                                'Charset': 'utf-8'

                            }
                        }
                    },
                }
            )

            return Response({"jwt": jwt}, status=201)
        except Exception as e:
            print(e, response)
            return HttpResponse("Internal Server Error", status=500)
