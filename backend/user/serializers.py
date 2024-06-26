from rest_framework import serializers
from .models import UserInfo
from DB.models import PlayerInfo

from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from staticfiles.make_code import make_code

import re

# 유저 정보 불러오기
class User_main_page(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
        
        
        
class User_info_Serializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UserInfo
        # password 제외하고 리턴
        extra_kwargs = {
    	    'password' : {'write_only' : True },
            'user_code' : {'required' : False}
	    }
        
    
    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            # hashing password
            if password == "0":
                instance.password = "0"
            else:
                instance.password = make_password(password)

        instance.user_code = make_code('u')
        player_data = {
            'user_code' : instance.user_code
        }

        # birth = validated_data.pop('user_birth', None)
        # birth = birth[0:4] + '-' + birth[4:6] + '-' + birth[6:8]
        # instance.user_birth = birth
        player_info_serializer = Player_info_Serializer(data = player_data)
        player_info_serializer.is_valid(raise_exception=True)
        player_info_serializer.save()
        instance.save()
        return instance
    
    def validate(self, data):
        user_id = data.get('user_id', None)
        password = data.get("password")
        user_birth = data.get("user_birth")
        user_name = data.get("user_name")
        user_gender = data.get("user_gender")
        user_nickname = data.get("user_nickname")
        marketing_agree = data.get("marketing_agree")

        # 모든 항목을 입력받았는지 검사
        if (
            not user_id
            or not password
            or not user_birth
            or not user_name
            or not user_gender
            or not user_nickname
        ):
            raise serializers.ValidationError({"error" : "모든 필드는 필수입니다."})
        
        # 정규식 적용 유효성 검사
        self.regexes_all(user_id, password, user_nickname, user_name, user_birth)
        
        # 닉네임 중복 확인
        if UserInfo.objects.filter(user_nickname=user_nickname).exists():
            raise serializers.ValidationError({"error" : "이미 존재하는 닉네임입니다."})

        # 이메일 중복 확인
        if UserInfo.objects.filter(user_id=user_id).exists():
            raise serializers.ValidationError({"error" : "이미 가입된 이메일입니다."})
        return data

    def regexes(self, pattern, text):
        return re.compile(r''+pattern).match(text)
    
    def regexes_all(self, user_id, password, user_nickname, user_name, user_birth):
        patterns = ['^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
                    '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&^])[A-Za-z\d@$!%*#?&^]{8,}$',
                    '^[a-zA-Z가-힣0-9!@#$%^&*()-_=+{};:,<.>]{3,10}$',
                    '^[가-힣a-zA-Z]{2,20}$',
                    '^(?:(?:19|20)\d{2})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$' ]
        items = [user_id, password, user_nickname, user_name, user_birth]
        massges = ['이메일', '패스워드', '닉네임', '이름', '생년월일']

        for i in range (0, 5):
            if (self.regexes(patterns[i], items[i]) == None):
                if (i == 1 and items[i] == "0"):
                    return None
                raise serializers.ValidationError({"error" : "올바르지 않은 " + massges[i] +" 형식입니다."})
        return None


class Player_info_Serializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PlayerInfo

        extra_kwargs = {
            'player_height' : {'required' : False},
            'player_weight' : {'required' : False},
            'player_point' : {'required' : False},
            'player_area' : {'required' : False},
            'player_position' : {'required' : False},
            'player_description' : {'required' : False},
            'player_goal' : {'required' : False},
            'player_assist' : {'required' : False},
            'player_foot' : {'required' : False},
	    }