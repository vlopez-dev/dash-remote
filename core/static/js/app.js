
$(document).ready(function(){

    equipos_data();

    setInterval(equipos_data, 6000);









  });

  function equipos_data() {
    $.ajax({
       url: "/lectura",
        type: 'GET',
        dataType: 'json',
       contentType: 'application/json; charset=utf-8',
      destroy: true,
      success: function (data) {
        console.log(data)

          //  $("#state").html(data[1].state);
          //  $("#pro_consum").html(data[2].pro_consum);
          //  $("#memory_free").html(data[2].memory_free);


       }

   });
}