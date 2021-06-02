from rest_framework.permissions import BasePermission
import requests
import os
from dotenv import load_dotenv
from .utils import checkotp

request = requests.Session()


class CustomPerms(BasePermission):
    def has_permission(self, request, view) -> bool:
        try:
            return self.checkToken(token=request.META['HTTP_X_RECAPTCHA_TOKEN']) and \
                   checkotp(request.headers['Authorization'], request.data['otp'])
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def checkToken(token) -> bool:
        url = "https://www.google.com/recaptcha/api/siteverify"
        load_dotenv()
        secret_key = os.getenv('RECAPTCHA_SECRET_KEY')

        payload = {
            'secret': secret_key,
            'response': token,
        }
        response = request.post(url, data=payload)

        return response.json()["success"]
