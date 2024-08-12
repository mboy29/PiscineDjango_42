document.addEventListener('DOMContentLoaded', function() {
    // Get the room name from the JSON script tag
    const roomNameElement = document.getElementById('room-name');
    if (!roomNameElement) {
        console.error('No room-name element found in the DOM');
        return;
    }

    const roomName = JSON.parse(roomNameElement.textContent);

    // Create WebSocket connection
    const chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
    );

    // Handle incoming messages
    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        document.querySelector('#chat-log').value += (data.message + '\n');
    };

    // Handle WebSocket closure
    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

    // Handle message input
    document.querySelector('#chat-message-input').focus();
    document.querySelector('#chat-message-input').onkeyup = function(e) {
        if (e.key === 'Enter') {
            document.querySelector('#chat-message-submit').click();
        }
    };

    document.querySelector('#chat-message-submit').onclick = function(e) {
        const messageInputDom = document.querySelector('#chat-message-input');
        const message = messageInputDom.value;
        chatSocket.send(JSON.stringify({
            'message': message
        }));
        messageInputDom.value = '';
    };
});
