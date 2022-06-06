
$(document).ready(function(){

    reload()


     setInterval(reload, 100000);








  });


 function reload() {
  $( "#valores" ).load(window.location.href + " #valores" );
  console.log("refrescado")
}

