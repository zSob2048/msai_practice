import React, { useState } from "react";
import axios from 'axios';

const Ajaxget = () => {
  const [xy, setXy] = useState({ x: 0, y: 1 });
  const [asmd, setAsmd] = useState({add:1,sub:-1,multi:0,div:0})
  const changeXy = (e)=>{setXy({...xy,[e.target.name]:e.target.value})};

  const calculate = () => { 
    alert("a");
    axios.get(`http://195.168.9.202:2048/get.asmd?x=${xy.x}&y=${xy.y}`)
    .then((res)=>{
        alert(res);
        setAsmd(res.data);
    }).catch(()=>{alert("fail");})
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

export default Ajaxget;
