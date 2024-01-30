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
      <div id="deleteMessageContainer" class="grey-color" style="position: relative;">
          <span class="grey-color">[${currdateFormat}]</span> 
          ${userName}: <i>${messageField.value}</i> 
          <i class="material-icons" 
            style="color: green; font-size: 14px; margin-right: -13px; position: absolute; bottom: 0px;">done</i>
      </div>
    `;
}


displayMessageFromDB = (userName, currdateFormat, newMessageData) => {
  return messageContainer.innerHTML += `
  <div style="position: relative;">
      <span class="grey-color">[${currdateFormat}]</span> 
      ${userName}: <i>${newMessageData.fields.text}</i> 
      <i class="material-icons" 
        style="color: green; font-size: 14px; margin-right: -13px; position: absolute; bottom: 0px;">done</i>
      <i class="material-icons" 
        style="color: green; font-size: 14px; margin-left: 4px; position: absolute; bottom: 0px;">done</i>
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