from django.urls import path, include
from .views import helloAPI, DiaryAPI

app_name = "diary"

urlpatterns = [
    path('hello/', helloAPI), # test
    path('<str:userId>/write/', DiaryAPI.as_view()), # 일기 작성
]