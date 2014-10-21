function login(username, password) {
    $.post('/login/', {
      'username': username,
      'password': password,
      'csrfmiddlewaretoken': $.cookie("csrftoken"),
    }).done(function(data) {
      if ( data == "Correct." ) {
          location.reload(true);
      }
      else {
          $("#username").css("border", "1.5px solid #e74c3c");
          $("#password").css("border", "1.5px solid #e74c3c");
      }
    });
}

$(document).ready(function() {
    $(document).foundation();
    $("#login").click(function() {
      var username = $("#username").val();
      var password = $("#password").val();
      login(username, password);
    });
    $("#logout").click(function() {
        $.post('/logout/', {
            'csrfmiddlewaretoken': $.cookie("csrftoken"),    
        }).done(function(data) {
            window.location = "/";
        });
    });
    $("#username").keydown(function(event) {
        if ( event.which == 13 ) {
            var username = $("#username").val();
            var password = $("#password").val();
            login(username, password);
        }
    });
    $("#password").keydown(function(event) {
        if ( event.which == 13 ) {
            var username = $("#username").val();
            var password = $("#password").val();
            login(username, password);
        }
    });
});