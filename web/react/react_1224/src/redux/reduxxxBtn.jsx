import React from 'react'
import { useDispatch } from 'react-redux'
import { sizeDown, sizeUp } from '../h1SizeSlice';

const ReduxxxBtn = () => {
    const d = useDispatch();
  return (
    <>
        <button onClick={() => { d(sizeUp()) }}>size UP</button>
        <button onClick={() => { d(sizeDown()) }}>size DOWN</button>
    </>
  )
}

export default ReduxxxBtn