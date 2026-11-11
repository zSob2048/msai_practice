import { useState } from 'react'

const Clicker = () => {
    const [click, setClick] = useState(0);
    const clickerr = () => { setClick(click+1); };
  return <button onClick={clickerr}>{click}</button>
  
}

export default Clicker