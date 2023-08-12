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

let numbers = [21, 45, 100, 12, 11, 78, 61, 4, 39, 22];
let number = numbers.length;
console.log(number);
console.log(numbers[3]);
for (let i = 0; i <= (number - 1); i = i + 1); {
    console.log(numbers[i]);
}

let numbers = [21, 45, 100, 12, 11, 78, 61, 4, 39, 22];
let numero = numbers.length;
console.log(numero);
for (let i = 0; i <= (numero - 1); i += 1); {
    if (numbers[i] % 2 === 0) {
        console.log(numbers[i]);
    }
}

let numbers = [21, 45, 100, 12, 11, 78, 61, 4, 39, 22];
let numero = numbers.length;
console.log(numero);
for (let i = 0; i <= (numero - 1); i += 1); {
    if (numbers[i] >= 10 && numbers[i] <= 60) {
        console.log(numbers[i]);
    }
}