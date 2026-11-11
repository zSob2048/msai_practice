import { useState } from "react";

const MyTbl = () => {
  const [txt, setTxt] = useState("");
  const [txt2, setTxt2] = useState("");
  const keyUp = (e) => {
    setTxt(e.target.value);
  };
  return (
    <>
      <tr>
        <td>
          <input value={txt} onChange={keyUp} />
          <input
            value={txt2}
            onChange={(e) => {
              setTxt2(e.target.value);
            }}
          />
        </td>
      </tr>
      <tr>
        <h1>{txt}</h1>
        <h1>{txt2}</h1>
      </tr>
    </>
  );
};

export default MyTbl;
