async function sendMessage() {
    const input = document.getElementById("userInput");
    const chatBox = document.getElementById("chatBox");

    const message = input.value;
    if (!message) return;

    chatBox.innerHTML += `<div class="user-message">${message}</div>`;

    try {
        const response = await fetch("http://127.0.0.1:8000/admission-query", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ query: message })
        });

        const data = await response.json();

        chatBox.innerHTML += `<div class="bot-message">${data.response}</div>`;
    } catch (error) {
        chatBox.innerHTML += `<div class="bot-message">Error connecting to server.</div>`;
    }

    input.value = "";
}