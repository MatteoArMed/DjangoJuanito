
// Variables formulario 'Contacto'
var emailContacto = document.getElementById('email');
var descripcion = document.getElementById('descripcion');


function EnviarFormularioContacto(){
    	
    if(emailContacto.value === '' || emailContacto.value === null){
		alert('Debes ingresar un correo');
		return false;

    } 
    else if (!/^[\w.-]+@[\w.-]+\.\w+$/.test(emailContacto.value)){
		alert('Debes ingresar un correo válido');
		return false;
	}
				
	if(descripcion.value === null || descripcion.value === ''){
		alert('Por favor, cuentanos que quieres hacer')
		return false;
	}

	document.getElementById('contacto').submit();
    return true;
}