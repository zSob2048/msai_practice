import React, { useEffect } from "react";
import { useState } from "react";

const MouseEvent = () => {
  const divCss = { width: 200, height: 200, border: "black solid 2px" };
  const [moveEv, setMoveEv] = useState("");
  const [xyEv, setXyEv] = useState("undef, undef");
  const [xyEv2, setXyEv2] = useState("undef, undef");
  const [clickEv, setClickEv] = useState("click");

  const clickEvChange = (event) => {
    setClickEv(event);
  }; // 정리차원

  ///////////////////////////////////////////

  const [tableCss, setTableCss] = useState(
    {width: "80px", backgroundColor: "#F2F2E8",display: "none", position: "absolute"}
  );

  const nonPopup = (ee) => {
    ee.preventDefault(); // 기존기능 삭제
  };

  const menuPopup = (ee) => {
  if (ee.button == 2) {
    setTableCss({...tableCss,left : ee.clientX+ 1 + "px", top:ee.clientY+ 1 + "px",display:"block"});

  } else {
    setTableCss({...tableCss,display:"none"});
  }};

  useEffect(() => {
    document.addEventListener("contextmenu", nonPopup);
    document.addEventListener("mouseup", menuPopup);

    return () => {
      document.removeEventListener("contextmenu", nonPopup);
      document.removeEventListener("mouseup", menuPopup);
    };
  });

  return (
    <>
      <div
        style={divCss}
        onMouseEnter={() => {
          setMoveEv("enter");
        }}
        onMouseMove={(e) => {
          setXyEv(e.clientX + "," + e.clientY);
          setXyEv2(e.nativeEvent.offsetX + "," + e.nativeEvent.offsetY);
        }}
        onMouseLeave={() => {
          setMoveEv("leave");
        }}
        onMouseUp={(e) => {
          clickEvChange("UP :" + e.button);
        }}
        onMouseDown={(e) => {
          clickEvChange("DOWN :" + e.button);
        }}
      ></div>{" "}
      <h2>{moveEv}</h2>
      <h2>{xyEv} : browser 기준</h2>
      <h2>{xyEv2} : 객체 기준</h2>
      <h2>{clickEv}</h2>
      {/* <img src="myunn.png" width="50px" style="position: absolute;" onMouseMove={} /> */}
      <table style={tableCss}>
        <tr align="center">
          <td>
            <a href="https://www.naver.com">메뉴1</a>
          </td>
        </tr>
        <tr align="center">
          <td>
            <a href="https://www.google.com">메뉴2</a>
          </td>
        </tr>
        <tr align="center">
          <td>
            <a href="https://www.daum.net">메뉴3</a>
          </td>
        </tr>
      </table>
    </>
  );
};

export default MouseEvent;
