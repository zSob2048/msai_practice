import { useRef, useState } from "react";
import axios from 'axios';
import React from 'react'

const Fileupp = () => {
    const [filee, setFilee] = useState({title:"" , imggg:""});
    const [bfilee, setBfilee] = useState({title:"" , imgn:""});
    // const changeFile = (e) => { setFilee({...filee,[e.target.name]:e.target.value}); };
    const changeFileT = (e) => { setFilee({...filee,"title":e.target.value}); };
    const changeFileI = (e) => { setFilee({...filee,"imggg":e.target.files[0]}); };
   
    const imginput = useRef();

    const formdt = new FormData();
    formdt.append("title",filee.title);
    formdt.append("img",filee.imggg);

    const gotoback = () => { 
        alert("go!!");
        axios.post("http://195.168.9.202:2048/fi.le",formdt,{ headers:{"Content-Type":"multipart/form-data"}, withCredentials:true})
            .then((res)=>{
      alert("succes : "+filee.title);
        // alert(res);
        setBfilee(res.data);
    }).catch(()=>{alert("fail : "+filee.title);});
    setFilee({title:"" , imggg:""});
    imginput.current.value="";
     }
// 염병 하기싫네
// 하지말까
     
  return (
    <>
    제목: <input name="title" value={filee.title} onChange={changeFileT}/><br/>
    파일: <input  ref={imginput} onChange={changeFileI} type="file"/><br/>
    {/* 파일들 : UX문제로 잘 안쓰긴 함 <input multiple name="imggg" onChange={changeFileI}/><br/> */}
    <button onClick={gotoback}>Upp</button>
    <hr/>
    printttt: {bfilee.title} <br/>
    <img src={"http://localhost:2048/fi.leb?fileN="+bfilee.imgn}/>
    </>
  )
}

export default Fileupp