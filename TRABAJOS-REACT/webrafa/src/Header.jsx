import React from 'react'
import './Header.css'

function Header() {
  return (
    <>
    <header>
        <div class="ancho1">
            <div class="logo1">
                <p> <a href="./App.jsx">Rafael Antequera Caballero</a></p>
            </div>
            <nav>
                <ul>
                    <li> <a href="./App.jsx">Inicio</a></li>
                    <li> <a href="./Experiencia.jsx">Experiencia</a></li>
                    <li> <a href="./Formacion.jsx">Formación</a></li>
                    <li> <a href="./Contacto.jsx">Contacto</a></li>
                </ul>
            </nav>
        </div>
    </header>
    </>
  )
}

export default Header