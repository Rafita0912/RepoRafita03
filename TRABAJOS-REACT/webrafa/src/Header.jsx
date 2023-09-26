import React from 'react'
import './Header.css'

function Header() {
  return (
    <>
        <div class="ancho">
            <div class="logo">
                <p> <a href="https://localhost:5174">Rafael Antequera Caballero</a></p>
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
    </>
  )
}

export default Header