
$(document).ready(function(){

    reload()


     setInterval(reload, 6000);








  });


 function reload() {
  $( "#valores" ).load(window.location.href + " #valores" );
  console.log("refrescado")
}

