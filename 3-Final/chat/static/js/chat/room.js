$(document).ready(function() {
    const roomNameElement = document.getElementById('room-name');
    if (!roomNameElement) {
        console.error('No room-name element found in the DOM');
        return;
    }

    const roomName = JSON.parse(roomNameElement.textContent);

    const chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
    );

    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        const chatLog = document.getElementById('chat-log');
        const userList = document.getElementById('user-list');
    
        if (data.type === 'recent_messages') {
            data.messages.forEach(function(msg) {
                const messageElement = document.createElement('div');
                messageElement.classList.add('chat-message');
                messageElement.innerHTML = `
                    <div class="username">${msg.username}</div>
                    <div class="message-bubble">${msg.message}</div>
                `;
                chatLog.appendChild(messageElement);
            });
            chatLog.scrollTop = chatLog.scrollHeight;
        } else if (data.type === 'user_list') {
            userList.innerHTML = '';
            data.users.forEach(function(user) {
                const userElement = document.createElement('div');
                userElement.classList.add('user-item');
                userElement.textContent = user;
                userList.appendChild(userElement);
            });
        } else {
            const messageElement = document.createElement('div');
            if (data.username === "System") {
                messageElement.classList.add('system-message');
                messageElement.innerHTML = `<div class="message-bubble">${data.message}</div>`;
            } else {
                messageElement.classList.add('chat-message');
                messageElement.innerHTML = `
                    <div class="username">${data.username}</div>
                    <div class="message-bubble">${data.message}</div>
                `;
            }
            chatLog.insertBefore(messageElement, chatLog.firstChild);
            chatLog.scrollTop = chatLog.scrollHeight;
        }
    };

    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

    $('#chat-message-input').focus();
    $('#chat-message-input').on('keyup', function(e) {
        if (e.key === 'Enter') {
            $('#chat-message-submit').click();
        }
    });

    $('#chat-message-submit').on('click', function(e) {
        const messageInputDom = $('#chat-message-input');
        const message = messageInputDom.val();
        chatSocket.send(JSON.stringify({
            'message': message
        }));
        messageInputDom.val('');
    });
});