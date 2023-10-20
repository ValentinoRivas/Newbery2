// Obtener la tabla
var tabla = document.getElementById("table");
// Añadir el evento de doble clic a las filas
var tbody = document.getElementsByTagName("tbody")[0];



    // Añadir el evento de doble clic al cuerpo de la tabla
    tbody.addEventListener("dblclick", function(event) {
      // Obtener la fila seleccionada
      var fila = event.target.parentNode;

      // Obtener los datos de la fila seleccionada
      var datosFila = [];
      var celdas = fila.cells;
      for (var i = 0; i < celdas.length; i++) {
        datosFila.push(celdas[i].innerHTML);
        console.log(datosFila);
      }
        // Crear los parámetros de la URL
      var parametro1 = encodeURIComponent(datosFila[0]);
      var parametro2 = encodeURIComponent(datosFila[1]);
      var parametro3 = encodeURIComponent(datosFila[2]);
      var parametro4 = encodeURIComponent(datosFila[3]);
      var parametro5 = encodeURIComponent(datosFila[4]);
      var parametro6 = encodeURIComponent(datosFila[5]);
      var parametro7 = encodeURIComponent(datosFila[6]);
      var parametro8 = encodeURIComponent(datosFila[7]);
      var parametro9 = encodeURIComponent(datosFila[8]);
      var parametro10 = encodeURIComponent(datosFila[9]);
      var parametro11 = encodeURIComponent(datosFila[10]);
      var parametro12 = encodeURIComponent(datosFila[11]);
      var parametro13 = encodeURIComponent(datosFila[12]);
      var parametro14 = encodeURIComponent(datosFila[13]);
      var parametro15 = encodeURIComponent(datosFila[14]);
      var parametro16 = encodeURIComponent(datosFila[15]);
      var parametro17 = encodeURIComponent(datosFila[16]);
      var parametro18 = encodeURIComponent(datosFila[17]);
      var parametro19 = encodeURIComponent(datosFila[18]);
      var parametro20 = encodeURIComponent(datosFila[19]);
      var parametro21 = encodeURIComponent(datosFila[20]);
      var parametro22 = encodeURIComponent(datosFila[21]);
      var parametro23 = encodeURIComponent(datosFila[22]);
      var parametro24 = encodeURIComponent(datosFila[23]);
      var parametro25 = encodeURIComponent(datosFila[24]);
      var parametro26 = encodeURIComponent(datosFila[25]);
      var parametro27 = encodeURIComponent(datosFila[26]);
      var parametro28 = encodeURIComponent(datosFila[27]);
      var parametro29 = encodeURIComponent(datosFila[28]);
      var parametro30 = encodeURIComponent(datosFila[29]);
      var parametro31 = encodeURIComponent(datosFila[30]);
      var parametro32 = encodeURIComponent(datosFila[31]);
      var parametro33 = encodeURIComponent(datosFila[32]);
      var parametro34 = encodeURIComponent(datosFila[33]);
      var parametro35 = encodeURIComponent(datosFila[34]);
      

      // Construir la URL con los parámetros
      var url = "http://127.0.0.1:5000//abm_ficha?";
      url += "parametro1=" + parametro1 + "&";
      url += "parametro2=" + parametro2 + "&";
      url += "parametro3=" + parametro3 + "&";
      url += "parametro4=" + parametro4 + "&";
      url += "parametro5=" + parametro5 + "&";
      url += "parametro6=" + parametro6 + "&";
      url += "parametro7=" + parametro7 + "&";
      url += "parametro8=" + parametro8 + "&";
      url += "parametro9=" + parametro9 + "&";
      url += "parametro10=" + parametro10 + "&";
      url += "parametro11=" + parametro11 + "&";
      url += "parametro12=" + parametro12 + "&";
      url += "parametro13=" + parametro13 + "&";
      url += "parametro14=" + parametro14 + "&";
      url += "parametro15=" + parametro15 + "&";
      url += "parametro16=" + parametro16 + "&";
      url += "parametro17=" + parametro17 + "&";
      url += "parametro18=" + parametro18 + "&";
      url += "parametro19=" + parametro19 + "&";
      url += "parametro20=" + parametro20 + "&";
      url += "parametro21=" + parametro21 + "&";
      url += "parametro22=" + parametro22 + "&";
      url += "parametro23=" + parametro23 + "&";
      url += "parametro24=" + parametro24 + "&";
      url += "parametro25=" + parametro25 + "&";
      url += "parametro26=" + parametro26 + "&";
      url += "parametro27=" + parametro27 + "&";
      url += "parametro28=" + parametro28 + "&";
      url += "parametro29=" + parametro29 + "&";
      url += "parametro30=" + parametro30 + "&";
      url += "parametro31=" + parametro31 + "&";
      url += "parametro32=" + parametro32 + "&";
      url += "parametro33=" + parametro33 + "&";
      url += "parametro34=" + parametro34 + "&";
      url += "parametro35=" + parametro35 + "&";
     // Redirigir a la nueva URL
     window.location.href = url;
    });