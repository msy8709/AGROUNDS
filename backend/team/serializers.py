from rest_framework import serializers
from DB.models import TeamInfo
from DB.models import UserInfo
from django.http import JsonResponse
import datetime
from staticfiles.make_code import make_code

import re
class Team_info_Serializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = TeamInfo
        extra_kwargs = {
            'team_code': {'required' : False}
        }

    def create(self, validated_data):
        team_code = make_code('t')  # 먼저 match_code 생성
        validated_data['team_code'] = team_code  # validated_data에 추가
        validated_data['team_point'] = 0
        validated_data['team_player'] =[]
        validated_data['team_5_match'] =[]
        instance = super().create(validated_data)  # 인스턴스 생성
        instance.save()
        return instance
    
    def validate(self, data):
        required_fields = ['team_host', 'team_name', 'team_area']
        errors = {field: f"팀 {field}는 필수 항목입니다." for field in required_fields if not data.get(field)}

        if errors:
            raise serializers.ValidationError(errors)

        team_player = data.get('team_player', [])

        # If team_player is provided, execute the following logic.
        if team_player:
            # Calculate team_age based on user_birth for each team player
            team_age_list = calculate_team_age([],team_player)

            # Check for duplicate team players
            seen = set()
            for player in team_player:
                if player in seen:
                    raise serializers.ValidationError("error : team_player에 중복된 값이 있습니다.")
                seen.add(player)

            # Assign the average team age to the data
            if team_age_list:
                data['team_age'] = sum(team_age_list) // len(team_age_list)

        return data



## Team 수정페이지
class UpdateTeamInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamInfo
        exclude = ('team_code', 'team_name', 'team_point', 'team_5_match',)

    def update(self, instance, validated_data):
        instance.team_host = validated_data.get('team_host', instance.team_host)
        instance.team_logo = validated_data.get('team_logo', instance.team_logo)
        instance.team_area = validated_data.get('team_area', instance.team_area)
        instance.team_description = validated_data.get('team_description', instance.team_description)

        new_team_player = validated_data.get('team_player', [])
        
        # If new_team_player is provided, execute the following logic.
        if new_team_player:
            # Check if the new players are already in the existing team
            existing_team_player_set = set(instance.team_player)
            new_team_player_set = set(new_team_player)
            if existing_team_player_set & new_team_player_set:
                raise serializers.ValidationError("error : team_player에 중복된 값이 있습니다.")
            
            # Calculate team_age based on user_birth for each team player
            team_age_list = calculate_team_age(instance.team_player, new_team_player)

            # Merge the existing and new team players
            instance.team_player = list(existing_team_player_set | new_team_player_set)

            # Assign the average team age to the data
            if team_age_list:
                instance.team_age = sum(team_age_list) // len(team_age_list)

        instance.save()
        return instance


def calculate_team_age(existing_team_player, new_team_player):
    team_age_list = []
    all_team_players = existing_team_player + new_team_player
    for player_code in all_team_players:
        try:
            user_info = UserInfo.objects.get(user_code=player_code)
            user_birth = user_info.user_birth
            # Assuming user_birth is in YYYYMMDD format
            current_date = datetime.datetime.now()
            birth_year = int(user_birth[:4])
            birth_month = int(user_birth[4:6])
            birth_day = int(user_birth[6:8])
            birth_date = datetime.datetime(birth_year, birth_month, birth_day)
            age_timedelta = current_date - birth_date
            team_age = age_timedelta.days // 365
            team_age_list.append(team_age)
        except UserInfo.DoesNotExist:
            raise serializers.ValidationError(f"유저 코드 {player_code}에 해당하는 사용자가 존재하지 않습니다.")
    return team_age_list