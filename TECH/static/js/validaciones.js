/**
 * =====================================================
 *   TecnoStore UTC - Validaciones Frontend
 *   Proyecto: MartinezGonzalezYahirEmanuelUnidad1
 * =====================================================
 * Este archivo valida los formularios en el navegador
 * ANTES de enviarlos al servidor (validación frontend).
 * Django también los valida en el servidor (backend).
 */

// Esperar a que la página cargue completamente
document.addEventListener('DOMContentLoaded', function () {

    // -------------------------------------------------------
    // Validación: Formulario de Registro
    // -------------------------------------------------------
    const formRegistro = document.getElementById('formRegistro');
    if (formRegistro) {
        formRegistro.addEventListener('submit', function (e) {

            let valido = true;
            limpiarErrores(formRegistro);

            // Validar nombre
            const nombre = formRegistro.querySelector('[name="first_name"]');
            if (!nombre.value.trim()) {
                mostrarError(nombre, 'El nombre es obligatorio.');
                valido = false;
            }

            // Validar apellidos
            const apellido = formRegistro.querySelector('[name="last_name"]');
            if (!apellido.value.trim()) {
                mostrarError(apellido, 'Los apellidos son obligatorios.');
                valido = false;
            }

            // Validar usuario (solo letras, números y guion bajo)
            const usuario = formRegistro.querySelector('[name="username"]');
            if (!usuario.value.trim()) {
                mostrarError(usuario, 'El nombre de usuario es obligatorio.');
                valido = false;
            } else if (!/^[a-zA-Z0-9_]{3,}$/.test(usuario.value.trim())) {
                mostrarError(usuario, 'El usuario debe tener al menos 3 caracteres (letras, números o _).');
                valido = false;
            }

            // Validar email
            const email = formRegistro.querySelector('[name="email"]');
            if (!email.value.trim()) {
                mostrarError(email, 'El correo electrónico es obligatorio.');
                valido = false;
            } else if (!esEmailValido(email.value.trim())) {
                mostrarError(email, 'Ingresa un correo electrónico válido.');
                valido = false;
            }

            // Validar contraseña
            const pass1 = formRegistro.querySelector('[name="password1"]');
            if (!pass1.value) {
                mostrarError(pass1, 'La contraseña es obligatoria.');
                valido = false;
            } else if (pass1.value.length < 6) {
                mostrarError(pass1, 'La contraseña debe tener al menos 6 caracteres.');
                valido = false;
            }

            // Validar confirmación de contraseña
            const pass2 = formRegistro.querySelector('[name="password2"]');
            if (!pass2.value) {
                mostrarError(pass2, 'Confirma tu contraseña.');
                valido = false;
            } else if (pass1.value !== pass2.value) {
                mostrarError(pass2, 'Las contraseñas no coinciden.');
                valido = false;
            }

            // Validar captcha (3 + 4 = 7)
            const captcha = formRegistro.querySelector('[name="captcha_respuesta"]');
            if (!captcha.value) {
                mostrarError(captcha, 'Responde la pregunta de verificación.');
                valido = false;
            } else if (parseInt(captcha.value) !== 7) {
                mostrarError(captcha, 'Respuesta incorrecta. 3 + 4 = 7');
                valido = false;
            }

            if (!valido) {
                e.preventDefault(); // Detener el envío si hay errores
                // Hacer scroll al primer error
                const primerError = formRegistro.querySelector('.is-invalid');
                if (primerError) {
                    primerError.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
            }
        });
    }

    // -------------------------------------------------------
    // Validación: Formulario de Login
    // -------------------------------------------------------
    const formLogin = document.getElementById('formLogin');
    if (formLogin) {
        formLogin.addEventListener('submit', function (e) {

            let valido = true;
            limpiarErrores(formLogin);

            const usuario = formLogin.querySelector('[name="username"]');
            if (!usuario.value.trim()) {
                mostrarError(usuario, 'Ingresa tu nombre de usuario.');
                valido = false;
            }

            const password = formLogin.querySelector('[name="password"]');
            if (!password.value) {
                mostrarError(password, 'Ingresa tu contraseña.');
                valido = false;
            }

            if (!valido) e.preventDefault();
        });
    }

    // -------------------------------------------------------
    // Validación: Formulario de Buzón
    // -------------------------------------------------------
    const formBuzon = document.getElementById('formBuzon');
    if (formBuzon) {
        formBuzon.addEventListener('submit', function (e) {

            let valido = true;
            limpiarErrores(formBuzon);

            const asunto = formBuzon.querySelector('[name="asunto"]');
            if (!asunto.value.trim()) {
                mostrarError(asunto, 'El asunto es obligatorio.');
                valido = false;
            } else if (asunto.value.trim().length < 5) {
                mostrarError(asunto, 'El asunto debe tener al menos 5 caracteres.');
                valido = false;
            }

            const mensaje = formBuzon.querySelector('[name="mensaje"]');
            if (!mensaje.value.trim()) {
                mostrarError(mensaje, 'El mensaje no puede estar vacío.');
                valido = false;
            } else if (mensaje.value.trim().length < 10) {
                mostrarError(mensaje, 'El mensaje debe tener al menos 10 caracteres.');
                valido = false;
            }

            if (!valido) e.preventDefault();
        });
    }

    // -------------------------------------------------------
    // Validación: Formulario de Contacto
    // -------------------------------------------------------
    const formContacto = document.getElementById('formContacto');
    if (formContacto) {
        formContacto.addEventListener('submit', function (e) {

            let valido = true;
            limpiarErrores(formContacto);

            const nombre = formContacto.querySelector('[name="nombre"]');
            if (!nombre.value.trim()) {
                mostrarError(nombre, 'Tu nombre es obligatorio.');
                valido = false;
            }

            const email = formContacto.querySelector('[name="email"]');
            if (!email.value.trim()) {
                mostrarError(email, 'El correo es obligatorio.');
                valido = false;
            } else if (!esEmailValido(email.value.trim())) {
                mostrarError(email, 'Ingresa un correo válido.');
                valido = false;
            }

            const asunto = formContacto.querySelector('[name="asunto"]');
            if (!asunto.value.trim()) {
                mostrarError(asunto, 'El asunto es obligatorio.');
                valido = false;
            }

            const mensaje = formContacto.querySelector('[name="mensaje"]');
            if (!mensaje.value.trim()) {
                mostrarError(mensaje, 'El mensaje es obligatorio.');
                valido = false;
            } else if (mensaje.value.trim().length < 10) {
                mostrarError(mensaje, 'Escribe al menos 10 caracteres.');
                valido = false;
            }

            if (!valido) e.preventDefault();
        });
    }

    // -------------------------------------------------------
    // Auto-cerrar alertas después de 5 segundos
    // -------------------------------------------------------
    const alertas = document.querySelectorAll('.alert');
    alertas.forEach(function (alerta) {
        setTimeout(function () {
            const bsAlert = new bootstrap.Alert(alerta);
            if (bsAlert) bsAlert.close();
        }, 5000);
    });

    // -------------------------------------------------------
    // Efecto activo en el navbar según la página actual
    // -------------------------------------------------------
    const navLinks = document.querySelectorAll('.nav-link');
    const paginaActual = window.location.pathname;

    navLinks.forEach(function (link) {
        if (link.getAttribute('href') === paginaActual) {
            link.classList.add('active');
        }
    });

});

// -------------------------------------------------------
// FUNCIONES DE APOYO
// -------------------------------------------------------

/**
 * Muestra un mensaje de error debajo de un campo.
 * También agrega la clase 'is-invalid' para estilos Bootstrap.
 */
function mostrarError(campo, mensaje) {
    campo.classList.add('is-invalid');

    // Crear el div de error si no existe ya
    let errorDiv = campo.nextElementSibling;
    if (!errorDiv || !errorDiv.classList.contains('error-js')) {
        errorDiv = document.createElement('div');
        errorDiv.classList.add('invalid-feedback', 'error-js');
        campo.parentNode.insertBefore(errorDiv, campo.nextSibling);
    }
    errorDiv.textContent = mensaje;
}

/**
 * Limpia todos los errores de validación de un formulario.
 */
function limpiarErrores(formulario) {
    const camposInvalidos = formulario.querySelectorAll('.is-invalid');
    camposInvalidos.forEach(function (campo) {
        campo.classList.remove('is-invalid');
    });

    const erroresJs = formulario.querySelectorAll('.error-js');
    erroresJs.forEach(function (div) {
        div.remove();
    });
}

/**
 * Valida si un email tiene formato correcto.
 */
function esEmailValido(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}
