function ajustarAltura() {
    var altura = window.innerHeight;
    var altura2 = altura - 240
    var altura3 = window.innerWidth;
    var altura4 = altura3 -100
    console.log(altura2)
    document.getElementById("table-container").style.height = altura2 + "px";
    document.getElementById("table-container").style.width = altura4 + "px";
  }
  ajustarAltura();
  
  window.addEventListener("resize", ajustarAltura);

  /*Selctor nuevo socio y list ficha*/

const seleccionado_product = document.getElementById('list');
const seleccionado_fpagos = document.getElementById('new');

seleccionado_product.addEventListener('click', function() {
    document.getElementById('list').classList.toggle('active');
})



