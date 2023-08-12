let numbers = [21, 45, 100, 12, 11, 78, 61, 4, 39, 22];
let numero = numbers.length;
console.log(numero);
for (let i = 0; i <= (numero - 1); i += 1); {
    if (numbers[i] >= 10 && numbers[i] <= 60) {
        console.log(numbers[i]);
    }
}