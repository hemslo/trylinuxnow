// application.js
$(function($, undefined) {
  $('#terminal-wrapper').terminal(function(command, term) {
    if (command !== '') {
      // var request = $.ajax({
      //   url: "postcommand",
      //   type: "POST",
      //   data: {cmd : command},
      // });
      // request.done(function(msg) {
      //   // DO STUFFS HERE2
      //   term.echo(String(msg))
      json = $.parseJSON(msg)

      // 1 term echo
      term.echo(String(json.msg))

      // 2 refresh directory tree
      $("#tree-wrapper").jstree({ 
        "json_data" : json.tree,
        "plugins" : [ "themes", "json_data", "ui" ]
      });

      // 3 refresh step
      $("#nowstep").html(json.nowstep)

    }
  }, {
    greetings: 'Greetings!',
    name: 'terminal',
    height: 400,
    width: 560,
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
