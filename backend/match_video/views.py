from rest_framework.views import APIView
from rest_framework.response import Response
from staticfiles.get_file_url import get_file_url
from django.db.models import Min

from .serializers import *

link = {
    "player" : get_file_url('video/m_0001/1쿼터/player_pc/AAAAAA_20241017_1_pc/AAAAAA_20241017_1_pc.mpd'),
    "team" :  get_file_url('video/m_0001/1쿼터/team/team.mpd'),
    "full" :  get_file_url('video/m_0001/1쿼터/full/full.mpd')
}

download_link = {
    "player" : get_file_url('video/m_0001/1쿼터/player_pc/AAAAAA_20241017_1_pc.mp4'),
    "team" : get_file_url('video/m_0001/1쿼터/team.mp4'),
    "full" : get_file_url('video/m_0001/1쿼터/full.mp4')
}

thumnails = [
    get_file_url('video/thumbnail/thumbnail1.png'), 
    get_file_url('video/thumbnail/thumbnail2.png'), 
    get_file_url('video/thumbnail/thumbnail3.png')
]

class getVideoSummation(APIView):
    def post(self, request):
        user_code = request.data.get('user_code')

        if user_code is None:
            return Response({'error': 'Missing required field: user_code'}, status=400)
        
        if not UserInfo.objects.filter(user_code=user_code).exists():
            return Response({'error': f'user_code({user_code})에 해당하는 유저가 존재하지 않습니다.'})
        
        player_videos_number = VideoInfo.objects.filter(user_code = user_code, type = 'player').count()
        team_videos_number = 0
        full_videos_number = 0
        
        user_info = UserInfo.objects.get(user_code = user_code)
        if user_info.user_type == 'coach' or user_info.user_type == 'player':
            team_code = UserTeam.objects.filter(user_code = user_code).first().team_code
            if team_code is not None :
                team_videos_number = VideoInfo.objects.filter(team_code = team_code, type = 'team').count()
                full_videos_number = VideoInfo.objects.filter(team_code = team_code, type = 'player').count()
        
        result = {
            "player_cam" : {
                "thumbnail" : thumnails,
                "number_of_videos" : player_videos_number
            },
            "team_cam" : {
                "thumbnail" : thumnails,
                "number_of_videos" : team_videos_number
            },
            "full_cam" : {
                "thumbnail" : thumnails,
                "number_of_videos" : full_videos_number
            },
            "highlight_cam" : {
                "thumbnail" : [],
                "number_of_videos" : 0
            }
        }

        return Response(result)

class getPlayerVideoList(APIView):
    def post(self, request):
        user_code = request.data.get('user_code')

        if user_code is None:
            return Response({'error': 'Missing required field: user_code'}, status=400)
        
        if not UserInfo.objects.filter(user_code=user_code).exists():
            return Response({'error': f'user_code({user_code})에 해당하는 유저가 존재하지 않습니다.'})
        
        video_infos = VideoInfo.objects.filter(user_code=user_code, type='player').values('match_code').annotate(min_id=Min('id')).values('min_id')
        serializer = Video_List_Serializer(video_infos, many = True)

        return Response({'result' : serializer.data})
                
        result = [
            {
                "match_code" : "m_0001",
                "title" : "인하대학교 FC",
                "date" : "2024-11-20",
                "thumbnail" : thumnails[0]
            },
            {
                "match_code" : "m_0002",
                "title" : "FC 호빵",
                "date" : "2024-11-21",
                "thumbnail" : thumnails[1]
            },
            {
                "match_code" : "m_0003",
                "title" : "동백 FC",
                "date" : "2024-11-22",
                "thumbnail" : thumnails[2]
            },
            {
                "match_code" : "m_0004",
                "title" : "토트넘",
                "date" : "2024-11-23",
                "thumbnail" : thumnails[0]
            },
            {
                "match_code" : "m_0005",
                "title" : "바이에른 뮌헨",
                "date" : "2024-11-24",
                "thumbnail" : thumnails[1]
            },
            {
                "match_code" : "m_0006",
                "title" : "인하대학교 FC",
                "date" : "2024-11-25",
                "thumbnail" : thumnails[2]
            },
            {
                "match_code" : "m_0007",
                "title" : "인하대학교 FC",
                "date" : "2024-11-26",
                "thumbnail" : thumnails[0]
            },
            {
                "match_code" : "m_0008",
                "title" : "인하대학교 FC",
                "date" : "2024-11-27",
                "thumbnail" : thumnails[1]
            },
        ]

        return Response({'result':result})

