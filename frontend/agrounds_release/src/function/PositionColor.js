const PositionColor = {
  LWF: "linear-gradient(117.23deg, rgba(232, 123, 76, 0.8), rgba(210, 89, 58) , rgba(232, 125, 95) 80%)",
  ST: "linear-gradient(117.23deg, rgba(232, 123, 76, 0.8), rgba(210, 89, 58) , rgba(232, 125, 95) 80%)",
  RWF: "linear-gradient(117.23deg, rgba(232, 123, 76, 0.8), rgba(210, 89, 58) , rgba(232, 125, 95) 80%)",
  LWM: "linear-gradient(117.23deg, rgba(87, 187, 170, 0.8), rgba(72, 157, 158) , rgba(105, 217, 188) 80%)",
  CAM: "linear-gradient(117.23deg, rgba(87, 187, 170, 0.8), rgba(72, 157, 158) , rgba(105, 217, 188) 80%)",
  RWM: "linear-gradient(117.23deg, rgba(87, 187, 170, 0.8), rgba(72, 157, 158) , rgba(105, 217, 188) 80%)",
  LM: "linear-gradient(117.23deg, rgba(87, 187, 170, 0.8), rgba(72, 157, 158) , rgba(105, 217, 188) 80%)",
  CM: "linear-gradient(117.23deg, rgba(87, 187, 170, 0.8), rgba(72, 157, 158) , rgba(105, 217, 188) 80%)",
  RM: "linear-gradient(117.23deg, rgba(87, 187, 170, 0.8), rgba(72, 157, 158) , rgba(105, 217, 188) 80%)",
  LWB: "linear-gradient(117.23deg, rgba(92, 139, 245, 0.8), rgba(76, 103, 244) , rgba(114, 192, 250) 80%)",
  CDM: "linear-gradient(117.23deg, rgba(87, 187, 170, 0.8), rgba(72, 157, 158) , rgba(105, 217, 188) 80%)",
  RWB: "linear-gradient(117.23deg, rgba(92, 139, 245, 0.8), rgba(76, 103, 244) , rgba(114, 192, 250) 80%)",
  LB: "linear-gradient(117.23deg, rgba(92, 139, 245, 0.8), rgba(76, 103, 244) , rgba(114, 192, 250) 80%)",
  CB: "linear-gradient(117.23deg, rgba(92, 139, 245, 0.8), rgba(76, 103, 244) , rgba(114, 192, 250) 80%)",
  RB: "linear-gradient(117.23deg, rgba(92, 139, 245, 0.8), rgba(76, 103, 244) , rgba(114, 192, 250) 80%)",
  GK: "linear-gradient(97.23deg, rgba(209,198, 81, 0.8), rgba(186, 162, 64) , rgba(226, 207, 84) 80%)",
};


const PositionBackColor = {
  LWF: "linear-gradient(117.23deg, rgba(232, 123, 76, 0.1), rgba(210, 89, 58, 0.3) , rgba(232, 125, 95, 0) 80%)",
  ST: "linear-gradient(117.23deg, rgba(232, 123, 76, 0.1), rgba(210, 89, 58, 0.3) , rgba(232, 125, 95, 0) 80%)",
  RWF: "linear-gradient(117.23deg, rgba(232, 123, 76, 0.1), rgba(210, 89, 58, 0.3) , rgba(232, 125, 95, 0) 80%)",
  LWM: "linear-gradient(117.23deg, rgba(87, 187, 170, 0.2), rgba(72, 157, 158, 0.2) , rgba(105, 217, 188, 0.2) 80%)",
  CAM: "linear-gradient(117.23deg, rgba(87, 187, 170, 0.2), rgba(72, 157, 158, 0.2) , rgba(105, 217, 188, 0.2) 80%)",
  RWM: "linear-gradient(117.23deg, rgba(87, 187, 170, 0.2), rgba(72, 157, 158, 0.2) , rgba(105, 217, 188, 0.2) 80%)",
  LM: "linear-gradient(117.23deg, rgba(87, 187, 170, 0.2), rgba(72, 157, 158, 0.2) , rgba(105, 217, 188, 0.2) 80%)",
  CM: "linear-gradient(117.23deg, rgba(87, 187, 170, 0.2), rgba(72, 157, 158, 0.2) , rgba(105, 217, 188, 0.2) 80%)",
  RM: "linear-gradient(117.23deg, rgba(87, 187, 170, 0.2), rgba(72, 157, 158, 0.2) , rgba(105, 217, 188, 0.2) 80%)",
  LWB: "linear-gradient(117.23deg, rgba(92, 139, 245, 0.2), rgba(76, 103, 244, 0.2) , rgba(114, 192, 250, 0.2) 80%)",
  CDM: "linear-gradient(117.23deg, rgba(87, 187, 170, 0.2), rgba(72, 157, 158, 0.2) , rgba(105, 217, 188, 0.2) 80%)",
  RWB: "linear-gradient(117.23deg, rgba(92, 139, 245, 0.2), rgba(76, 103, 244, 0.2) , rgba(114, 192, 250, 0.2) 80%)",
  LB: "linear-gradient(117.23deg, rgba(92, 139, 245, 0.2), rgba(76, 103, 244, 0.2) , rgba(114, 192, 250, 0.2) 80%)",
  CB: "linear-gradient(117.23deg, rgba(92, 139, 245, 0.2), rgba(76, 103, 244, 0.2) , rgba(114, 192, 250, 0.2) 80%)",
  RB: "linear-gradient(117.23deg, rgba(92, 139, 245, 0.2), rgba(76, 103, 244, 0.2) , rgba(114, 192, 250, 0.2) 80%)",
  GK: "linear-gradient(97.23deg, rgba(209,198, 81, 0.2), rgba(186, 162, 64, 0.3) , rgba(226, 207, 84, 0.1) 80%)",
};

const PositionDotColor = ({ position }) => {
  let color;
  
  switch (position) {
    case 'LWF':
    case 'ST':
    case 'RWF':
      color = '#FD6C4F';
      break;
    case 'LWM':
    case 'CAM':
    case 'RWM':
    case 'LM':
    case 'CM':
    case 'RM':
    case 'CDM':
      color = '#3CF3C1';
      break;
    case 'LWB':
    case 'RWB':
    case 'LB':
    case 'CB':
    case 'RB':
      color = '#33CAFE';
      break;
    case 'CK':
      color = '#F7E46D';
      break;
    default:
      color = '#FD6C4F'; 
  }
  
  return color;
};


export {PositionColor, PositionBackColor, PositionDotColor};