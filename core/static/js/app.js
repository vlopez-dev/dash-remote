
$(document).ready(function(){

  consume_porcent();
  create_dynamic_table();


    setInterval(consume_porcent, 6000);








  });




function consume_porcent() {
  $.ajax({
     url: "/lectura",
      type: 'GET',
      dataType: 'json',
     contentType: 'application/json; charset=utf-8',
    destroy: true,
    success: function (data) {

      let lastItem=data[data.length-1];

      // $("#memory_free").html(lastItem.memory_free);
      // $("#pro_consum").html(lastItem.pro_consum);


      console.log(lastItem.id_equipo)

     }

 });
}


function create_dynamic_table() {
// create table
var $table = $('#table').append(  '<table />' );
// caption
$table.append('<caption>MyTable</caption>')
// thead
.append('<thead>').children('thead')
.append('<tr />').children('tr').append('<th>Nombre</th><th>Direccion</th><th>C</th><th>D</th>');

//tbody
var $tbody = $table.append('<tbody />').children('tbody');

// add row
$tbody.append('<tr />').children('tr:last')
.append("<td>val</td>")
.append("<td>val</td>")
.append("<td>val</td>")
.append("<td>val</td>");

// add another row
$tbody.append('<tr />').children('tr:last')
.append("<td>val</td>")
.append("<td>val</td>")
.append("<td>val</td>")
.append("<td>val</td>");

// add table to dom
$table.appendTo('#dynamicTable');





















  // var table=$('#table').append(  '<table />' );
  // table.append(
  // $('#table').append(  '<tbody> <tbody/>' );
  // $('#table').append(  '<tbody> <tbody/>' );
  // $('#table').append(  '<tbody> <tbody/>' );

}