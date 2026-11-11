import React from 'react'
import { useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';

const LoginNow = () => {
  const go = useNavigate();
  const memberInfo = useSelector((s)=>s.loginInfo.memberInfo);
  return (
    <table id='loginNowA'>
        <tr id="profileA">
            <td  align="right">
              <img src={`http://localhost:2048/member.photo?photo=${memberInfo.photo}`}
              width={"35px"}/> 
              <a>{memberInfo.name}@{memberInfo.id}</a>
            </td>
        </tr>
        <tr>
            <td align='center'valign='bottom'>
                <button onClick={() => { go("/member.info") }}>profile</button>
                <button onClick={() => { 
                  sessionStorage.removeItem("Login");
                  go(0);
                 }}>Logout</button>
            </td>
        </tr>
    </table>
  )
}

export default LoginNow