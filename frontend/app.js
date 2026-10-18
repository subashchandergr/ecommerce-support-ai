async function sendMessage() {

    const input =
        document.getElementById("messageInput");

    const message = input.value;

    if (!message) return;


    addMessage("customer", message);

    input.value = "";


    const response = await fetch(
        "http://localhost:8000/chat",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                session_id: "web-user",

                message: message
            })
        }
    );


    const data = await response.json();

    addMessage(
        "nova",
        data.reply
    );
}


function addMessage(role, text) {

    const messages =
        document.getElementById("messages");

    const div =
        document.createElement("div");

    div.className = role;

    div.innerText =
        role === "customer"
            ? "You: " + text
            : "Nova: " + text;

    messages.appendChild(div);
}