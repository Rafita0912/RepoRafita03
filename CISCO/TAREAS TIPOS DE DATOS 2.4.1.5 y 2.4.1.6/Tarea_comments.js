"use strict"; 
 
const prefix = "username_"; 
 
let userName = "Jack"; 
// const userName = "Adam"; no puede haber constante igual a variable
 
let prefixedUserName; 
// const prefixedUserName; no puede haber constante igual a variable
 
userName = "John"; 
prefixedUserName = prefix + userName; 
 
console.log(prefixedUserName/*+ prefixedUserName2*/); /*  no existe prefixedUserName2 */
// console.log(prefixedUserName2); no existe prefixedUserName2