import React, { useEffect } from "react";

const ScrollEv = () => {
  const scrollll = () => {
    const scrollT = window.scrollY ;
    const scrollH = window.innerHeight ;
    const contentH = document.documentElement.scrollHeight;
    if (scrollH+scrollT>=contentH){
        alert(scrollT+","+scrollH+">"+contentH);
    }
  };
  useEffect(() => {
    window.addEventListener("scroll", scrollll);
    return () => {
      window.removeEventListener("scroll", scrollll);
    };
  }, []);

  return <div>scrollT</div>;
};

export default ScrollEv;
