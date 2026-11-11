import React from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { inputTxt } from '../h2TxTSlice';


const InputTest1 = () => {
    const d = useDispatch();
    const txt = useSelector((st) => st.txt);
  return (
    <input value={txt.txt} onChange={(e)=>{d(inputTxt(e.target.value));}}/>
  )
}

export default InputTest1