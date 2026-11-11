import React, { useState } from 'react'

const Rpssss = () => {
    const [snacks] = useState([
        {name: "과자1", price: 2000, color:"#A0CB8C"},
        {name: "과자2", price: 500, color:"#6F9F68"},
        {name: "과자3", price: 4000, color:"#617555"}
    ])

    // const snackupper1000 = snacks.filter((s)=>s.price>=1000);

    const snackTrs = snacks.map((s) => { return <tr style={{color:s.color}}>
        <td>{s.name}</td>
        <td>{s.price}</td>
    </tr> });
  return (
    <table border={1}><tr>
        <th>이름</th>
        <th>가격</th>
        </tr>
        {snackTrs}
        </table>
  );

};

export default Rpssss