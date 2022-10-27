const btnDelete = document.querySelectorAll('.btn-delete')
if(btnDelete) {
    const btnArray = Array.from(btnDelete);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if(!confirm('¿Estás seguro de eliminar este paciente?')){
                e.preventDefault();
            }
        } )
    })
}
var select = document.querySelector(".seleccion");
var selectOption = select.options[select.selectedIndex];
var lastSelected = localStorage.getItem('select');

if(lastSelected) {
    select.value = lastSelected; 
}

select.onchange = function () {
   lastSelected = select.options[select.selectedIndex].value;
   console.log(lastSelected);
   localStorage.setItem('select', lastSelected);
}

$(document).ready(function(){
    var radios = document.getElementsByName("es_prestador");
    var val = localStorage.getItem('es_prestador');
    for(var i=0;i<radios.length;i++){
      if(radios[i].value == val){
        radios[i].checked = true;
      }
    }
    $('input[name="es_prestador"]').on('change', function(){
      localStorage.setItem('es_prestador', $(this).val());
    
    });
  });


