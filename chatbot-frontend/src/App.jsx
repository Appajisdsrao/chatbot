import { useState } from "react";

function App() {
    const [input, setInput] = useState("");
    const [response, setResponse] = useState("");

    const sendMessage = async () => {
        if (!input.trim()) return;  // Prevent empty messages

        try {
            const API_URL = "http://localhost:5000/ask";  // Correctly defining API URL
            const res = await fetch(API_URL, {  // Correcting fetch syntax
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: input }),  // Sending actual input message
            });

            if (!res.ok) {
                throw new Error(`HTTP error! Status: ${res.status}`);
            }

            const data = await res.json();
            setResponse(data.response);
        } catch (error) {
            console.error("Error fetching response:", error);
            setResponse("Error: Could not connect to chatbot.");
        }
    };

    return (
        <div style={{ textAlign: "center", padding: "50px", background: "#222", color: "#fff" }}>
            <h1>Chatbot</h1>
            <input 
                type="text" 
                value={input} 
                onChange={(e) => setInput(e.target.value)} 
                placeholder="Type a message..."
                style={{ padding: "10px", fontSize: "16px" }} 
            />
            <button onClick={sendMessage} style={{ marginLeft: "10px", padding: "10px", fontSize: "16px" }}>
                Send
            </button>
            <p>Response: {response}</p>
        </div>
    );
}

export default App;
