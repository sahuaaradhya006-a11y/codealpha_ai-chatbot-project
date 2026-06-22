async function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value.trim();

    if (message === "") return;

    let chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `<p><b>You:</b> ${message}</p>`;
    chatBox.innerHTML += `<p id="loading"><i>Bot is typing...</i></p>`;

    try {
        let response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ message: message })
        });

        let data = await response.json();

        document.getElementById("loading").remove();
        setTimeout(() => {
            chatBox.innerHTML += `<p><b>Bot:</b> ${data.response}</p>`;
         }, 500);
       
    } catch {
        document.getElementById("loading").remove();
        chatBox.innerHTML += `<p><b>Bot:</b> Server error</p>`;
    }

    input.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;
}