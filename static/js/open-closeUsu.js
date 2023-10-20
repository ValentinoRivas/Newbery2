const ShowPanelUsu = document.getElementById ('perfil');
const HiddenPanelUsu = document.getElementById ('close-panel');

ShowPanelUsu.addEventListener('click', function() {
    document.getElementById ('cajaUsu').classList.toggle('active');
})

HiddenPanelUsu.addEventListener('click', function() {
    document.getElementById ('cajaUsu').classList.remove('active');
})

