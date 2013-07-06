// application.js
$(function($, undefined) {
  $('#terminal-wrapper').terminal(function(command, term) {
    if (command !== '') {
      var request = $.ajax({
        url: "postcommand",
        type: "POST",
        data: {cmd : command},
      });
      request.done(function(msg) {
        term.echo(String(msg))
      });
    }
  }, {
    greetings: 'Greetings',
    name: 'terminal',
    height: 400,
    width: 720,
    prompt: '$ '});
});

// init tree
$(function () {
  $("#tree-wrapper").jstree({ 
    "json_data" : {
      "data" : [{ 
        "data" : "/"
      }]
    },
    "plugins" : [ "themes", "json_data", "ui" ]
  });
});
