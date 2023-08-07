// CHAT
var messages = [];
var send_blank = false;
let askQuery = document.querySelector("#ask-query");
let bubbles = document.querySelector("#bubbles");

// APPEND INTO CHAT
var chatBody = document.querySelector(".chat-body");
var append_message = function (message) {
  {
    if (message.user == true) {
      var div = document.createElement("div");
      div.classList.add("chat-bubble", "me");
      div.innerHTML = message.text;
      chatBody.appendChild(div);
      chatBody.scrollTop = chatBody.scrollHeight;
    } else {
      var div = document.createElement("div");
      div.classList.add("chat-bubble", "you");
      div.innerHTML = message.text;
      chatBody.appendChild(div);
      chatBody.scrollTop = chatBody.scrollHeight;
    }
  }
};

// LOAD OLD MESSAGES
var load_messages = function () {
  for (let i = 0; i < messages.length; i++) {
    append_message(messages[i]);
  }
};
document.addEventListener("load", load_messages());

// ADD MESSAGES MAIN METHOD
var add_message = function () {
  if (askQuery.value.length > 0) {
    var message = {
      text: askQuery.value,
      user: true,
      chat_bot: false,
    };
    messages.push(message);
    append_message(message);

    document
      .querySelector(".chat-body")
      .appendChild(document.querySelector("#bubbles"));
    $("#bubbles").removeClass("hide");
    chatBody.scrollTop = chatBody.scrollHeight;
    askQuery.value = "";
    send_blank = false;

    fetch("/get-response/", {
      body: JSON.stringify({ message: message["text"] }),
      cache: "no-cache",
      credentials: "same-origin",
      headers: {
        "user-agent": "Mozilla/4.0 MDN Example",
        "content-type": "application/json",
      },
      method: "POST",
      mode: "cors",
      redirect: "follow",
      referrer: "no-referrer",
    })
      .then((response) => response.json())
      .then((json) => {
        messages.push(json["message"]);

        $("#bubbles").addClass("hide");

        append_message(json["message"]);

        if (
          "Sorry, We don't have such information for now." ===
          json["message"].text
        ) {
          let options = document.querySelectorAll(".chat-start");
          for (let i = 0; i < options.length; i++) {
            document.querySelector(".chat-body").appendChild(options[i]);
          }
        }
        chatBody.scrollTop = chatBody.scrollHeight;
      });
  } else {
    send_blank = true;
  }
};

// SUGGESTED QUERIES
let makeQuery = function (id) {
  document.querySelector("#ask-query").value = document.querySelector(
    `#${id}`
  ).innerHTML;
  document.querySelector("#ask-query-button").click();
};


document.querySelector("#Location").addEventListener("click", function () {
  makeQuery(this.id);
});
document
  .querySelector("#ContactDetails")
  .addEventListener("click", function () {
    makeQuery(this.id);
  });

// Home Page Slide Show

var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs((slideIndex += n));
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  if (n > x.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = x.length;
  }
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  x[slideIndex - 1].style.display = "block";
}
