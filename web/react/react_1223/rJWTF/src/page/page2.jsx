import React from 'react'
import axios from 'axios';
import { useNavigate, useParams, useSearchParams } from 'react-router-dom';

const Pagee2 = () => {
  const ipdt = useParams()
  const [ippr]=useSearchParams(); // ?어쩌고=어쩌고로 넘어오는 값

  const n = useNavigate();
  const printIpttt = () => { 
    alert(sessionStorage.getItem("iptt")) ;
    axios.get(`http://195.168.9.202:2048/t.e?jwt=${sessionStorage.getItem("iptt")}`)
    .then((res) => { alert(res.data.result); 
      alert(res.data.ipt1 +" & " +res.data.ipt2);
    })
   };

  return (
    <>
    <button onClick={() => { n(-1) }}>뒤로</button> <br/>
    <button onClick={printIpttt}>정보 확인</button>
    <hr/>
    입력1: {ipdt.iptt1} <br/>
    입력2: {ipdt.iptt2}
    <hr/>
    받은값 1 : {ippr.get("ipt1")}<br/>
    받은값 2 : {ippr.get("ipt2")}
    </>
  )
}

export default Pagee2