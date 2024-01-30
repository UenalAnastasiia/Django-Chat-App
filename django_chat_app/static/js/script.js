sendMessage = () => {
  let fd = new FormData();
  let token = getInputData('csrfmiddlewaretoken');
  let userName = getInputData('userName');
  let currdateFormat = getCurrdateFormat();
  fd.append('textmessage', messageField.value);
  fd.append('csrfmiddlewaretoken', token);
  try {
    tryFetchData(fd, userName, currdateFormat)
  } catch (e) {
      console.error('An error occured', e);
  }
}


getInputData = (name) => {
  let inputElems = document.querySelectorAll('input');
  for (i = 0; i < inputElems.length; ++i) {
      if (inputElems[i].name === name) {
          return inputElems[i].value;
      }
  }
}


getCurrdateFormat = () => {
  const today = new Date();
  const currMonth = today.toLocaleDateString("en-us", { month: "short" });
  let currdateFormat = currMonth + '. ' + today.getDate() + ', ' + today.getFullYear();
  return currdateFormat;
}


tryFetchData = async (fd, userName, currdateFormat) => {
  displayMessageByLoadingToDB(userName, currdateFormat);
  let response = await fetch('/chat/', {
    method: 'POST',
    body: fd
  });

  let json = await response.json();
  newMessageData = JSON.parse(json);
  document.getElementById('deleteMessageContainer').remove();
  displayMessageFromDB(userName, currdateFormat, newMessageData);
  resetInputFieldAfterSend();
}


displayMessageByLoadingToDB = (userName, currdateFormat) => {
  return messageContainer.innerHTML += `
      <div style="display: flex;  flex-direction: column" id="deleteMessageContainer" class="grey-color">
        <div>
          <span class="grey-color">[${currdateFormat}]</span> 
          ${userName}: <i>${messageField.value}</i> 
        </div>
        <div>
          <i class="material-icons">done</i>
        </div>
      </div>
    `;
}


displayMessageFromDB = (userName, currdateFormat, newMessageData) => {
  return messageContainer.innerHTML += `
  <div style="display: flex; flex-direction: column">
    <div>
      <span class="grey-color">[${currdateFormat}]</span> 
      ${userName}: <i>${newMessageData.fields.text}</i> 
    </div>
    <div>
      <i class="material-icons">done</i>
      <i class="material-icons">done</i>
    </div>
  </div>`;
}


resetInputFieldAfterSend = () => {
  messageField.value = '';
  document.getElementById('messageDiv').classList.remove('is-dirty');
  sendBtn.disabled = true;
}


enableSendBtn = () => {
  if(messageField.value === "") { sendBtn.disabled = true; } 
  else { sendBtn.disabled = false; }
}