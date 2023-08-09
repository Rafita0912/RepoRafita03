let num = prompt("introduce un numero cualquiera : ");
if (num >90 && num<110) {
    alert("!BINGO ...... ESTA DENTRO DEL RANGO ...");
    } else {
    alert("FALLASTE .... PUEDES INTENTAR NUEVAMENTE SI ASI LO DESEAS ....");    
        }
        
let num1 = prompt("introduce un numero cualquiera : ");
let message = (num1 >90 && num1<110) ? "!BINGO ...... ESTA DENTRO DEL RANGO ..." : "FALLASTE .... PUEDES INTENTAR NUEVAMENTE SI ASI LO DESEAS ....";
alert(message)

let Numero1 = Number(prompt("Introduce el primer numero : "));
let Numero2 = Number(prompt("Introduce el segundo numero : "));
let Oper = prompt("Introduce la operacion que deseas +  -  *  / : ");
let resultado;
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