var currentPromptIndex = 0;

function sendPromptAndRemoveButton(button, prompt) {
    sendPrompt(prompt);
    button.remove();
    if (currentPromptIndex < remainingPrompts.length) {
        var nextPrompt = remainingPrompts[currentPromptIndex++];
        addPromptButton(nextPrompt);
    }
}

function addPromptButton(prompt) {
    var sampleQuestionsDiv = document.getElementById('sample-questions');
    var button = document.createElement('button');
    button.textContent = prompt;
    button.setAttribute('type', 'button');
    button.onclick = function() {
        sendPromptAndRemoveButton(this, prompt);
    };
    sampleQuestionsDiv.appendChild(button);
}

function sendPrompt(prompt) {
    var promptInput = document.querySelector('textarea[name="prompt"]');
    promptInput.value = prompt;

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/generate', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    xhr.onreadystatechange = function() {
    if (xhr.readyState == 4 && xhr.status == 200) {
        var response = JSON.parse(xhr.responseText);
        updateChatLog({role: 'user', content: prompt});
        updateChatLog({...response, role: 'assistant'});
        promptInput.value = '';  
    }
};

    var data = 'prompt=' + encodeURIComponent(prompt);
    xhr.send(data);
    
    return false;
}

function updateChatLog(message) {
    var messageElement = document.createElement('div');
    messageElement.className = 'chat-entry ' + message.role;

    var roleElement = document.createElement('span');
    roleElement.className = 'role';
    roleElement.textContent = message.role + ': ';

    var contentElement = document.createElement('span');
    contentElement.className = 'content';
    contentElement.textContent = message.content;
    
    messageElement.appendChild(contentElement);
    var chatContainer = document.querySelector('.chat-container');
    chatContainer.appendChild(messageElement);

    chatContainer.scrollTop = chatContainer.scrollHeight;
}