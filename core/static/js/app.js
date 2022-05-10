
$(document).ready(function(){

    equipos_data();

    setInterval(equipos_data, 6000);









  });

  function equipos_data() {
    $.ajax({
       url: "/equipo",
        type: 'GET',
        dataType: 'json',
       contentType: 'application/json; charset=utf-8',
      destroy: true,
      success: function (data) {
           
           $("#name").html(data.name);
           $("#direction").html(data.direction);
           $("#name").html(data.name);
           $("#state").html(data.state);
           $("#pro_consum").html(data.pro_consum);



            console.log(data)
       }

   });
}