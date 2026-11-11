import axios from 'axios';
import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { loginChk } from '../../../siteMain';

const LoginForm = () => {
    const go = useNavigate();
    
    const [memberLogin, setMemberLogin] = useState({id:"",pw:""});
    const mFormDL = new FormData();
    mFormDL.append("id",memberLogin.id);
    mFormDL.append("pw",memberLogin.pw);
    const inputMember = (e) => { 
        setMemberLogin({...memberLogin,[e.target.name]: e.target.value});
     }

    const login = () => { 
        axios.post("http://195.168.9.202:2048/member.login", mFormDL,
                    {headers:{"Content-Type":"multipart/form-data"}, withCredentials:true})
            .then((res) => { if (res.data.result === "로그인 성공"){
                sessionStorage.setItem("Login",res.data.memberInfo)  ;
                
                loginChk();
                go(0);
            } else {
                  alert(res.data.result);
            } });
     }

  return (
    <table id='loginFormA'>
        <tr>
            <td>
                <input
                    name='id'
                    value={memberLogin.id}
                    onChange={(e)=>{
                        if (/\W/.test(e.target.value)){
                        e.target.value = e.target.value.replaceAll(/\W/,"");
                        }
                        inputMember(e)}}
                    placeholder='ID'
                />
            </td>
        </tr>
        <tr>
            <td>
                <input 
                    name='pw'
                    value={memberLogin.pw}
                    onChange={(e)=>{
                        if (/[^0-9a-zA-Z_!@#$%^*+=-]/.test(e.target.value)){
                            e.target.value = e.target.value.replaceAll(/[^0-9a-zA-Z_!@#$%^*+=-]/,"");
                        }
                        inputMember(e)}}
                    placeholder='PW'
                    type="password" 
                />
            </td>
        </tr>
        <tr>
            <td align='center' valign='bottom'>
                <button onClick={login}>Login</button>
                <button onClick={() => { go("/sign.up") }}>Sign up</button>
            </td>
        </tr>
    </table>
  )
}

export default LoginForm