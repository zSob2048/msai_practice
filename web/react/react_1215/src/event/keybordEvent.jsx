import React, { useState } from "react";

const KeybordEvent = () => {
  const [keyUDEv, setKeyUDEv] = useState("key");
  const [keycord, setKeycord] = useState("");

  return (
    <>
      <input
        onKeyDown={(e) => {
          setKeyUDEv("DOWN");
          setKeycord(e.key);
        }}
        onKeyUp={(e) => {
          setKeyUDEv("UP");
          setKeycord(e.key);
        }}
      />
      <h2>{keyUDEv}</h2>
      <h2>{keycord}</h2>
    </>
  );
};

export default KeybordEvent;
