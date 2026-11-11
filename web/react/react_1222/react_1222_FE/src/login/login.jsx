import React, { useState } from 'react'
import axios from 'axios';

const Login = () => {
const [userr, setUserr] = useState({id:"",pw:""});
const changeUserr = (e) => { 
    setUserr({...userr,[e.target.name]:e.target.value});
 };

const regUserr = () => { 
    axios.get(`http://195.168.9.202:2048/c.a?id=${userr.id}&pw=${userr.pw}`)
    .then((res) => { 
      alert(res.data.jwtresult); // 복호화 불가
      sessionStorage.setItem("jwtt",res.data.jwtresult);
      setUserr({id:"",pw:""});
     }).catch(()=>{alert("fail");});
 };

const chkUserr = () => { alert(sessionStorage.getItem("jwtt")) ;};

const decodingjwt = () => { 
      axios.get(`http://195.168.9.202:2048/c.b?jwt=${sessionStorage.getItem("jwtt")}`)
    .then((res) => { 
      alert(res.data.result)
      alert(res.data.id); // 복호화 불가
      alert(res.data.pw); // 복호화 불가
      // sessionStorage.setItem("jwtt",res.data.jwtresult);
      // setUserr({id:"",pw:""});
     }).catch(()=>{alert("fail");});
 };

 const udateexpjwt = () => { 
  axios.get(`http://195.168.9.202:2048/c.d?jwt=${sessionStorage.getItem("jwtt")}`)
    .then((res) => { 
      alert(res.data.result);
    sessionStorage.setItem("jwtt",res.data.result);
    });
  };

 const deljwt = () => { sessionStorage.removeItem("jwtt") };


  return (
    <>
    ID: <input value={userr.id} name="id" onChange={changeUserr}/> <br/>
    PW: <input value={userr.pw} name="pw" onChange={changeUserr}/> <br/>
    <button onClick={regUserr}>set</button>
    <button onClick={chkUserr}>checkkkkk</button>
    <button onClick={decodingjwt}>decode</button>
    <button onClick={udateexpjwt}>udateexp</button>
    <button onClick={deljwt}>delete</button>
    <hr/>

    </>
  );
}

export default Login