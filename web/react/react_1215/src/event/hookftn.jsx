import React, { useEffect, useReducer, useRef, useState } from "react";

const HookFtn = () => {
  const [clickCount, setClickCount] = useState(0);

  const changeCnt = () => {
    let cnt = clickCount;
    setClickCount(cnt + 1);
  };

  /////////////////////////////////////
  const recordtxt = (history_i, inputobj) => {
    // 기존state값(:self), 그 외 변수(payload라고 부름...)
    return history_i + "+" + inputobj.alpabet + inputobj.num;
  }; // setter역할 함수 : 밖에...
  // >> 이후 setHistory 호출시 recordtxt실행
  const [history, setHistory] = useReducer(recordtxt, "PI");

  /////////////////////////////////////

  const [css1, setCss1] = useState({ color: "#A0CB8C" });

  const changeCss = (state, payL) => {
    // return { ...state, color: payL.target.value };
    return {color: payL.target.value };
  };
  const [css2, setCss2] = useReducer(changeCss, { color: "#A0CB8C" });
  /////////////////////////////////////
  
    // useRef : 객체 선택이 필요한 경우
    const paper =useRef();
    // 이후 생성자에 ...
    // 생성자 (=$(function(){}))
    const [pen, setPen] = useState();

    useEffect(() => {
      setPen(paper.current.getContext("2d"));
      // pen.fillRect(10,10,30,30);
      
      // return () => {}; // 소멸자 : 객체가 화면상에서 사라질때
      // 배열 생략시 : 이 객체가 렌더링 될 때마다 : 시작, 값 변경, css변경 등
    }, []); // 마지막 배열 : 객체 처음 렌더링될+ 배열 안 값 변경마다
    

    const drowSqr = (e) => { return pen.fillRect(e.nativeEvent.offsetX-5, e.nativeEvent.offsetY-5, 10, 10); }
    
  /////////////////////////////////////

  return (
    <>
      <h1>count: {clickCount}</h1>
      <button
        onClick={() => {
          setClickCount(clickCount + 1);
        }}
      >
        click!
      </button>
      <button onClick={changeCnt}>click!</button>
      <br />
      useState(멤버변수)+ set(___)(setter ; 멤버변수 값 바꾸는 메소드... )
      <br />
      OOP 캡슐화 : 멤버변수를 직접 수정하지 못하게 해 잘못된 값을 입력하는걸
      방지... 하는 용도였는데 그냥 문화쯤으로 남음
      <hr />
      <button
        onClick={() => {
          setHistory({ alpabet: "A", num: 1 });
        }}
      >
        A1
      </button>
      <button
        onClick={() => {
          setHistory({ alpabet: "A", num: 2 });
        }}
      >
        A2
      </button>
      <button
        onClick={() => {
          setHistory({ alpabet: "B", num: 1 });
        }}
      >
        B1
      </button>
      <button
        onClick={() => {
          setHistory({ alpabet: "B", num: 2 });
        }}
      >
        B2
      </button>
      <h1>{history}</h1>
      <hr />
      <input
        style={css1}
        onChange={(e) => setCss1({ color: e.target.value })}
        value={css1.color}
      ></input>
      <br />
      <input style={css2} value={css2.color} onChange={(e) => setCss2(e)} />
      <hr />
      뭔가 2번씩 실행... : main.jsx의 StrictMode (개발중엔 2회/build뒤엔 1회) 지워도 됨
      <hr />
      <canvas ref={paper} style={{border: "black solid 2px"}} width={300} height={300}
      onClick={(e) => { drowSqr(e) }}/>
    </>
  );
};

export default HookFtn;
