import { useRef, useState } from "react";
import axios from 'axios';
import React from 'react'

const FileuppReal = () => {
    const [postt, setPostt] = useState({id:"",pw:"", ptxt:"" ,pimg:""});
    const [bposts, setBposts] = useState([]); //{id:"ID",pw:"PW", ptxt:"글내용" ,imgn:"", uptime:""}
    const [page] = useState(1)


    const postTb = bposts.map((p) => {
      return (<>
              <tr className="postTr">
                <td><img src={"http://localhost:2048/get.pim?imgn="+p.imgn} width={"100px"}/></td>
                <td rowSpan={2}>{p.uptime}<br/>{p.ptxt}
                <button onClick={()=>{deletePost(p);}}>삭제</button>
                </td>
                </tr>
              <tr>{p.id}</tr></>
      ) ;
     });

     const deletePost = (p) => {
      setBposts(bposts.filter((pp)=>p.id !== pp.id));
      axios.get("http://195.168.9.202:2048/delete.post?id="+p.id+"&imgn="+p.imgn)
            .then(()=>{
      alert("succes : "+p.id);
        // alert(res);
    }).catch(()=>{alert("fail : "+p.id);});
     };

    const changeFileT = (e) => { setPostt({...postt,[e.target.name]:e.target.value}); };
    const changeFileI = (e) => { setPostt({...postt,"pimg":e.target.files[0]}); };
   
    const imginput = useRef();

    const formdt = new FormData();
    formdt.append("id",postt.id);
    formdt.append("pw",postt.pw);
    formdt.append("txt",postt.ptxt);
    formdt.append("img",postt.pimg);

    const gotoback = () => { 
        alert("now uploading...");
        axios.post("http://195.168.9.202:2048/ipi.up",formdt,{ headers:{"Content-Type":"multipart/form-data"}, withCredentials:true})
            .then((res)=>{
      alert("succes : "+postt.id);
        alert(res);
    }).catch((res)=>{alert("fail : "+postt.id);alert(res.result);});
    setPostt({id:"" ,pw:"", ptxt:"", pimg:""});
    imginput.current.value="";
     }
     
     const getPosts = () => { 

      axios.get("http://195.168.9.202:2048/get.post?page="+page+"&txt"+"")
            .then((res)=>{
          alert("succes : "+page);
          setBposts(bposts.concat(res.data));
        // alert(res);
    }).catch(()=>{alert("fail : "+page);});
      };


  return (
    <>
    ID: <input name="id" value={postt.id} onChange={changeFileT}/><br/>
    PW: <input name="pw" value={postt.pw} onChange={changeFileT}/><br/>
    TXT: <input name="ptxt" value={postt.ptxt} onChange={changeFileT}/><br/>
    IMG: <input  ref={imginput} onChange={changeFileI} type="file"/><br/>
    <button onClick={gotoback}>Upload</button>
    <hr/>
    <button onClick={getPosts}>list</button>
    <table>
      {/* <tr>
      <td><img src={"http://localhost:2048/get.pim?imgn="+bpost.imgn} width={"100px"}/></td>
      <td rowSpan={2}>{bpost.uptime}<br/>{bpost.ptxt}
      </td>
      </tr>
      <tr>{bpost.id}</tr> */}
      {postTb}
    </table>
    </>
  )
}

export default FileuppReal