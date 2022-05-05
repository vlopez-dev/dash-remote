
$(document).ready(function(){

    free_memory();

    setInterval(free_memory, 4000);









    
  });

function free_memory(){
    $.ajax({
        url: "/free_memory",
         type: 'GET',
         dataType: 'json',
        contentType: 'application/json; charset=utf-8',
       destroy: true,
       success: function (data) {

            $("#memory_free").html(memory_free);

 
        }

 
    });
}