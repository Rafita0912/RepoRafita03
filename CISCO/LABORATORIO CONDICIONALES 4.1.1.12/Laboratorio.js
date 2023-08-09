let contacts = [{
    name: "Maxwell Wright",
    phone: "(0191) 719 6495",
    email: "egestas@nonummyac.co.uk"
}, {
    name: "Raja Villarreal",
    phone: "0866 398 2895",
    email: "posuere@sed.com"
}, {
    name: "Helen Richards",
    phone: "0800 1111",
    email: "libero@vallis.edu"
}];

// escribe tu código aquí

let opcion = Number(prompt("introduzca la opcion de su preferencia :  1 ==> ver primer contacto, 2==> ver el ultimo contacto, 3 ==> anadir nuevo contacto"));

switch (opcion) {
    case 1:
    console.log(`${contacts[0].name} / ${contacts[0].phone} / ${contacts[0].email}`);
    break;
    case 2:
    let last = contacts.length - 1;
    console.log(`${contacts[last].name} / ${contacts[last].phone} / ${contacts[last].email}`);
    break;
    case 3:
    let tam = contacts.length;
    contacts.name[tam] = prompt("introduzca nuevo nombre de contacto : ", "nombre");
    contacts.phone[tam] = prompt("introduzca nuevo telefono de contacto : ", "telefono");
    contacts.email[tam] = prompt("introduzca nuevo email de contacto : ", "email");
    break
    default:
    console.log("esta no es una opcion valida")
}