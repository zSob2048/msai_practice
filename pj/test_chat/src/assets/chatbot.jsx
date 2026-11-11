import { useState } from "react";

function Chatbot() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

//   const sendMessage = async () => {
//     const res = await fetch("http://localhost:2048/chat", {
//   method: "POST",
//   headers: { "Content-Type": "application/json" },
//   body: JSON.stringify({ message: input })
// });
// const data = await res.json();


//     setMessages([
//       ...messages,
//       { role: "user", content: input },
//       { role: "bot", content: data.reply }
//     ]);
//     setInput("");
//   };

const sendMessage = async () => {
  try {
    const res = await fetch("http://localhost:2048/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input })
    });

    const data = await res.json();
    console.log("DEBUG data:", data); // 응답 확인

    setMessages([
      ...messages,
      { role: "user", content: input },
      { role: "bot", content: data.reply }
    ]);
    setInput("");
  } catch (err) {
    console.error("Error:", err);
  }
};

  return (
    <div style={{ width: "400px", margin: "auto", padding: "20px" }}>
      <h2>Chatbot</h2>
      <div style={{ border: "1px solid #ccc", padding: "10px", height: "300px", overflowY: "scroll" }}>
        {messages.map((m, i) => (
          <p key={i}><b>{m.role}:</b> {m.content}</p>
        ))}
      </div>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        style={{ width: "80%", marginRight: "10px" }}
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

export default Chatbot;
