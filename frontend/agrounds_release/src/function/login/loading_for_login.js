import { useEffect } from 'react';
import './loading.scss'
import client from '../../client';
import { useNavigate } from 'react-router-dom';

const LoadingPage = () => {
    const url = new URL(window.location.href);
    const token = url.searchParams.get('code');
    const type = url.searchParams.get('type');

    const navigate = useNavigate();
    // 카카오 로그인 시 token이 url parameter로 들어오는지 검사하고,
    // 들어오고 있으면 token을 api에 전송하여 유저 정보 불러옴
    useEffect(()=>{
        if (token === '0' && type !== 'apple'){
            let hostname = window.location.hostname
            if(hostname !== 'localhost')
                hostname = 'agrounds.com'
            window.location.replace(process.env.REACT_APP_BASE_URL+"/api/login/kakao/?hostname=" + hostname);
        } else {
            setTimeout(loader, 1000 * 1);
        }
    },[])

    function loader() {
        if(token === null){
            console.log('token is not comming');
            alert('로그인 실패 : 토큰이 null 입니다.');
            window.location.replace('/app');
        } else {
            client.defaults.headers.common['Authorization'] = token;
            client.get('/api/login/get-user-info')
            .then(function(response){
                console.log(response);
                sessionStorage.setItem('token', response.data.token)
                sessionStorage.setItem('userCode', response.data.user_code);
                sessionStorage.setItem('userId', response.data.user_id);
                sessionStorage.setItem('userBirth', response.data.user_birth);
                sessionStorage.setItem('userName', response.data.user_name);
                sessionStorage.setItem('userGender', response.data.user_gender);
                sessionStorage.setItem('userNickname', response.data.user_nickname);
                sessionStorage.setItem('marketingAgree', response.data.marketing_agree);
                sessionStorage.setItem('loginType', response.data.login_type);
                sessionStorage.setItem('userType', response.data.user_type);
                sessionStorage.setItem('userHeight', response.data.user_height);
                sessionStorage.setItem('userWeight', response.data.user_weight);
                sessionStorage.setItem('userPosition', response.data.user_position);
                sessionStorage.setItem('teamCode', response.data.team_code);

                if(response.data.user_type === '-1') { // 가입 후 첫 로그인시 팀 가입 유도 페이지로 이동
                    window.location.replace('/app/completesignup');
                } else {
                    navigate('/app/main');
                }
            })
            .catch(function(error){
                alert('로그인 실패');
                window.location.replace('/app');
                console.log(error);
            });
        }
    }

    return(
        <div style={{width: '100%', height:'100vh', display:'flex', flexDirection:'column', 
        alignItems:'center', justifyContent:'center'}}>
            <div style={{fontWeight: '700', fontSize: '5vh', position:'absolute'}}>AGROUNDS</div>
            <span style={{position:'absolute', bottom:'20vh'}} className="loader"></span>
        </div>
    )
};

export default LoadingPage