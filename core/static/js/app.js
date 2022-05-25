
$(document).ready(function(){

    reload()


     setInterval(reload, 6000);








  });


 function reload() {
  $("#table").load(location.href + " #table");
  console.log("refrescado")
}

