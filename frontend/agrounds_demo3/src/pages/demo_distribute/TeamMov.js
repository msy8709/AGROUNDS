import React , {useState} from 'react';
import DownBtn from '../../components/display/DownBtn';
import Mov from '../../assets/display/playanal/Q3/replay.mp4';
import styled from 'styled-components';
import AIcam from '../../assets/aicam.png';
import Nav from '../../components/display/Nav';
import VideoPlayer from '../../components/demo/VideoPlayer';

const TeamMov = () => {
  return (
    <TeamMovStyle>
      <Nav arrow={true}/>
      <div className='theme'>AI CAM<img src={AIcam}/></div>
      <div className='titlebox'>
        <p className='title'>팀 영상</p>
        <DownBtn bgColor="#616161" onClick={() => alert('아직 지원하지 않는 기능입니다.')} >다운로드</DownBtn>
      </div>
      <VideoPlayer url="" />
      <p className='content1'>영상은 15일 뒤 자동 삭제됩니다.</p>
      <p className='content2'>삭제일자: 업데이트 일 + 15일</p>
    </TeamMovStyle>
  );
};

export default TeamMov;

const TeamMovStyle = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 420px;

  .theme{
    color: #055540;
    font-size: 16px;
    font-weight: 600;
    display: flex;
    align-items: center;
    width: 90%;
    margin-top: 5vh;
    img{
      height: 16px;
      margin-left: 1vh;
    }
  }
  .titlebox{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    width: 90%; 
    margin-top: 1vh;
    .title{
      font-weight: 700;
      color: black;
      font-size: 24px;
      margin: 0;
    }
  }

  .content1{
    color: #616161;
    font-size: 14px;
    margin: 2vh 0 0 0;
    width: 90%;
  }
  .content2{
    color: #616161;
    font-size: 14px;
    margin: 0;
    width: 90%;
  }
`

const VideoStyle = styled.div`
  video{
    margin: auto;
  }
`

// const TeamMovStyle = styled.div`
//   display: flex;
//   flex-direction: column;
//   align-items: center;

//   .theme{
//     color: #055540;
//     font-size: 1.9vh;
//     font-weight: 600;
//     display: flex;
//     align-items: center;
//     width: 340px;
//     margin-top: 5vh;
//     img{
//       height: 16px;
//       margin-left: 1vh;
//     }
//   }
//   .titlebox{
//     display: flex;
//     flex-direction: row;
//     align-items: center;
//     justify-content: space-between;
//     width: 340px;
//     margin-top: 1vh;
//     .title{
//       font-weight: 700;
//       color: black;
//       font-size: 24px;
//       margin: 0;
//     }
//   }

//   .content1{
//     color: #616161;
//     font-size: 14px;
//     margin: 2vh 0 0 0;
//     width: 340px;
//   }
//   .content2{
//     color: #616161;
//     font-size: 14px;
//     margin: 0;
//     width: 340px;
//   }

// `