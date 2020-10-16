
contenido_textarea = "";
num_caracteres_permitidos = 913;
function valida_longitud() {
  num_caracteres = document.forms[0].texto.value.length;
  if (num_caracteres > num_caracteres_permitidos) {
    document.forms[0].texto.value = contenido_textarea;
  } else {
    contenido_textarea = document.forms[0].texto.value;
  }

  if (num_caracteres >= num_caracteres_permitidos) {
    document.forms[0].caracteres.style.color = "#ff0000";
  } else {
    document.forms[0].caracteres.style.color = "#000000";
  }
  cuenta();
}

function cuenta() {
  document.forms[0].caracteres.value = document.forms[0].texto.value.length;
}