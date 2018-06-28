
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
class CustomAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response_details = {}
        serializer = self.serializer_class(data=request.data, context={'request':request})
        print(serializer)
        if serializer.is_valid():
            user_instance = serializer.validated_data.get('user')
            response_details['id'] = user_instance.id
            response_details['name'] = user_instance.username
            response_details['token'] = Token.objects.get_or_create(user=user_instance)[0].key
            response_details["status_code"] = status.HTTP_200_OK
        else:
            response_details['error'] = "Invalid Details"
            response_details["status_code"] = status.HTTP_401_UNAUTHORIZED

        return Response(data=response_details)
