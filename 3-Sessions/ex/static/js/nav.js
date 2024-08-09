let intervalId = null;

function sessionUpdate() {
    console.log('[INFO] Session Update...');
    fetch('/session/update/')
        .then(response => response.json())
        .then(data => {
            if (data.username) {
                if (data.remaining_time === -1) {
                    if (intervalId !== null) {
                        clearInterval(intervalId);
                        intervalId = null;
                    }
                    console.log('- A user is logged in, session does not need to be updated.');
                } else {
                    const remainingTime = data.remaining_time * 1000;
                    if (intervalId === null) {
                        intervalId = setInterval(sessionUpdate, remainingTime);
                    }
                    console.log('- No user logged in, session will be updated in', remainingTime, 'ms.');
                }
                document.getElementById('username').innerText = data.username;
                console.log('- Current username:', data.username);
            }
        })
        .catch(error => {
            console.error('Error fetching username:', error);
            setTimeout(sessionUpdate, 1000);
        });
}
sessionUpdate();

function sessionGet() {
    console.log('[INFO] Session Get...');
    fetch('/session/info/')
        .then(response => response.json())
        .then(data => {
            console.log('- Session info:', data);
        })
        .catch(error => {
            console.error('Error fetching session info:', error);
        });
}
setInterval(sessionGet, 5000);