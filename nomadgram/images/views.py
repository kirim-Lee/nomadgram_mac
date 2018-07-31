from rest_framework.views import APIView 
from rest_framework.response import Response
from . import models, serializers


class ListAllImages(APIView):
    
    def get(self,request,format=None): # format None 이면 default 값인 JSON 으로 응답
        all_images = models.Image.objects.all() # 모든 이미지를 가져옴
        
        serializer = serializers.ImageSerializer(all_images, many=True)

        return Response(data=serializer.data)
