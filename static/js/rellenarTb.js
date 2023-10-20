$(document).ready(function() {
  $("#search, #select").on("input", function() {
    var valor_seacrh = $("#search").val();
    var valor_select = $("#select").val();
    $.ajax({
      type: "POST",
      url: "/ficha",
      data: {
        valor_seacrh: valor_seacrh, 
        valor_select: valor_select
      },
      success: function(data) {
        var html = ""; // Variable para almacenar el contenido HTML de la tabla
        data.forEach(function(socio) {
          // Construir una fila HTML con los datos del socio
          html += "<tr>";
          html += "<td>" + socio.campo1 + "</td>";
          html += "<td>" + socio.campo2 + "</td>";
          html += "<td>" + socio.campo3 + "</td>";
          html += "<td>" + socio.campo4 + "</td>";
          html += "<td>" + socio.campo5 + "</td>";
          html += "<td>" + socio.campo6 + "</td>";
          html += "<td>" + socio.campo7 + "</td>";
          html += "<td>" + socio.campo8 + "</td>";
          html += "<td>" + socio.campo9 + "</td>";
          html += "<td>" + socio.campo10 + "</td>";
          html += "<td>" + socio.campo11 + "</td>";
          html += "<td>" + socio.campo12 + "</td>";
          html += "<td>" + socio.campo13 + "</td>";
          html += "<td>" + socio.campo14 + "</td>";
          html += "<td>" + socio.campo15 + "</td>";
          html += "<td>" + socio.campo16 + "</td>";
          html += "<td>" + socio.campo17 + "</td>";
          html += "<td>" + socio.campo18 + "</td>";
          html += "<td>" + socio.campo19 + "</td>";
          html += "<td>" + socio.campo20 + "</td>";
          html += "<td>" + socio.campo21 + "</td>";
          html += "<td>" + socio.campo22 + "</td>";
          html += "<td>" + socio.campo23 + "</td>";
        });
        // Establecer el contenido HTML completo en la tabla
        $("#table tbody").html(html);
      }
    });
  });
});