class getTeamVideoList(APIView):
    def post(self, request):
        user_code = request.data.get('user_code')

        if user_code is None:
            return Response({'error': 'Missing required field: user_code'}, status=400)
        
        try:
            user_info = UserInfo.objects.get(user_code=user_code)
        except UserInfo.DoesNotExist:
            return Response({'error': f'user_code({user_code})에 해당하는 유저가 존재하지 않습니다.'})
        
        result = []
        
        if user_info.user_type == 'coach' or user_info.user_type == 'player':
            team_code = UserTeam.objects.filter(user_code = user_code).first().team_code
            if team_code is not None :
                video_infos = VideoInfo.objects.filter(team_code=team_code, type='team').values('match_code').annotate(min_id=Min('id')).values('min_id')
                serializer = Video_List_Serializer(video_infos, many=True)
                result = serializer.data

        return Response({"result" : result})
        
        result = [
            {
                "match_code" : "m_0001",
                "title" : "인하대학교 FC",
                "date" : "2024-11-20",
                "thumbnail" : thumnails[0]
            },
            {
                "match_code" : "m_0002",
                "title" : "FC 호빵",
                "date" : "2024-11-21",
                "thumbnail" : thumnails[1]
            },
            {
                "match_code" : "m_0003",
                "title" : "동백 FC",
                "date" : "2024-11-22",
                "thumbnail" : thumnails[2]
            },
            {
                "match_code" : "m_0004",
                "title" : "토트넘",
                "date" : "2024-11-23",
                "thumbnail" : thumnails[0]
            },
            {
                "match_code" : "m_0005",
                "title" : "바이에른 뮌헨",
                "date" : "2024-11-24",
                "thumbnail" : thumnails[1]
            },
            {
                "match_code" : "m_0006",
                "title" : "인하대학교 FC",
                "date" : "2024-11-25",
                "thumbnail" : thumnails[2]
            },
            {
                "match_code" : "m_0007",
                "title" : "인하대학교 FC",
                "date" : "2024-11-26",
                "thumbnail" : thumnails[0]
            },
            {
                "match_code" : "m_0008",
                "title" : "인하대학교 FC",
                "date" : "2024-11-27",
                "thumbnail" : thumnails[1]
            },
        ]

        return Response({'result':result})

class getFullVideoList(APIView):
    def post(self, request):
        user_code = request.data.get('user_code')

        if user_code is None:
            return Response({'error': 'Missing required field: user_code'}, status=400)
        
        try:
            user_info = UserInfo.objects.get(user_code=user_code)
        except UserInfo.DoesNotExist:
            return Response({'error': f'user_code({user_code})에 해당하는 유저가 존재하지 않습니다.'})
        
        result = []
        
        if user_info.user_type == 'coach' or user_info.user_type == 'player':
            team_code = UserTeam.objects.filter(user_code = user_code).first().team_code
            if team_code is not None :
                video_infos = VideoInfo.objects.filter(team_code=team_code, type='full').values('match_code').annotate(min_id=Min('id')).values('min_id')
                serializer = Video_List_Serializer(video_infos, many=True)
                result = serializer.data

        return Response({"result" : result})
        
        result = [
            {
                "match_code" : "m_0001",
                "title" : "인하대학교 FC",
                "date" : "2024-11-20",
                "thumbnail" : thumnails[0]
            },
            {
                "match_code" : "m_0002",
                "title" : "FC 호빵",
                "date" : "2024-11-21",
                "thumbnail" : thumnails[1]
            },
            {
                "match_code" : "m_0003",
                "title" : "동백 FC",
                "date" : "2024-11-22",
                "thumbnail" : thumnails[2]
            },
            {
                "match_code" : "m_0004",
                "title" : "토트넘",
                "date" : "2024-11-23",
                "thumbnail" : thumnails[0]
            },
            {
                "match_code" : "m_0005",
                "title" : "바이에른 뮌헨",
                "date" : "2024-11-24",
                "thumbnail" : thumnails[1]
            },
            {
                "match_code" : "m_0006",
                "title" : "인하대학교 FC",
                "date" : "2024-11-25",
                "thumbnail" : thumnails[2]
            },
            {
                "match_code" : "m_0007",
                "title" : "인하대학교 FC",
                "date" : "2024-11-26",
                "thumbnail" : thumnails[0]
            },
            {
                "match_code" : "m_0008",
                "title" : "인하대학교 FC",
                "date" : "2024-11-27",
                "thumbnail" : thumnails[1]
            },
        ]

        return Response({'result':result})

class getMatchVideoInfo(APIView):
    def post(self, request):
        data = request.data.copy()

        required_fields = ['match_code', 'user_code', 'type']
        errors = {field: f"{field}는 필수 항목입니다." for field in required_fields if field not in data}
        if errors:
            return Response(errors, status=400)
        
        match_code = data['match_code']
        user_code = data['user_code']

        type = data['type']
        types = ['player', 'team', 'full']

        if type not in types :
            return Response({'error':'type이 올바르지 않습니다.'}, status=400)
        
        video_info = VideoInfo.objects.filter(match_code=match_code, user_code=user_code, type=type)

        if video_info is None:
            return Response({'error':'해당 영상이 존재하지 않습니다.'}, status=400)
        
        serializer = Video_Info_Serializer(video_info, many=True)

        return Response({'result':serializer.data})

        result = [
                {
                    "quarter" : "1쿼터",
                    "video_code" : "v_0001",
                    "title" : "인하대학교 FC",
                    "match_location" : "인하대운동장",
                    "date" : "2024-11-20",
                    "thumbnail" : thumnails[0],
                    "link" : link[type],
                    "download_link" : download_link[type]
                },
                {
                    "quarter" : "2쿼터",
                    "video_code" : "v_0002",
                    "title" : "인하대학교 FC",
                    "match_location" : "인하대운동장",
                    "date" : "2024-11-20",
                    "thumbnail" : thumnails[1],
                    "link" : link[type],
                    "download_link" : download_link[type]
                },
                {
                    "quarter" : "3쿼터",
                    "video_code" : "v_0003",
                    "title" : "인하대학교 FC",
                    "match_location" : "인하대운동장",
                    "date" : "2024-11-20",
                    "thumbnail" : thumnails[2],
                    "link" : link[type],
                    "download_link" : download_link[type]
                },
	        ]
        
        return Response({'result' : result})