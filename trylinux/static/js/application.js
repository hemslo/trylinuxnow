// application.js
$(function($, undefined) {
  $('#terminal-wrapper').terminal(function(command, term) {
    if (command !== '') {
      var request = $.ajax({
        url: "/postcommand/",
        type: "POST",
        data: {cmd : command},
      });
      request.done(function(msg) {
        // DO STUFFS HERE2
        json = msg

        // 1 term echo
        term.echo(String(json.msg))

        // 2 refresh directory tree
        // $("#tree-wrapper").jstree({
        //   "json_data" : json.tree,
        //   "plugins" : [ "themes", "json_data", "ui" ]
        // });

        // 3 refresh step
        nextstep = $("#nowstep").html()+1
        $("#nowstep").html(nextstep)


      });
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
        "data" : "/",
        "children": ["directory1", "directory2"]
      }]
    },
    "plugins" : [ "themes", "json_data", "ui" ]
  });
});
