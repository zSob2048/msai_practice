import React, { useEffect } from 'react'

const External = () => {
    useEffect(() => {
      window.importScripts.connect("http://195.168.9.202:2048");
    
      return () => {
        
      }
    }, []);
    
  return (
    <div>
        React에서 외부 파일 :: index.html에 넣고 사용은 window.~~~로
    </div>
  )
}

export default External