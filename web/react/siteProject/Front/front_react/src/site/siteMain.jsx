/* eslint-disable react-refresh/only-export-components */
/* eslint-disable react-hooks/globals */
import React, { useEffect } from 'react'
import Title from './layout/title/title'
import Menu from './layout/menu/menu'
import Content from './layout/content/content'
import "./layout/layout.css"
import "./layout/menu/loginSystem/login.css"
import axios from 'axios'
import { setMemberInfo } from '../slice/mLoginSlice'
import { useDispatch } from 'react-redux'
import { useNavigate } from 'react-router-dom'


let d = null;
let go = null;

export const loginChk = () =>{
axios.get(`http://195.168.9.202:2048/member.info?memberInfo=${sessionStorage.getItem("Login")}`)
.then((res) => {
   if (sessionStorage.getItem("Login") === null && res.data.memberInfo===undefined){
      sessionStorage.removeItem("Login");
      
      go(0);
  }else{
    d(setMemberInfo(res.data.memberInfo)) ;
    axios.get(`http://195.168.9.202:2048/member.info.r?memberInfo=${sessionStorage.getItem("Login")}`)
    .then((ress)=>{sessionStorage.setItem("Login",ress.data.memberInfo)  ;})
   }
  })}

const SiteMain = () => {
  d = useDispatch();
  go = useNavigate();

  useEffect(() => { document.addEventListener("click",loginChk);
    return () => { document.removeEventListener("click",loginChk); };
   },[]);

  return (
    <>
        <Title/>
        <Menu/>
        <Content/>
    </>
  )
}

export default SiteMain