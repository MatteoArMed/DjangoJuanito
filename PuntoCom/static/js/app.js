


function EnviarFormularioContacto(){
	// Variables formulario 'Contacto'
	var emailContacto = document.getElementById('email');
	var descripcion = document.getElementById('descripcion');
    	
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


function enviarTrabajo() {
	
	// // Variables del formulario de Crear Servicios
    var nombreServicio = document.getElementById('nombreServicio').value;
    var subtitulo = document.getElementById('subTitulo').value;
    var descripcionServicio = document.getElementById('descripcionServicio').value;
    var precioServicio = document.getElementById('precioServicio').value;
    var imagenServicio = document.getElementById('fotosServicio').value;

    if (nombreServicio === '' || nombreServicio === null) {
        alert('Debes ingresar un nombre, no puede estar vacio')
        return false;
    } else if (subtitulo === '' || subtitulo === null) {
        alert('Debes ingresar un subtitulo, lo ideal es que sea un pequeño resumen')
        return false;
    } else if (descripcionServicio === '' || descripcionServicio === null) {
        alert('Debes ingresar una descripcion, ni muy larga ni muy corta')
        return false;
    } else if (precioServicio === '' || precioServicio === null || precioServicio < 0) {
        alert('El precio no puede ser menor que 0')
        return false;
    }

    // Si todos los campos están llenos y válidos, envía el formulario
    document.getElementById('addservicio').submit();
    return true;
}


function previsualizarImagen(event) {
    var input = event.target;
    var imagenPrevia = document.getElementById('imagenPrevia');
    if (input.files && input.files[0]) {
        var lector = new FileReader();
        lector.onload = function(e) {
            imagenPrevia.src = e.target.result;
            imagenPrevia.style.display = 'block';
        }
        lector.readAsDataURL(input.files[0]);
    } else {
        imagenPrevia.src = "#";
        imagenPrevia.style.display = 'none';
    }
}
