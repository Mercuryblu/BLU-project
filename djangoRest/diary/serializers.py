from rest_framework import serializers
from .models import Diary


# 유저정보
class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = UserSerializerfields = (
            'userId',
            'userName',
            'email',
        )


# 일기
class DiarySerializer(serializers.ModelSerializer) :
    # user = UserSerializer(read_only=True) # user정보 읽기만

    class Meta :
        model = Diary
        fields = (
            'user',
            'title', 
            'content', 
            'create_at',
        )
        read_only_fields = ('create_at',) # 날짜 읽기만

        user_id = serializers.SerializerMethodField("get_user_id")

        def get_user_id(self, obj):
            return obj.user.username
            
            