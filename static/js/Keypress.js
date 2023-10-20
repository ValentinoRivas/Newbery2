function handleKeyDown(event) {
    if (event.keyCode === 13) {
      var valor_input = document.getElementById('enter').value;
      $.ajax({
        type: "POST",
        url: "/registroSocio",
        data: {
          valor_input: valor_input
        },
        success: function(response) {
          location.reload(); // Recargar la página después de recibir la respuesta
        }
      });
    }
  }