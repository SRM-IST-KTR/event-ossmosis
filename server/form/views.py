from .utils import checkData, checkotp, createjwt, createotp, emailbody
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from .mongo import database_entry
from .backends import CustomPerms
from rest_framework import status
import boto3
from .serializer import EmailSerializer, DataEntrySerializer

client = boto3.client('sesv2', region_name='ap-south-1')


class DataEntry(APIView):
    """ 

    Class to handle data entry

    """

    permission_classes = [CustomPerms]
    throttle_scope = 'emails'
    serializer_class = DataEntrySerializer

    def post(self, request, **kwargs) -> Response:
        if self.serializer_class(data=request.data).is_valid():
            if database_entry(request.data['fields']):
                pass
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            client.send_email(
                FromEmailAddress='GitHub Community SRM <community@githubsrm.tech>',
                Destination={
                    'ToAddresses': [
                        request.data['fields']['email'],
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
                                'Data': emailbody(file='confirm_email.html', name=request.data['fields']['name'], otp=None),
                                'Charset': 'utf-8'

                            }
                        }
                    },
                }
            )
            return HttpResponse("Data received successfully", status=status.HTTP_200_OK)
        else:
            return HttpResponse("Bad request", status=status.HTTP_400_BAD_REQUEST)


class Email(APIView):
    """ 

    Class to handle emails

    """

    throttle_scope = 'emails'
    serializer_class = EmailSerializer

    def post(self, request, **kwargs) -> Response:

        otp = createotp()
        jwt = createjwt(otp)

        try:

            if self.serializer_class(data=request.data).is_valid():
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

                return Response({"jwt": jwt}, status=status.HTTP_201_CREATED)

            return Response(status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return HttpResponse("Internal Server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
