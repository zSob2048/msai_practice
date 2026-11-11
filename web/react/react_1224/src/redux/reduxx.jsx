import React from 'react'
import { useState } from 'react'

const Reduxx = () => {
    const [h1CSS, setH1CSS] = useState({fontSize:30});
    const sizeUP = () => { setH1CSS({fontSize: h1CSS.fontSize+10}); };
    const sizeDOWN = () => { setH1CSS({fontSize: h1CSS.fontSize-10}); };
    
  return (<>
    <button onClick={sizeUP}>size UP</button>
    <button onClick={sizeDOWN}>size DOWN</button>
    <h1 style={h1CSS}>Reduxx</h1>
    </>
  )
}

export default Reduxx