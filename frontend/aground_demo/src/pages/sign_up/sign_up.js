import React, {useState, useEffect} from 'react';
import './sign_up.scss';
import SignUpInput from '../../components/textintput/sign_up_input';
import Female from "../../assets/female.png";
import male from "../../assets/male.png";
import Checkbox from '../../components/checkbox/checkbox';
import client from '../../clients';
import GeneralBtn from '../../components/button/generalBtn';
import classNames from 'classnames';
import { useNavigate } from 'react-router-dom';
import GoBack from '../../assets/go-back-icon.png';
import Nav from '../../components/general/nav';
const SignUp = () => {
    const [email, setEmail] = useState('');
    const [password,setPassword] = useState('');
    const [isEmail,setIsEmail] = useState('');
    const [isPassword,setIsPassword] = useState('');
    const [nickname, setNickname] = useState('');
    const [name, setName] = useState('');
    const [birth,setBirth] = useState('');
    const [gender, setGender] = useState('');
    const [marketingAgree, setMarketingAgree] = useState('');
    const [termsAgree,setTermsAgree] = useState('');
    const [privacyAgree,setPrivacyAgree] = useState('');
    const [allAgree,setAllAgree] = useState('');
    const [isNickname,setIsNickname] = useState('');
    const [isName,setIsName] = useState('');
    const [isBirth,setIsBirth] = useState('');
    const [selectedGender, setSelectedGender] = useState(null);

    const navigate = useNavigate();
    const handleGenderSelect = (gender) => {
        setSelectedGender(gender);
        setGender(gender);
    };
    
    let isAgree = privacyAgree && termsAgree;
    let isAllValid = isEmail && isPassword && isName && isNickname && isBirth && isAgree;

    useEffect(() => {
        setAllAgree(privacyAgree && termsAgree && marketingAgree)
    },[privacyAgree ,termsAgree, marketingAgree])

    const saveEmail = (e) => {
        setEmail(e.target.value);
        const isValidEmail = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(e.target.value);
        setIsEmail(isValidEmail ? "1" : "0");
        if (e.target.value === "") {
            setIsEmail("2");
          }
        
    }
    
    const savePassword = event => {
        setPassword(event.target.value);
        const IsValidPassword = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&^])[A-Za-z\d@$!%*#?&^]{8,}$/.test(event.target.value)
        setIsPassword(IsValidPassword? "1" : "0");
        
    }
    
    const saveNickname = event => {
        setNickname(event.target.value);
        const IsValidNickname = /^[a-zA-Z가-힣0-9!@#$%^&*()-_=+{};:,<.>]{3,10}$/.test(event.target.value)
        setIsNickname(IsValidNickname ? "1" : "0")
    }
    
    const saveName = event => {
        setName(event.target.value);
        const IsValidName = /^[가-힣a-zA-Z]{2,20}$/.test(event.target.value)
        setIsName(IsValidName);
        }
    
    const saveBirth = event => {
        setBirth(event.target.value);
        setIsBirth(event.target.value);
    }
    
    
    const onSubmitHandler = async event => {
        event.preventDefault();

        let SignUpData = {
            'user_id' : email,
            'password' : password,
            'user_birth' : birth,
            'user_name' : name,
            'user_gender' : gender,
            'user_nickname' : nickname,
            'marketing_agree' : marketingAgree
        }
        console.log(SignUpData);

        client.post('/api/V2login/signup/',SignUpData)
        .then(function(response){
            console.log(response);
            alert('회원가입에 성공했습니다.');
            navigate("/")
        })
        .catch(function(error){ 
            alert('회원가입에 실패했습니다.');
            console.log(error)
        })
    }

    
    return (
        <form onSubmit={onSubmitHandler}>
            <div className='signupbackground'>
                <Nav/>
                <SignUpInput title='이름' type='text' onChange={saveName}/>
                <SignUpInput title='닉네임' type='text' onChange={saveNickname}/>
                <div className='signupinput'>
                    <div className='gender_title'>성별</div>
                    <div className='gender-largebox'>
                        <div className='gender-mediumbox'>
                            <div className={classNames('gender-logobox', {'black': selectedGender === 'female'})} onClick={() => handleGenderSelect('female')}><img className='gender-logo' src={Female}/></div>
                            <div className='gender-description'>여성</div>
                        </div>
                    </div>
                    <div className='gender-largebox'>
                        <div className='gender-mediumbox'>
                            <div className={classNames('gender-logobox', {'black': selectedGender === 'male'})} onClick={() => handleGenderSelect('male')}><img className='gender-logo' src={male}/></div>
                            <div className='gender-description'>남성</div>
                        </div>
                    </div>
                </div>
                <SignUpInput title='이메일' placeholder='이메일 형식으로 입력'type='email' onChange={saveEmail} />
                <SignUpInput title='비밀번호' placeholder='특수문자 포함 8자리이상' type='password' onChange={savePassword}/>
                <SignUpInput title='생년월일' type='date' onChange={saveBirth}/>
                <Checkbox setTermsAgree={setTermsAgree}privacyAgree={privacyAgree}termsAgree={termsAgree}marketingAgree={marketingAgree}allAgree={allAgree}setAllAgree={setAllAgree}setMarketingAgree={setMarketingAgree}setPrivacyAgree={setPrivacyAgree} />
                {isAllValid ? <GeneralBtn color='black' onClick={onSubmitHandler}>가입하기</GeneralBtn> : <GeneralBtn type='button'color='white'>가입하기</GeneralBtn>}
                <div style={{height: '10vh'}}></div>
            </div>
        </form>
    );
};

export default SignUp;