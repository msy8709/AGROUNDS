from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .models import User_info
from DB.models import TeamInfo
from .serializers import Team_info_Serializer
from .serializers import UpdateTeamInfoSerializer

class maketeam(APIView):
    """
    json 형식
    {
    "team_host": "u_1sa886fuu8678", 
    "team_name": "test", 
    "team_logo": "test",
    "team_area": "test",
    "team_description": "test"
    }
    """
    def post(self, request, *args, **kwargs):
        serializer = Team_info_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            # 유효성 검사 오류 메시지를 확인하여 반환합니다.
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class update_team(APIView):
    """
    json 형식
    {
    "team_code": "t_1sa888s3bheta6", 
    "team_host": "u_1sa886fuu8678", 
    "team_player": ["u_1sa886fuu8678"],
    "team_logo": "test",
    "team_area": "test",
    "team_description": "test"
    }
    """
    def patch(self, request, *args, **kwargs):
        team_code = request.data.get('team_code')
        team_info = TeamInfo.objects.get(team_code=team_code)
        serializer = UpdateTeamInfoSerializer(team_info, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            # 유효성 검사 오류 메시지를 확인하여 반환합니다.
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)