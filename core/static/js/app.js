
$(document).ready(function(){

    reload()


     setInterval(reload, 100000);







  });
  
  function modal(){

    $('#myModal').on('shown.bs.modal', function () {
      $('#myInput').trigger('focus')
    })
  }

 function reload() {
  $( "#valores" ).load(window.location.href + " #valores" );
  console.log("refrescado")
}

