let contactos = [{
    nombre: "Maxwell Wright",
    telefono: "(0191) 719 6495",
    correo: "Curabitur.egestas.nunc@nonummyac.co.uk"
    }, {
    nombre: "Raja Villarreal",
    telefono: "0866 398 2895",
    correo: "posuere.vulputate@sed.com"
    }, {
    nombre: "Helen Richards",
    telefono: "0800 1111",
    correo: "libero@convallis.edu"
    }];
    console.log("contacto 1 = nombre = ", contactos[0].nombre," telefono = ",contactos[0].telefono," correo electronico = ",contactos[0].correo)
    console.log("contacto 2 = nombre = ", contactos[1].nombre," telefono = ",contactos[1].telefono," correo electronico = ",contactos[1].correo)
    console.log("contacto 3 = nombre = ", contactos[2].nombre," telefono = ",contactos[2].telefono," correo electronico = ",contactos[2].correo)

    contactos.push({
        nombre: "Maisie Haley",
        telefono: "0913 531 3030",
        correo: "risus.Quisque@urna.ca"
    })
    console.log("contacto 4 = nombre = ", contactos[3].nombre," telefono = ",contactos[3].telefono," correo electronico = ",contactos[3].correo)

    console.log("contacto 1 = nombre = ", contactos[0].nombre," telefono = ",contactos[0].telefono," correo electronico = ",contactos[0].correo)
    console.log("contacto ",(contactos.length-1)," = nombre = ", contactos[contactos.length-1].nombre," telefono = ",contactos[contactos.length-1].telefono," correo electronico = ",contactos[contactos.length-1].correo)
