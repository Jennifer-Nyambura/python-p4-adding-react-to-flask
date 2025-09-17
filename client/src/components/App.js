import React, { useState, useEffect } from "react";
import NewMessage from "./NewMessage";

function App() {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/messages")
      .then((r) => r.json())
      .then((data) => setMessages(data));
  }, []);

  function handleAddMessage(newMessage) {
    setMessages([...messages, newMessage]);
  }

  function handleDelete(id) {
    fetch(`http://127.0.0.1:5555/messages/${id}`, {
      method: "DELETE",
    }).then(() => {
      setMessages(messages.filter((msg) => msg.id !== id));
    });
  }

  return (
    <div>
      <h1>Chatterbox</h1>
      <ul>
        {messages.map((msg) => (
          <li key={msg.id}>
            <strong>{msg.username}: </strong> {msg.body}
            <button onClick={() => handleDelete(msg.id)}>❌</button>
          </li>
        ))}
      </ul>
      <NewMessage currentUser={{ username: "Alice" }} onAddMessage={handleAddMessage} />
    </div>
  );
}

export default App;
