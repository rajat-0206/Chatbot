function gettime(){
  var now = new Date();
now.setHours(now.getHours());
var isPM = now.getHours() >= 12;
var isMidday = now.getHours() == 12;
var time = [now.getHours() - (isPM && !isMidday ? 12 : 0), 
            now.getMinutes(), 
           ].join(':') +
           (isPM ? ' pm' : 'am');
  return time;
}

function bot(msg) { /*change*/
  var $content = "<div class='direct-chat-msg'>" +
    '<img alt="iamgurdeeposahan" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Google_Assistant_logo.svg/1200px-Google_Assistant_logo.svg.png" class="direct-chat-img">' +
    '<div class="direct-chat-text">' +
    msg +
    '<span class="direct-chat-timestamp pull-right">' + gettime() +
    '</span>' +
    "</div>" +
    "</div>";
  $('#chat').append($content);
  chat = document.getElementById('chat');
  chat.scrollTop = chat.scrollHeight;
}

function user(msg) { /*change*/
  var $content = "<div class='direct-sender'>" +
    '<div class="direct-sender-text">' +
    msg +
    '<span class="direct-sender-timestamp pull-left">' + gettime() +
    '</span>' +
    "</div>" +
    '<img alt="User" src="/static/images/user.jpg" class="direct-sender-img">'+
    "</div>";
  $('#chat').append($content);
}
  window.onload = function () {
    bot("Hii I am Risp. Your Personal AI assistant");
  }
  $('.sendbtn').click(function () {
    query = $('#status_message').val();
    document.getElementById('status_message').value = "";
    user(query);

    $.get('/ask', {
      'query': query,
    },
      function (data, status) {
        if (status == "success") {
          bot(data);
        }
      }
    )
  });