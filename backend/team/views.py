from django.shortcuts import render
# 함수추가 
from staticfiles.get_info import get_user_code_by_user_nickname 
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .models import User_info
from DB.models import TeamInfo
from .serializers import Team_info_Serializer
from .serializers import UpdateTeamInfoSerializer
from .serializers import Team_main_page
from .serializers import Team_Search
from .serializers import Team_More_info
from .serializers import *

## main page
class TeamMainAPI(APIView):
    def get(self, request):
        team_info = TeamInfo.objects.all()
        serializer = Team_main_page(team_info, many=True)
        return Response(serializer.data)


class TeamMakeTeamAPI(APIView):
    """
    json 형식
    {
    "team_host": "u_1sa88lq2mi23fl2", 
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

class TeamUpdateTeamAPI(APIView):
    """
    json 형식
    {
    "team_code": "t_1sa88m32hn7rb8", 
    "team_player": ["규성98"],
    "team_logo": "test",
    "team_area": "test",
    "team_description": "test"
    }
    """
    def patch(self, request, *args, **kwargs):
        team_code = request.data.get('team_code')
        try:
            team_info = TeamInfo.objects.get(team_code=team_code)
        except TeamInfo.DoesNotExist:
            return Response({'error' : '해당 팀이 존재하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UpdateTeamInfoSerializer(team_info, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            # 유효성 검사 오류 메시지를 확인하여 반환합니다.
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# team search
class TeamSearchAPIView(APIView):
    """
    { 
       "team_tier" : "bronze"
    }
    or 
    {
        "team_area": "인천광역시"
    }
    """
    def post(self, request):
        team_tier = request.data.get('team_tier')
        team_area = request.data.get('team_area')

        if team_tier is None and team_area is None:
            return Response({"error": "At least one of team_tier or team_area parameters is required"}, status=status.HTTP_400_BAD_REQUEST)

        if team_tier and team_area:
            return Response({"error": "Please provide either team_tier or team_area, not both"}, status=status.HTTP_400_BAD_REQUEST)

        if team_tier:
            team_info = TeamInfo.objects.filter(team_tier=team_tier)
            context = {'tier': team_tier}
        else: 
            team_info = TeamInfo.objects.filter(team_area=team_area)
            context = {'area': team_area}

        if team_info.exists():
            serializer = Team_Search(team_info, many=True, context=context)
            return Response(serializer.data)
        else:
            return Response({"error": "No team information found for the provided criteria"}, status=status.HTTP_404_NOT_FOUND)

# 팀 상세 조희 API
class TeamMoreInfoAPI(APIView):
    """
    {
    "team_code": "t_1sa88og1lrrmvq"
    }
    """
    def post(self, request):
        team_code = request.data.get('team_code')
        if team_code is None:
            return Response({"error": "team_code parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        team_info = TeamInfo.objects.filter(team_code=team_code)
        if not team_info.exists():
            return Response({"error": "Team with provided team_code does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = Team_More_info(team_info, many=True, context={'team_code': team_code})
        return Response(serializer.data)


# 팀 선수 상세 조회 API
class TeamPlayerMoreInfoView(APIView):
    """
    { 
        "user_code": "강인01"
    }
    """
    def post(self, request):
        user_code = get_user_code_by_user_nickname(request.data.get('user_code'))
        if user_code is None:
            return Response({"error": "user_code parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        team_info = PlayerInfo.objects.filter(user_code=user_code)
        serializer = Team_Player_More_info(team_info, many=True, context={'user_code': user_code})
        return Response(serializer.data)

# 팀 요약 조회 API 
class TeamShortView(APIView):
    def get(self, request, format=None):
        areas = ["서울특별시", "인천광역시", "부산광역시", "대전광역시", "대구광역시",
                 "울산광역시","광주광역시","경기도","강원도","충청북도",
                 "충청남도","경상북도","전라북도","전라남도","세종특별자치시","제주특별자치도"]
        data = [{"area": area} for area in areas]
        serializer = Team_Short_info(data=data, many=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)