import styled from 'styled-components';
import RankBox from './RankBox';
import HighBox from './HighBox';


const TeamAnalTotal = ({data}) => {
  const topData = data.top_players;
  const myData = data.my_rankings;

  return(
    <TeamAnalTotalStyle>
      <div className="title">팀내 항목별 최고 순위</div>
      <div className="high-box">
        <div className="high-column">
          <HighBox img={topData.top_point.profile} name={topData.top_point.nickname} title='평점' titleData={topData.top_point.value} km=''/>
          <HighBox img={topData.top_activity.profile} name={topData.top_activity.nickname} title='활동량' titleData={topData.top_activity.value} km='km'/>
          
        </div>
        <div className="high-column">
          <HighBox img={topData.top_sprint.profile} name={topData.top_sprint.nickname} title='스프린트' titleData={topData.top_sprint.value} km='m'/>
          <HighBox img={topData.top_speed.profile} name={topData.top_speed.nickname} title='속력' titleData={topData.top_speed.value} km='km/h'/>
        </div>
      </div>
      <div className="title2">나의 순위</div>
      <div className='rank-box'>
        <div className="rank-column">
          <RankBox title='평점' titleData={myData.point.value} rank={myData.point.rank} />
          <RankBox title='활동량' titleData={myData.activity.value} rank={myData.activity.rank} km={true}/>
        </div>
        <div className="rank-column">
          <RankBox title='스프린트' titleData={myData.sprint.value} rank={myData.sprint.rank} km={true}/>
          <RankBox title='속력' titleData={myData.speed.value} rank={myData.speed.rank} km={true}/>
        </div>
      </div>
    </TeamAnalTotalStyle>
  )
}

export default TeamAnalTotal;

const TeamAnalTotalStyle = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 2vh;
  width: 100%;
  font-family: 'Pretendard-Regular';
  .title{
    width: 90%;
    font-size: 2vh;
    font-weight: 700;
    font-family: 'Pretendard-Regular';
    color: #262626;
  }
  .title2{
    width: 90%;
    font-size: 2vh;
    font-weight: 700;
    font-family: 'Pretendard-Regular';
    color: #262626;
    margin-top: 5vh;
  }
  .high-box{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    gap: 1.5vh;
    margin-top: 3vh;
    .high-column{
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;
      gap: 1.5vh;
    }
  }
  .rank-box{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    gap: 1.5vh;
    margin-top: 3vh;
    margin-bottom: 10vh;
    .rank-column{
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;
      gap: 1.5vh;
    }
  }
  
`
