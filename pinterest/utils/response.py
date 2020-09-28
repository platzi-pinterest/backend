""""Utils Response"""

# Rest Library
from rest_framework.response import Response
from rest_framework.settings import api_settings


class CustomActions():

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def custom_response(self, response):
        status_data = response['status_code']
        response.pop('status_code')
        headers = self.get_success_headers(response)
        return Response(response, status=status_data, headers=headers)

    def set_response(self, status_code, message=None, data=None, status=None):
        response = {
            "status_code": status_code,
            # Fix Condition
            "status": status_code < 300,
            "message": message
        }
        if data:
            response.update({'data': data})
        if message:
            response.update({'message': message})
        return response
