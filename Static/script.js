async function sendMessage() {
    const input = document.getElementById("userInput");
    const userMessage = input.value.trim();
    if (!userMessage) return;

    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div class="user-msg">${userMessage}</div>`;
    input.value = "";

    const res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: userMessage })
    });

    const data = await res.json();
    chatBox.innerHTML += `<div class="bot-msg">${data.response}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
}
