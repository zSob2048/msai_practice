import React, { useState } from "react";
import axios from 'axios';

const Ajaxpost = () => {
  const [xy, setXy] = useState({ x: 0, y: 1 });
  const [asmd, setAsmd] = useState({add:1,sub:-1,multi:0,div:0})
  const changeXy = (e)=>{setXy({...xy,[e.target.name]:e.target.value})};

  const formdataa = new FormData();
  formdataa.append("x", xy.x)
  formdataa.append("y", xy.y)

  const calculate = () => { 
    alert("a");
    // axios.post("http://195.168.9.202:2048/post.asmd", formdataa, {headers:{이름:값,이어쩌고...})
    axios.post("http://195.168.9.202:2048/upgpost.asmd", formdataa,{withCredentials:true}) //보안강화
    .then((res)=>{
      alert("succes : "+formdataa);
        alert(res);
        setAsmd(res.data);
    }).catch(()=>{alert("fail : "+formdataa.value);})
    ;
    
  };

    
  return (
    <>
      x: <input value={xy.x} name="x" onChange={changeXy}/>
      <br />
      y: <input value={xy.y} name="y" onChange={changeXy}/>
      <br />
      <button onClick={calculate}>input</button>
      <hr />
      ＋ :{asmd.add} <br />
      － :{asmd.sub}<br />
      × :{asmd.multi}<br />
      ÷ :{asmd.div}<br />
    </>
  );
};

export default Ajaxpost;
