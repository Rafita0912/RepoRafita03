for (i = 100; i >= 0; i = i - 10) {
    console.log(i);
}


let limiteSuperior = Number(prompt("Ingresa limite superior"));
let limiteInferior = Number(prompt("Ingresa limite inferior"));
if (!Number.isNaN(limiteSuperior) && !Number.isNaN(limiteInferior) && limiteSuperior > limiteInferior) {
    for (i = limiteSuperior; i >= limiteInferior; i -= 10) {
        console.log(i);
    }
}

let numeros = [21, 45, 100, 12, 11, 78, 61, 4, 39, 22];
let numero = numeros.length;
console.log(numero);
console.log(numeros[3]);
let i=0;
for (i = 0; i <= (numero - 1); i = i + 1) {
    console.log(numeros[i]);
}

let numbers = [21, 45, 100, 12, 11, 78, 61, 4, 39, 22];
let numero = numbers.length;
console.log(numero);
let i=0
for (i = 0; i <= (numero - 1); i += 1) {
    if (numbers[i] % 2 === 0) {
        console.log(numbers[i]);
    }
}

let numbers = [21, 45, 100, 12, 11, 78, 61, 4, 39, 22];
let numero = numbers.length;
console.log(numero);
for (let i = 0; i <= (numero - 1); i += 1) {
    if (numbers[i] >= 10 && numbers[i] <= 60) {
        console.log(numbers[i]);
    }
}

let peliculas = [];
while (true) {
    let titulo = prompt("Ingresa el título de la película");
    let valoracion = prompt("Ingresa la calificación de la película (imdb)");
    if (titulo === null || valoracion === null) {
        break
    } else {
        peliculas.push({
            titulo: titulo,
            valoracion: Number(valoracion)
        });
    }
}

console.log("Películas con calificaciones inferiores a 7:");
for ( peli of peliculas) {
    if (peli.valoracion < 7) {
        console.log(`${peli.titulo} (${peli.valoracion})`);
    }
}

console.log("Películas con calificaciones inferiores a 7:");
for ( peli of peliculas) {
    if (peli.valoracion >= 7) {
        console.log(`${peli.titulo} (${peli.valoracion})`);
    }
}

let vessel = {
    LATITUD: 40.07288,
    LONGITUD: 154.48535,
    CURSO: 285.6,
    VELOCIDAD: 14.0,
    OMI: 9175717,
    NOMBRE: "MARENO"
}
for (let key in vessel) {
    console.log(`${key} -> ${vessel[key]}`);   
}

let Numero1 = Number(prompt("Introduce el primer numero o S para salir : "));
let Numero2 = Number(prompt("Introduce el segundo numero o S para salir: "));
let Oper = prompt("Introduce la operacion que deseas +  -  *  / o S para salir: ");
let resultado;
if (Numero1 === "S" || Numero2 === "S" || Oper === "S") {
    break;
} else {
if (!Number.isNaN(Numero1) && !Number.isNaN(Numero2)){
    switch (Oper) {
        case "+":resultado = Numero1 + Numero2;
        break;
        case "-":resultado = Numero1 - Numero2;
        break;
        case "*":resultado = Numero1 * Numero2;
        break;
        case "/":resultado = Numero1 / Numero2;
        break;
        default: resultado = "Error, operador no registrado";
        }
    } else {
        resultado = "los valores introducidos no son numeros";
        }
    alert(resultado);
    }