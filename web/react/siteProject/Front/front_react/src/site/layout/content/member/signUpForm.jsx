import React, { useRef, useState } from 'react'
import './member.css'
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const SignUpForm = () => {
    const go = useNavigate();
    const memberInput = useRef({});
    const [tfResult, setTfResult] = useState({id : !true,iddbc:!true, pw : !true, name : !true});

    const [memberData, setMemberData] = useState({
        id:"", 
        pw:"",
        pw2:"",
        name:"",
        addrZ:"",
        addrR:"",
        addr:"",
        bday:"",
        tel:"",
        photo:"",
    });
    
    const mFormD = new FormData();
    mFormD.append("id",memberData.id);
    mFormD.append("pw",memberData.pw);
    mFormD.append("name",memberData.name);
    mFormD.append("addr",memberData.addrZ+"!"+memberData.addrR+"!"+memberData.addr);
    mFormD.append("bday",memberData.bday+"");
    mFormD.append("tel",memberData.tel+"");
    mFormD.append("photo",memberData.photo);

    const inputMember = (e) => { 
        (e.target.name==="photo")?setMemberData({...memberData,photo: e.target.files[0]}):setMemberData({...memberData,[e.target.name]: e.target.value});
     };

     const addrApi = () => { 
         new window.daum.Postcode({
            oncomplete: function (data) {
                var extraRoadAddr = ''; 

                if(data.bname !== '' && /[동|로|가]$/g.test(data.bname)){
                    extraRoadAddr += data.bname;
                }
                if(data.buildingName !== '' && data.apartment === 'Y'){
                   extraRoadAddr += (extraRoadAddr !== '' ? ', ' + data.buildingName : data.buildingName);
                }
                if(extraRoadAddr !== ''){
                    extraRoadAddr = ' (' + extraRoadAddr + ')';
                }
                
                setMemberData({
                    ...memberData,
                    addrZ: data.zonecode,
                    addrR: data.roadAddress+extraRoadAddr,
                });
            },
        }).open();
      };

    const idCheck = (e) => {
        if (e.target.value.length >= 8){
        axios.get(`http://195.168.9.202:2048/member.idcheck?id=${e.target.value}`)
            .then((res)=>{
                setTfResult({...tfResult,id:res.data.result});
            })
        }else{setTfResult({...tfResult,id:false});}
    }

    const allTfCheck = () => {
        if(tfResult.id && tfResult.pw && tfResult.name && memberData.pw===memberData.pw2){
            if (memberData.photo ==""){
                axios.post("http://195.168.9.202:2048/member.signup", mFormD,
                    {headers:{"Content-Type":"multipart/form-data"}, withCredentials:true})
                .then((res) => { 
                    if (res.data.result === "가입 성공"){
                        memberInput.current.photo.value = "";
                            setMemberData({
                                id:"", 
                                pw:"",
                                pw2:"",
                                name:"",
                                addrZ:"",
                                addrR:"",
                                addr:"",
                                bday:"",
                                tel:"",
                                photo:"",
                            });
                        alert(res.data.result);
                        go("/");
                    }
                    else{alert(res.data.result);} })
                // .catch((res)=>{alert(res);})
                }
                else{axios.post("http://195.168.9.202:2048/member.sign.up", mFormD,
                    {headers:{"Content-Type":"multipart/form-data"}, withCredentials:true})
                .then((res) => { 
                    if (res.data.result === "가입 성공"){
                        memberInput.current.photo.value = "";
                            setMemberData({
                                id:"", 
                                pw:"",
                                pw2:"",
                                name:"",
                                addrZ:"",
                                addrR:"",
                                addr:"",
                                bday:"",
                                tel:"",
                                photo:"",
                            });
                        alert(res.data.result);
                        go("/");
                    }
                    else{alert(res.data.result);} })
                // .catch((res)=>{alert(res);})
                }
        }else{
            alert("입력상황 확인")
        }
    };
  return (
    <table id='signUpA'>
        <tr>
            <th align='center' colSpan={2}>
                <h1>Sign Up</h1>
                <a> * 항목 필수 입력</a>
            </th>
        </tr>
        <tr>
            <td> * ID </td>
            <td> <input 
                name='id'
                value={memberData.id}
                onChange={(e)=>{
                    if (/\W/.test(e.target.value)){
                        e.target.value = e.target.value.replaceAll(/\W/,"");
                    }
                    idCheck(e);
                    inputMember(e);
                }}
                type='text'
                placeholder='ID' 
                className='normalI' 
                maxLength={20}
            /><br/>
            <a>_ 이외 특수문자 불가 8~20자</a><br/>
            <a style={{color : (tfResult.id)?"#42524180":"#c2788c"}}>
                {(tfResult.id)?"사용 가능한 ID 입니다.":"사용 불가능한 ID 입니다."}</a>
            <a style={{color : (tfResult.id)?"#42524180":"#c2788c"}}>
                {(memberData.id.length>=8&&!tfResult.id)?"(ID 중복)":""}</a>
            </td>
        </tr>
        <tr>
            <td> * PW </td>
            <td align='left'> 
            <input  
                name='pw'
                value={memberData.pw}
                onChange={(e)=>{
                    if (/[^0-9a-zA-Z_!@#$%^*+=-]/.test(e.target.value)){
                        e.target.value = e.target.value.replaceAll(/[^0-9a-zA-Z_!@#$%^*+=-]/,"");
                    }
                    setTfResult({...tfResult, pw: e.target.value!=="" && /^(?=.*[A-z])(?=.*[0-9]).{8,20}$/.test(e.target.value)})
                    inputMember(e);
                }}
                type="password" 
                placeholder='비밀번호' 
                className='normalI' 
                maxLength={20}
                /> <br/>
                <a style={{color :  (tfResult.pw)?"#42524180":"#c2788c"}}>
                영문, 숫자를 포함한 8~20자</a> <br/>
                <a>사용 가능 특수문자: !@#$%^*+=-</a> <br/>
            <input  
                name='pw2'
                value={memberData.pw2}
                onChange={(e)=>{
                    if (/[^0-9a-zA-z_!@#$%^*+=-]/.test(e.target.value)){
                        e.target.value = e.target.value.replaceAll(/[^0-9a-zA-z_!@#$%^*+=-]/,"");
                    }
                    inputMember(e);
                }}
                type="password" 
                placeholder='비밀번호 확인' 
                className='normalI' 
                maxLength={20}
            /> <br/>
            <a style={{color :  "#c2788c"}}>
                {(memberData.pw===memberData.pw2)?"":"비밀번호가 일치하지 않습니다"} </a> <br/>
            </td>
        </tr>
        <tr>
            <td> * Name </td>
            <td> <input 
                name='name'
                value={memberData.name}
                onChange={(e)=>{
                    inputMember(e);
                    setTfResult({...tfResult, name : e.target.value.length>=2});
                }}
                placeholder='이름' 
                className='normalI' 
                maxLength={10}
            />
            {/* <br/><a>{memberData.name.length}/10</a> */}
            <br/><a style={{color : (tfResult.name)?"#42524180":"#c2788c"}}>2~10자</a>
            
            </td>
        </tr>
        <tr>
            <td> Address </td>
            <td> 
                <input 
                    value={memberData.addrZ}
                    onClick={addrApi}
                    placeholder='우편번호' 
                    className='postNumI'
                /> 
                <button id='postNumB' onClick={addrApi}>우편번호 찾기</button> <br/> 
                <input 
                    value={memberData.addrR}
                    onClick={addrApi}
                    placeholder='도로명 주소' 
                    className='normalI'
                /> <br/>
                <input 
                    placeholder='상세주소' 
                    className='normalI'
                /> <br/>
            </td>
        </tr>
        <tr>
            <td> B-Day </td>
            <td> <input 
                name='bday'
                value={memberData.bday}
                onChange={(e) => { if(e.target.value.length>8){e.target.value = e.target.value.slice(0,8);}
                    inputMember(e);} }
                onWheel={(e) => e.target.blur()}
                placeholder='20000101' 
                className='normalI' 
                type='number' 
            /></td>
        </tr>
        <tr>
            <td> Tel </td>
            <td> <input 
                name='tel'
                value={memberData.tel}
                onChange={(e) => { if(e.target.value.length>11){e.target.value = e.target.value.slice(0,11);}
                    inputMember(e);} }
                onWheel={(e) => e.target.blur()}
                placeholder='01012345678' 
                className='normalI' 
                type='number' 
            /></td>
        </tr>
        <tr>
            <td> Photo </td>
            <td> <input 
                ref={(thisInput) =>
                    (memberInput.current.photo = thisInput)
                    }
                name='photo'
                onChange={inputMember}
                type='file' 
                accept='.png,.jpg,.jpeg' 
                className='photoI'
            /></td>
        </tr>
        <tr>
            <th align='center' colSpan={2}>
                <button 
                    id='signUpB'
                    onClick={allTfCheck}
                >Sign Up</button>
            </th>
        </tr>
    </table>
  )
}

export default SignUpForm