import React from 'react'
import axios from 'axios';
import { useState } from 'react';
import { Link, Navigate, useNavigate } from "react-router-dom";


const Pagee1 = () => {
  

const [ipttt, setIpttt] = useState({ipt1:"",ipt2:""})
const changeIpttt = (e) => { setIpttt({...ipttt,[e.target.name]:e.target.value}) ;};
const saveIpttt = () => { 
  axios.get(`http://195.168.9.202:2048/t.s?ipt1=${ipttt.ipt1}&ipt2=${ipttt.ipt2}`)
    .then((res) => { 
      alert(res.data.jwtresult);
    sessionStorage.setItem("iptt",res.data.jwtresult);
    });

 }

const n = useNavigate(); // : JS소스로 이동
// eslint-disable-next-line react-hooks/purity
let a = Math.random()
if (a>0.5){
  alert(a)
    return <Navigate to="/p2.w?ipt1=랜덤&ipt2=리다이렉트"/>
  };


return (<>
    <h1>P1</h1>
    입력1 : <input onChange={changeIpttt} name='ipt1'/><br/>
    입력2 : <input onChange={changeIpttt} name='ipt2'/><br/>
    <button onClick={saveIpttt}>정보 저장</button>
    <hr/>
    <a href="/p2.w">P2로</a>
    <Link to="/p2.w/asdf/asdf">변수전송/asdf/asdf</Link>
    <Link to="/p2.w?ipt1=asd&ipt2=fds">변수전송?ipt1=asd&ipt2=fds</Link>
    <button onDoubleClick={() => { 
      n("/p2.w/adf/asd")
      // n(-1) // 뒤로가기
     }}>더블클릭/adf/asd</button>
  </>)
}

export default Pagee1;