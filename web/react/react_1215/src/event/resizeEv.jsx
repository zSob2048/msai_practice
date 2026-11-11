import React, { useEffect, useState } from 'react'

const ResizeEv = () => {
    
    const [size, setSize] = useState({
        w : window.innerWidth,
        h : window.innerHeight
    });
    const resixee = (   ) => { 
        setSize({w : window.innerWidth,
        h : window.innerHeight})
     };

     useEffect(()=>{
        window.addEventListener("resize",resixee); // < 원래 JS문법
        return ()=>{
            window.removeEventListener("resize",resixee); // < 원래 JS문법
        };
     },[]);

  return (
    <div>{size.w + ","+ size.h }</div>
  )
}

export default ResizeEv