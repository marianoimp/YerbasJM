console.log("HOLAAA!")


function menosProductos() {
    document.getElementBy("Mostrar menos").innerText = "Mostrar mas";
}

function mostrarProductos() {
    var agregarElemento = document.getElementById("text-pcts");
    var toggleButton = document.getElementById("mostrar");

    if (agregarElemento.style.display === "none") {
        agregarElemento.style.display = "block";
        toggleButton.textContent = "Mostrar menos";
    } else {
        agregarElemento.style.display = "none";
        toggleButton.textContent = "Mostrar más";
    }
}


function mostrarMasMates() {
    var agregarElemento1 = document.getElementById("pcts-mates");
    var toggleButton1 = document.getElementById("mostrar-mates");

    if (agregarElemento1.style.display === "none") {
        agregarElemento1.style.display = "block";
        toggleButton1.textContent = "Mostrar menos";
    } else {
        agregarElemento1.style.display = "none";
        toggleButton1.textContent = "Mostrar más";
    }

}

function mostrarMasTermos() {
var agregarElemento = document.getElementById("pcts-termos");
var toggleButton = document.getElementById("mostrar-termos");

if (agregarElemento.style.display === "none") {
    agregarElemento.style.display = "block";
    toggleButton.textContent = "Mostrar menos";
} else {
    agregarElemento.style.display = "none";
    toggleButton.textContent = "Mostrar más";
}
}


function mostrarMasYerbas() {
    var agregarElemento = document.getElementById("pcts-yerbas");
var toggleButton = document.getElementById("mostrar-yerbas");

if (agregarElemento.style.display === "none") {
    agregarElemento.style.display = "block";
    toggleButton.textContent = "Mostrar menos";
} else {
    agregarElemento.style.display = "none";
    toggleButton.textContent = "Mostrar más";
}
}