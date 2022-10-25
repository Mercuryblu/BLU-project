from requests import request
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Diary
from .serializers import DiarySerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated



@api_view(['GET'])
def helloAPI(request) :
    return Response("hello world!")

# 일기 작성 / 일기 조회
class DiaryAPI(generics.ListCreateAPIView) :
    queryset = Diary.objects.all() # model 가져오기
    serializer_class = DiarySerializer
    permission_classes = [IsAuthenticated] # 인증 요청에 한해서 view호출 허용(로그인)

    def perfom_create(self, serializer) :
        serializer.save(user=self.request.user)
