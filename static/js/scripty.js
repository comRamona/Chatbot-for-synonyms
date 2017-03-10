$(function(){
  $('button').click(function(event) {
        /* Act on the event */
        $.ajax({
          url: '/ajaxcalc', //server url
          type: 'POST',    //passing data as post method
          dataType: 'json', // returning data as json
          data: {pig1:$('#in1').val()},  //form values
          success:function(json)
          {
            console.log(json.result);  //response from the server given as alert message
            $("#result").html(": "+json.result);

          }
        
        });
        
      });
});
