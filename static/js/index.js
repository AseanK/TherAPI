var container = document.getElementById("bubble")
for (let i = 0; i < 15; i++) {
    let bubbleDiv = document.createElement("div")
    let bubbleBox = document.createElement("span")

    bubbleBox.className = "dot";
    bubbleDiv.appendChild(bubbleBox)
    container.appendChild(bubbleDiv);
}


function playAudio() {
    var audio = document.getElementById("audio");
    audio.play();
}


function addMessage(role, content) {
    const Messages = document.getElementById("messages");
    const messageDiv = document.createElement("div");
    messageDiv.className = role + "-message";
    messageDiv.textContent = content;
    Messages.appendChild(messageDiv);
}

// Function to handle user message submission
function sendMessage(event) {
    event.preventDefault();
    const userInput = document.getElementById("message").value;
    addMessage("user", userInput);

    // Send an AJAX request to the Flask server
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: new URLSearchParams({
            "message": userInput
        })
    })
    .then(response => response.json())
    .then(data => {
        const assistantResponse = data.response;
        addMessage("assistant", assistantResponse);
    })
    .catch(error => console.error("Error:", error));

    document.getElementById("message").value = "";
}