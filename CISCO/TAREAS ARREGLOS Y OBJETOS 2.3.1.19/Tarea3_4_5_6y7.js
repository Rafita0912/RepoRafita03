let libros = [{
    titulo: "Speaking JavaScript",
    autor: "Axel Rauschmayer",
    paginas: 460,
    },
    {
    titulo: "ProgramingJavaScript Aplications",
    autor: "Eric Elliot",
    paginas: 254,
    },
    {
    titulo: "Understanding ECMAScript 6",
    autor: "Nicholas C. Zakas",
    paginas: 352,
    }]
    console.log("libro 1 : titulo = ", libros[0].titulo,"  autor = ",libros[0].autor," cantidad de paginas = ",libros[0].paginas)
    console.log("libro 2 : titulo = ", libros[1].titulo,"  autor = ",libros[1].autor," cantidad de paginas = ",libros[1].paginas)
    console.log("libro 3 : titulo = ", libros[2].titulo,"  autor = ",libros[2].autor," cantidad de paginas = ",libros[2].paginas)
    libros.push({
        titulo: "Learning JavaScript Design Patterns",
        autor: "Addy Osmani",
        paginas: 254,   
    })
    console.log("libro 4 : titulo = ", libros[3].titulo,"  autor = ",libros[3].autor," cantidad de paginas = ",libros[3].paginas)
    console.log(libros.length)
    console.log("libro 1 : titulo = ", libros[0].titulo)
    console.log("libro 2 : titulo = ", libros[1].titulo)
    console.log("libro 3 : titulo = ", libros[2].titulo)
    console.log("libro 4 : titulo = ", libros[3].titulo)

    let librangos = libros.slice(1,3)
    console.log("libro 1 de la nueva coleccion : titulo = ", librangos[0].titulo,"  autor = ",librangos[0].autor," cantidad de paginas = ",librangos[0].paginas)
    console.log("libro 2 de la nueva coleccion : titulo = ", librangos[1].titulo,"  autor = ",librangos[1].autor," cantidad de paginas = ",librangos[1].paginas)
    let lbroPerdido = libros.shift()
    console.log(libros.length)
