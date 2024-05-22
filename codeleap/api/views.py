from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

class ApiView(APIView):

    def get(self, request):
        codeleapAPI = "https://dev.codeleap.co.uk/careers/"
        r = requests.get(codeleapAPI).json()
        return Response(r, status=status.HTTP_200_OK)
    
    def post(self, request):        
        codeleapAPI = "https://dev.codeleap.co.uk/careers/"
        
        data = {
            'username': request.data.get('username'), 
            'title': request.data.get('title'), 
            'content': request.data.get('content')
        }
        r = requests.post(codeleapAPI, json=data).json()
        return Response(r, status=status.HTTP_200_OK)
    
class ApiViewObjectId(APIView):

    def get(self, request, id):
        codeleapAPI = "https://dev.codeleap.co.uk/careers/"+id+"/"
        r = requests.get(codeleapAPI).json()
        return Response(r, status=status.HTTP_200_OK)
    
    def patch(self, request, id, *args, **kwargs):
        codeleapAPI = "https://dev.codeleap.co.uk/careers/"+id+"/"
        
        data = {
            'title': request.data.get('title'), 
            'content': request.data.get('content')
        }
        r = requests.patch(codeleapAPI, json=data).json()
        return Response(r, status=status.HTTP_200_OK)
    
    def delete(self, request, id , *args, **kwargs):
        codeleapAPI = "https://dev.codeleap.co.uk/careers/"+id+"/"
        requests.delete(codeleapAPI)
        return Response(status=status.HTTP_204_NO_CONTENT)