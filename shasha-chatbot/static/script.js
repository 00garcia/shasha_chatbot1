let session_id = Date.now().toString();

function appendMessage(sender, text) {
    const chatbox = document.getElementById("chatbox");
    const msgDiv = document.createElement("div");
    msgDiv.classList.add("message", sender);
    msgDiv.innerText = text;
    chatbox.appendChild(msgDiv);
    chatbox.scrollTop = chatbox.scrollHeight;
}

async function sendMessage() {
    const input = document.getElementById("userInput");
    const text = input.value;
    if (!text) return;
    appendMessage("user", text);
    input.value = "";

    const resp = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text, session_id: session_id })
    });
    const data = await resp.json();
    appendMessage("bot", data.response);
}
