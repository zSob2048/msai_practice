import React from 'react'
import { useSelector } from 'react-redux';

const InputTest2 = () => {
    const txt = useSelector((st) => st.txt);
  return (
    <h2>{txt.txt}</h2>
  )
}

export default InputTest2