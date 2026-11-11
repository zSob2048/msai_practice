import React from 'react'
import { useSelector } from 'react-redux'

const Reduxxx = () => {
    const h1Csss = useSelector((st) => st.sizee)
  return (
    <h1 style={h1Csss}>Reduxxx</h1>
  )
}

export default Reduxxx