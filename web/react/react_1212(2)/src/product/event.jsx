import React from "react";

const Event = () => {
  // const [first, setfirst] = useState(second)

  const test = (e) => {
    alert(e.target.value);
    alert(e.target.name);
  };
  return (
    <>
      <input
        name="aaa"
        onClick={() => {
          alert("a");
        }}
        onChange={test}
      />{" "}
    </>
  );
};

export default Event;
