import React from "react";
import { useRef } from "react";
import { useState } from "react";
import { v_null } from "./zValidCheckR";

const InputValidChack = () => {
  const [menu, setMenu] = useState({ name: "", price: "", desc: "" });
  const menuInput = useRef({});

  const changeMenu = (e) => {
    setMenu({ ...menu, [e.target.name]: e.target.value });
  };

  const regMenu = () => {
    if (validC()) {
      alert("ok");
    }
  };

  const validC = () => {
    if (!v_null(menu.name)) {
      alert("nooooo");
      menuInput.current.name.value="";
      menuInput.current.name.focus();
      return false;
    }
    return true;
  };

  return (
    <>
      메뉴명 :
      <input
        ref={(thisInput) => {
          menuInput.current.name = thisInput;
        }}
        value={menu.name}
        onChange={changeMenu}
        name="name"
        // className={mmc.txtTypeInput}
        maxLength={30}
      /> <br/>
      가격 :
      <input
        ref={(thisInput) => {
          menuInput.current.price = thisInput;
        }}
        value={menu.price}
        onChange={changeMenu}
        name="price"
        // className={mmc.txtTypeInput}
        maxLength={5}
      /> <br/>
      설명 :
      <input
        ref={(thisInput) => {
          menuInput.current.name = thisInput;
        }}
        value={menu.desc}
        onChange={changeMenu}
        name="desc"
        // className={mmc.txtTypeInput}
        maxLength={100}
      /> <br/>
      <button onClick={regMenu}> 버튼 </button>
    </>
  );
};

export default InputValidChack;
