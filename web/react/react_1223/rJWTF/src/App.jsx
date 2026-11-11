import React from 'react'
import { Route, Routes } from "react-router-dom";
import Pagee1 from "./page/page1";
import Pagee2 from "./page/page2";

function App() {
  return (
    <>
      {/* <Pagee1 /> */}
      <Routes>
        <Route path="/" element={<Pagee1/>} />
        <Route index element={<Pagee1/>}/>
        <Route path="/p2.w" element={<Pagee2 />} />
        <Route path="/p2.w/:iptt1/:iptt2" element={<Pagee2 />} /> 
        {/* : 값이 넘어감 */}
      </Routes>
    </>
  );
}

export default App;
