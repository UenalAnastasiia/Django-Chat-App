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
  let createDate = [];
  const currdate = today.toLocaleDateString("en-us", { month: "short", day: "numeric", year: "numeric" });
  const currTime = today.getHours() + ':' + today.getMinutes();
  createDate.push({'currdate': currdate, 'currTime': currTime})
  return createDate[0];
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
    <div id="deleteMessageContainer" class="mdl-card__supporting-text grey-color" style="position: relative; text-align: end; height: 50px;">
      <span class="message-span" style="border-bottom-right-radius: 0;">
        <span class="grey-color">[${currdateFormat.currTime}]</span> 
        ${userName}: <i>${messageField.value}</i> 
        <i class="material-icons" 
          style="color: green; font-size: 14px; margin-right: -13px; position: absolute; bottom: 45px;">done</i>
      </span> 
      <span class="dateSpan" style="right: 18px;">[${currdateFormat.currdate}]</span>
    </div>
    `;
}


displayMessageFromDB = (userName, currdateFormat, newMessageData) => {
  return messageContainer.innerHTML += `
    <div class="mdl-card__supporting-text grey-color" style="position: relative; text-align: end; height: 50px;">
      <span class="message-span" style="border-bottom-right-radius: 0;">
        <span class="grey-color">[${currdateFormat.currTime}]</span> 
        ${userName}: <i>${newMessageData.fields.text}</i> 
        <i class="material-icons" 
          style="color: green; font-size: 14px; margin-right: -13px; position: absolute; bottom: 45px;">done</i>
        <i class="material-icons" 
          style="color: green; font-size: 14px; margin-left: 4px; position: absolute; bottom: 45px;">done</i>
      </span> 
      <span class="dateSpan" style="right: 18px;">[${currdateFormat.currdate}]</span>
    </div>
    `;
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

requiredInputColor = () => {
  let required = document.querySelectorAll("input[required]");
  
  required.forEach(function(element) {
    element.style.color = "green";
  });
}

// let messageContainer = document.getElementById('messageContainer')