import React, { useState } from "react";

const Rpsss = () => {
  const [num, setNum] = useState([5,4,3,2,1]);
  // var evenNum = num.filter((n) => n % 2 === 0); // 필터링
  // var sortNum = evenNum.sort(); // >> 글자 오름차순 정렬
  var sortNum = num.sort((n1, n2) => 
    // {
    // alert(n1 + "," + n2);
    // if (n1 > n2) {
    //   return 1;
    // } else {
    //   return -1;
    // }
  // }
  n1-n2
); // >> 기본: 글자 오름차순 정렬
  const marquees = sortNum.map((n, i) => (
    <marquee behavior="alternate">{n}</marquee>
  ));
  return <div>{marquees}</div>;
};

export default Rpsss;
