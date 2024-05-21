from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from tkinter import Tk, mainloop, OptionMenu, Label, StringVar, Entry, Button, Spinbox
from PIL import ImageTk, Image
from datetime import datetime

import sqlite3
conn = sqlite3.connect("database_proyecto.db")
cursor = conn.cursor()

import os
os.getcwd()

global inicia, acum, mp, util1, util2, nombre, contra, base, altura, cantidad, espesor, color, nvertical, mhorizontal, freno, puertaventana, tecnico, obra, cliente, telefono, direccion, correo, observaciones

inicia = [
    ["codigo ", "codigo original", "descripcion", "unidad", "costoc", "costos", "venta1CF", "venta1CD", "venta2CF", "venta2CD", "observaciones", "ac_cantidad", "ac_metros2", "ac_costoc", "ac_costos", "ac_precio1cf", "ac_precio1cd", "ac_precio2cf", "ac_precio2cd"], ["M1", "M1", "SILICONA TRANSPARENTE, BLANCA O NEGRA", "Tubo", 2.90, 2.90, 3.31, 3.19, 3.46, 3.34, "MAROL 20 Bs. -   -   - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["M2", "M2", "SILICONA ESTRUCTURAL", "Tubo", 6.24, 6.00, 7.11, 6.59, 7.44, 6.90, "MAROL 20 Bs. -   -   - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["M3", "M3", "CINTA MASKING 1/2  Pulg. (ROLLO DE 20)", "Rollo", 0.65, 0.65, 0.75, 0.72, 0.78, 0.75, "Ribepar  -   -   - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["M4", "M4", "U  15 X 15   ( 16X16 ) - ", "Barras", 4.72, 4.72, 5.37, 5.19, 5.63, 5.43, "Alvicruz 4.1 + 15% - 0.954 Kgr./barra - 4.715 $us./barra - 4 puesto S.C.", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["M5", "M5", "U  15 X 25 - 0,20 KG/MT.", "Barras", 6.79, 6.79, 7.74, 7.47, 8.09, 7.81, "Alvicruz 5.9  + 15% - 1.2 Kgr./barra - 6.785 $us./barra - 5.8 puesto S.C.", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["M6", "M6", "TUBO 50 X 50 - 1,037 KG/MT.", "Barras", 48.18, 48.18, 54.89, 53.00, 57.39, 55.41, "Alcoa 6.73 + 15% - 6.222 Kgr./barra - 48.155169 $us./barra - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["M7", "M7", "TUBO 40 X 40 - 0,624 KG/MT.", "Barras", 28.98, 28.98, 33.02, 31.88, 34.52, 33.33, "Alcoa 6.73 + 15% - 3.744 Kgr./barra - 28.976688 $us./barra - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["M8", "M8", "TUBO 80 X 40 - 0,948 KG/MT.", "Barras", 31.40, 31.40, 35.78, 34.54, 37.40, 36.11, "Alvicruz 27.30  + 15% - 5.688 Kgr./barra - 31.395 $us./barra - 26.80 puesto S.C.", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["M9", "M9", "TUBO 60 X 30 - 0,705 KG/MT.", "Barras", 21.16, 21.16, 24.11, 23.28, 25.20, 24.33, "Alvicruz 18.4  + 15% - 4.23 Kgr./barra - 21.16 $us./barra - 18 puesto S.C.", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["M10", "M10", "TUBO 100 X 50 - 1,560 KG/MT.", "Barras", 43.70, 43.70, 49.79, 48.07, 52.05, 50.26, "Alvicruz 38  + 15% - 4.716 Kgr./barra - 43.7 $us./barra - 37.50 puesto S.C.", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["M11", "M11", "FELPA", "Mt lineal", 0.15, 0.15, 0.18, 0.17, 0.18, 0.18, "Indalum -   -   - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["M12", "M12", "REMACHE 4 X 10", "Pza.", 0.03, 0.03, 0.04, 0.04, 0.04, 0.04, "Perbol -   -   - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["M13", "M13", "TARUGOS NO. 6", "Pza.", 0.03, 0.03, 0.04, 0.04, 0.04, 0.04, "Perbol -   -   - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["M14", "M14", "TORNILLOS 8 X 1 1/2 ", "Pza.", 0.03, 0.03, 0.04, 0.04, 0.04, 0.04, "Perbol -   -   - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["M15", "M15", "TORNILLOS 8 X 1/2 ", "Pza.", 0.02, 0.02, 0.03, 0.03, 0.03, 0.03, "Perbol -   -   - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["M16", "M16", "TUBO GALVANIZADO DE 4 Pulg. ", "Mt lineal", 26.25, 25.20, 29.91, 27.72, 31.27, 28.98, "Las Lomas ( 150+5 por ciento uniones) -   -   - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V1", "V1", "VIDRIO TEMPLADO 10MM INCOLORO", "Mt²", 31.5, 31.5, 35.89, 34.65, 37.52, 36.23, "MURANO 26 + 5 por ciento desp. - cbba - 180 - 25.83 - santa puej - 209.1 - 30", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V2", "V2", "VIDRIO TEMPLADO 8MM INCOLORO", "Mt²", 30.45, 30.45, 34.7, 33.5, 36.27, 35.02, "MURANO 25 + 5 por ciento desp - cbba - 175 - 25.11 - santa puej - 202.13 - 29", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V3", "V3", "VIDRIO TEMPLADO 6MM INCOLORO", "Mt²", 26.00, 25.00, 29.63, 27.5, 30.97, 28.75, "Revibol - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V4", "V4", "VIDRIO TEMPLADO 5MM INCOLORO", "Mt²", 24.00, 24.00, 27.35, 26.4, 28.59, 27.6, "Revibol - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V5", "V5", "VIDRIO TEMPLADO 4MM INCOLORO", "Mt²", 21.00, 21.00, 23.93, 23.10, 25.02, 24.15, "Revibol - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V6", "V6", "VIDRIO TEMPLADO 10MM COLOR", "Mt²", 40.95, 40.95, 46.66, 45.05, 48.78, 47.10, "MURANO 39 + 5 por ciento desp. - cbba -  - 38.7931034482759 - santa puej - 270 - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V7", "V7", "VIDRIO TEMPLADO 8MM COLOR", "Mt²", 39.90, 39.90, 45.46, 43.89, 47.53, 45.89, "MURANO 38 + 5 por ciento desp. - cbba -  - 37.3563218390805 - santa puej - 260 - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V8", "V8", "VIDRIO TEMPLADO 6MM COLOR", "Mt²", 42.00, 40.00, 47.85, 44.00, 50.03, 46.00, "Revibol - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V9", "V9", "VIDRIO TEMPLADO 5MM COLOR", "Mt²", 40.00, 38.00, 45.58, 41.80, 47.65, 43.70, "Revibol - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V10", "V10", "VIDRIO TEMPLADO 4MM COLOR", "Mt²", 38.00, 36.00, 43.30, 39.60, 45.27, 41.40, "Revibol - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V11", "V11", "VIDRIO TEMPLADO CATEDRAL 10MM INCOLORO", "Mt²", 44.00, 44.00, 50.13, 48.40, 52.41, 50.60, "Revibol - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V12", "V12", "VIDRIO TEMPLADO CATEDRAL 10MM COLOR", "Mt²", 46.00, 46.00, 52.41, 50.60, 54.79, 52.90, "Revibol - cbba -  -  - santa puej -  - nuevos", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V13", "V13", "CABEZAL, TAPA, GUIA, TAPA-GUIA 1.998 KG/MT", "Barras", 56.87, 56.87, 64.79, 62.56, 67.74, 65.40, "Alvicruz 49.45+ 15 por ciento desp. - cbba - 11.988 - Kgr./juego - santa puej - 56.8675 - $us./barra47.45 puesto S.C.", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V14", "V14", "VEDAPRES 001 - H DE ALUMINIO", "Barras", 8.63, 8.63, 9.83, 9.49, 10.28, 9.93, "Alvicruz 7.25+ 15 por ciento desp. - cbba - 1.542 - Kgr./barra - santa puej - 8.625 - $us./barra7.15 puesto S.C.", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V15", "V15", "VEDAPRES 002 - U DE ALUMINIO", "Barras", 5.18, 5.18, 5.90, 5.70, 6.17, 5.96, "Alvicruz 4.30+ 15 por ciento desp. - cbba - 0.906 - Kgr./barra - santa puej - 5.175 - $us./barra4.20 puesto S.C.", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V16", "V16", "VEDAPRES 003 - H (2,10MT/BARRA) INC.", "Barras", 5.25, 5.00, 5.99, 5.5, 6.26, 5.75, "Florencio Rivero - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V17", "V17", "VEDAPRES 001 - H (2,10MT/BARRA) BCE.", "Barras", 5.25, 5.00, 5.99, 5.50, 6.26, 5.75, "Florencio Rivero - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V18", "V18", "VEDAPRES 002 - UC (2,10MT/BARRA) BCE.", "Barras", 5.25, 5.00, 5.99, 5.50, 6.26, 5.75, "Florencio Rivero - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V19", "V19", "VEDAPRES 003 - H (2,10MT/BARRA) BCE.", "Barras", 5.25, 5.00, 5.99, 5.50, 6.26, 5.75, "Florencio Rivero - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V20", "V20", "FRENO HIDRÁULICO DORMA", "Pza.", 89.25, 85.00, 101.69, 93.50, 106.31, 97.75, "Florencio Rivero - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V21", "V21", "FRENO HIDRÁULICO HYH", "Pza.", 70.00, 70.00, 79.75, 77.00, 83.38, 80.50, "Cristembo La Paz - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V22", "V22", "MANIJONES DE VIDRIO", "Pza.", 3.00, 3.00, 3.42, 3.30, 3.58, 3.45, "Revibol - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V23", "V23", "1003 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 2.55, 2.55, 2.91, 2.81, 3.04, 2.94, "Alvicruz + 0.15 transp - cbba -  - 2.4 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V24", "V24", "1013 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 3.15, 3.15, 3.59, 3.47, 3.76, 3.63, "Alvicruz + 0.15 transp - cbba -  - 3 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V25", "V25", "1038 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 1.15, 1.15, 1.32, 1.27, 1.37, 1.33, "Alvicruz + 0.15 transp - cbba -  - 1 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V26", "V26", "1038-C ( CROMADO Ó BRONCE VIEJO )", "Pza.", 1.15, 1.15, 1.32, 1.27, 1.37, 1.33, "Alvicruz + 0.15 transp - cbba -  - 1 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V27", "V27", "1101 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 7.65, 7.65, 8.72, 8.42, 9.12, 8.80, "Alvicruz + 0.15 transp - cbba -  - 7.5 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V28", "V28", "1103 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 8.65, 8.65, 9.86, 9.52, 10.31, 9.95, "Alvicruz + 0.15 transp - cbba -  - 8.5 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V29", "V29", "1114 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 6.95, 6.95, 7.92, 7.65, 8.28, 8.00, "Alvicruz + 0.15 transp - cbba -  - 6.8 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V30", "V30", "1115 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 6.95, 6.95, 7.92, 7.65, 8.28, 8.00, "Alvicruz + 0.15 transp - cbba -  - 6.8 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V31", "V31", "1117 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 21.15, 21.15, 24.10, 23.27, 25.20, 24.33, "Alvicruz + 0.15 transp - cbba -  - 21 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V32", "V32", "1123 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 3.65, 3.65, 4.16, 4.02, 4.35, 4.20, "Alvicruz + 0.15 transp - cbba -  - 3.5 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V33", "V33", "1125 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 0.70, 0.70, 0.80, 0.77, 0.84, 0.81, "Alvicruz + 0.15 transp - cbba -  - 0.55 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V34", "V34", "1125-A ( CROMADO Ó BRONCE VIEJO )", "Pza.", 2.35, 2.35, 2.68, 2.59, 2.80, 2.71, "Alvicruz + 0.15 transp - cbba -  - 2.2 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V35", "V35", "1201 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 1.55, 1.55, 1.77, 1.71, 1.85, 1.79, "Alvicruz + 0.15 transp - cbba -  - 1.4 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V36", "V36", "1203 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 9.15, 9.15, 10.43, 10.07, 10.9, 10.53, "Alvicruz + 0.15 transp - cbba -  - 9 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V37", "V37", "1209 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 11.15, 11.15, 12.71, 12.27, 13.29, 12.83, "Alvicruz + 0.15 transp - cbba -  - 11 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V38", "V38", "1230 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 2.95, 2.95, 3.37, 3.25, 3.52, 3.40, "Alvicruz + 0.15 transp - cbba -  - 2.8 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V39", "V39", "1302 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 3.65, 3.65, 4.16, 4.02, 4.35, 4.20, "Alvicruz + 0.15 transp - cbba -  - 3.5 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V40", "V40", "1306 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 5.65, 5.65, 6.44, 6.22, 6.73, 6.50, "Alvicruz + 0.15 transp - cbba -  - 5.5 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V41", "V41", "1310 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 7.15, 7.15, 8.15, 7.87, 8.52, 8.23, "Alvicruz + 0.15 transp - cbba -  - 7 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V42", "V42", "1316 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 8.95, 8.95, 10.20, 9.85, 10.67, 10.30, "Alvicruz + 0.15 transp - cbba -  - 8.8 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V43", "V43", "1319 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 20.15, 20.15, 22.96, 22.17, 24.01, 23.18, "Alvicruz + 0.15 transp - cbba -  - 20 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V44", "V44", "1329 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 3.65, 3.65, 4.16, 4.02, 4.35, 4.20, "Alvicruz + 0.15 transp - cbba -  - 3.5 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V45", "V45", "1335 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 5.15, 5.15, 5.87, 5.67, 6.14, 5.93, "Alvicruz + 0.15 transp - cbba -  - 5 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V46", "V46", "1335-C ( CROMADO Ó BRONCE VIEJO )", "Pza.", 4.65, 4.65, 5.30, 5.12, 5.54, 5.35, "Alvicruz + 0.15 transp - cbba -  - 4.5 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V47", "V47", "1504 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 1.95, 1.95, 2.23, 2.15, 2.33, 2.25, "Alvicruz + 0.15 transp - cbba -  - 1.8 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V48", "V48", "1510 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 18.15, 18.15, 20.68, 19.97, 21.62, 20.88, "Alvicruz + 0.15 transp - cbba -  - 18 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V49", "V49", "1511 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 9.65, 9.65, 11.00, 10.62, 11.50, 11.10, "Alvicruz + 0.15 transp - cbba -  - 9.5 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V50", "V50", "1511-A ( CROMADO Ó BRONCE VIEJO )", "Pza.", 2.15, 2.15, 2.45, 2.37, 2.57, 2.48, "Alvicruz + 0.15 transp - cbba -  - 2 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V51", "V51", "1520 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 14.15, 14.15, 16.13, 15.57, 16.86, 16.28, "Alvicruz + 0.15 transp - cbba -  - 14 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V52", "V52", "1523 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 6.15, 6.15, 7.01, 6.77, 7.33, 7.08, "Alvicruz + 0.15 transp - cbba -  - 6 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V53", "V53", "1531 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 6.15, 6.15, 7.01, 6.77, 7.33, 7.08, "Alvicruz + 0.15 transp - cbba -  - 6 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V54", "V54", "1629-J ( CROMADO Ó BRONCE VIEJO )", "Pza.", 2.15, 2.15, 2.45, 2.37, 2.57, 2.48, "Alvicruz + 0.15 transp - cbba -  - 2 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V55", "V55", "1629-P ( CROMADO Ó BRONCE VIEJO )", "Pza.", 2.35, 2.35, 2.68, 2.59, 2.80, 2.71, "Alvicruz + 0.15 transp - cbba -  - 2.2 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V56", "V56", "1636-AL ( CROMADO Ó BRONCE VIEJO )", "Pza.", 3.35, 3.35, 3.82, 3.69, 4.00, 3.86, "Alvicruz + 0.15 transp - cbba -  - 3.2 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V57", "V57", "1800 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 6.35, 6.35, 7.24, 6.99, 7.57, 7.31, "Alvicruz + 0.15 transp - cbba -  - 6.2 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V58", "V58", "1800-C ( CROMADO Ó BRONCE VIEJO )", "Pza.", 7.15, 7.15, 8.15, 7.87, 8.52, 8.23, "Alvicruz + 0.15 transp - cbba -  - 7 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V59", "V59", "MANO DE OBRA INSTALACIÒN TEMPLADO", "Mt²", 10.00, 10.00, 11.4, 11.00, 11.92, 11.50, "Hilarion -  8 col.+dis. + 2 tec - cbba -  - 8 - santa puej - Sus/mt2 - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V60", "V60", "HERRAJE ARANA", "Pza.", 60.00, 60.00, 68.36, 66.00, 71.47, 69.00, "ALVICRUZ - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V61", "V61", "SOPORTE HERRAJE - TUBO", "Pza.", 20.00, 19.20, 22.79, 21.12, 23.83, 22.08, "8D La Paz - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V62", "V62", "1318 ( CROMADO Ó BRONCE VIEJO )", "Pza.", 14.60, 14.60, 16.64, 16.06, 17.39, 16.79, "Alvicruz + 0.15 transp - cbba -  - 14.5 - santa puej - puestos S.C. - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V63", "V63", "OTRO", "Pza.", 0, 0, 0, 0, 0, 0, "8D La Paz - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V64", "V64", "OTRO", "Pza.", 0, 0, 0, 0, 0, 0, "8D La Paz - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V65", "V65", "OTRO", "Pza.", 0, 0, 0, 0, 0, 0, "8D La Paz - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V66", "V66", "OTRO", "Pza.", 0, 0, 0, 0, 0, 0, "8D La Paz - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V67", "V67", "OTRO", "Pza.", 0, 0, 0, 0, 0, 0, "8D La Paz - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V68", "V68", "OTRO", "Pza.", 0, 0, 0, 0, 0, 0, "8D La Paz - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V69", "V69", "OTRO", "Pza.", 0, 0, 0, 0, 0, 0, "8D La Paz - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V70", "V70", "OTRO", "Pza.", 0, 0, 0, 0, 0, 0, "8D La Paz - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["V71", "V71", "OTRO", "Pza.", 0, 0, 0, 0, 0, 0, "8D La Paz - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A1", "A1", "ALUMINIO ANODIZADO BRONCE O CHAMPAGNE", "Kgr.", 7.74, 7.43, 8.82, 8.18, 9.22, 8.55, "Alcoa 6.73 + 15 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A2", "A2", "ALUMINIO ANODIZADO NATURAL", "Kgr.", 7.74, 7.43, 8.82, 8.18, 9.22, 8.55, "Alcoa 6.73 + 15 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A3", "A3", "VIDRIO INCOLORORO 3MM", "Mt²", 8.84, 8.84, 10.07, 9.72, 10.53, 10.17, "Oriental 7.68 + 15 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A4", "A4", "VIDRIO INCOLORORO 4MM", "Mt²", 10.91, 10.91, 12.43, 12.00, 13.00, 12.55, "Oriental 9.48 + 15 por ciento - cbba -  -  - santa puej - 9.47449823569479 - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A5", "A5", "VIDRIO INCOLORORO 5MM", "Mt²", 12.38, 12.38, 14.10, 13.62, 14.75, 14.24, "Oriental 10.76 + 15 por ciento - cbba -  -  - santa puej - 10.754835835113 - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A6", "A6", "VIDRIO INCOLORORO 6MM", "Mt²", 16.45, 16.45, 18.74, 18.09, 19.6, 18.92, "Oriental 14.30 + 15 por ciento - cbba -  -  - santa puej - 14.0837135936004 - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A7", "A7", "VIDRIO COLOR 3MM", "Mt²", 11.61, 11.61, 13.22, 12.77, 13.83, 13.36, "Garcia 10.09 + 15 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A8", "A8", "VIDRIO COLOR 4MM", "Mt²", 12.75, 12.75, 14.52, 14.02, 15.19, 14.67, "Oriental 11.08 + 15 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A9", "A9", "VIDRIO COLOR 5MM", "Mt²", 16.48, 16.48, 18.78, 18.13, 19.63, 18.96, "Garcia 14.33 + 15 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A10", "A10", "VIDRIO COLOR 6MM", "Mt²", 19.15, 19.15, 21.82, 21.07, 22.81, 22.03, "Oriental 16.65 + 15 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A11", "A11", "VIDRIO CATEDRAL CLARO", "Mt²", 6.33, 6.08, 7.21, 6.68, 7.54, 7.00, "Revibol - 5.55  + 15 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A12", "A12", "VIDRIO CATEDRAL COLOR", "Mt²", 8.24, 7.91, 9.39, 8.70, 9.82, 9.10, "Revibol - 7.16 + 15 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A13", "A13", "VIDRIO REFLECTIVO BRONCE O GRIS 4MM", "Mt²", 27.6, 26.5, 31.45, 29.15, 32.88, 30.48, "Garcia 24 + 15 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A14", "A14", "VIDRIO REFLECTIVO BRONCE O GRIS 5MM", "Mt²", 27.60, 26.50, 31.45, 29.15, 32.88, 30.48, "Garcia 24 + 15 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A15", "A15", "VIDRIO REFLECTIVO BRONCE O GRIS 6MM", "Mt²", 34.00, 33.00, 38.74, 36.30, 40.50, 37.95, " - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A16", "A16", "VIDRIO REFLECTIVO AZURLITE 4MM", "Mt²", 37.00, 36.00, 42.16, 39.60, 44.07, 41.40, " - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A17", "A17", "VIDRIO REFLECTIVO AZURLITE 5MM", "Mt²", 39.00, 38.00, 44.44, 41.80, 46.46, 43.70, " - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A18", "A18", "VIDRIO REFLECTIVO AZURLITE 6MM", "Mt²", 42.55, 40.85, 48.48, 44.94, 50.69, 46.98, "Garcia 37 + 15 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A19", "A19", "CINTA DOB.CONT. 4972 - 3M 1/2 Pulg.=12MM (ROLLO DE 20)", "Rollo", 26.20, 24.89, 29.85, 27.38, 31.21, 28.63, "America home center - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A20", "A20", "CINTA DOB.CONT. 4972 - 3M 3/4 Pulg.=19MM (ROLLO DE 20)", "Rollo", 42.00, 39.90, 47.85, 43.89, 50.03, 45.89, "America home center - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A21", "A21", "CINTA DOB.CONT. 4972 - 3M 1 Pulg.=25MM (ROLLO DE 20)", "Rollo", 65.00, 61.75, 74.06, 67.93, 77.42, 71.02, "America home center - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A22", "A22", "FELPA", "Mt lineal", 0.12, 0.12, 0.14, 0.14, 0.15, 0.14, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A23", "A23", "BURLETE", "Mt lineal", 0.30, 0.30, 0.35, 0.33, 0.36, 0.35, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A24", "A24", "PATIN SERIE 25", "Pza.", 1.20, 1.20, 1.37, 1.32, 1.43, 1.38, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A25", "A25", "PATIN SERIE 20", "Pza.", 0.50, 0.50, 0.57, 0.55, 0.60, 0.58, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A26", "A26", "PATIN SERIE 50", "Pza.", 0.40, 0.40, 0.46, 0.44, 0.48, 0.46, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A27", "A27", "PATIN SERIE 4000", "Pza.", 0.40, 0.40, 0.46, 0.44, 0.48, 0.46, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A28", "A28", "PATIN SHOWER DOOR", "Pza.", 0.50, 0.50, 0.57, 0.55, 0.60, 0.58, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A29", "A29", "CIERRE SERIE 20", "Pza.", 1.60, 1.60, 1.83, 1.76, 1.91, 1.84, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A30", "A30", "CIERRE SERIE 25", "Pza.", 3.00, 3.00, 3.42, 3.30, 3.58, 3.45, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A31", "A31", "GUIA EXTERIOR SHOWER DOOR", "Pza.", 0.10, 0.10, 0.12, 0.11, 0.12, 0.12, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A32", "A32", "GUIA SERIE 50", "Pza.", 0.10, 0.10, 0.12, 0.11, 0.12, 0.12, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A33", "A33", "GUIA SERIE 20", "Pza.", 0.10, 0.10, 0.12, 0.11, 0.12, 0.12, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A34", "A34", "GUIA SERIE 25", "Pza.", 0.10, 0.10, 0.12, 0.11, 0.12, 0.12, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A35", "A35", "CELOSIAS 2 ALETAS - 320 MM.", "Par", 13.39, 13.00, 15.26, 14.30, 15.95, 14.95, "Florencio Rivero - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A36", "A36", "CELOSIAS 3 ALETAS - 460 MM.", "Par", 17.51, 17.00, 19.95, 18.70, 20.86, 19.55, "Florencio Rivero - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A37", "A37", "CELOSIAS 4 ALETAS - 600 MM.", "Par", 19.57, 19.00, 22.30, 20.90, 23.31, 21.85, "Florencio Rivero - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A38", "A38", "CELOSIAS 5 ALETAS - 740MM.", "Par", 24.72, 24.00, 28.17, 26.40, 29.45, 27.60, "Florencio Rivero - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A39", "A39", "CELOSIAS 6 ALETAS - 880 MM.", "Par", 26.78, 26.00, 30.52, 28.60, 31.90, 29.90, "Florencio Rivero - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A40", "A40", "CELOSIAS 7 ALETAS - 1000 MM.", "Par", 33.99, 33.00, 38.73, 36.30, 40.49, 37.95, "Florencio Rivero - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A41", "A41", "CELOSIAS 8 ALETAS - 1160 MM.", "Par", 38.11, 37.00, 43.42, 40.70, 45.40, 42.55, "Florencio Rivero - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A42", "A42", "CELOSIAS 9 ALETAS - 1300 MM.", "Par", 46.35, 45.00, 52.81, 49.50, 55.21, 51.75, "Florencio Rivero - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A43", "A43", "BISAGRA SERIE 32 Y 42", "Pza.", 1.80, 1.80, 2.06, 1.98, 2.15, 2.07, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A44", "A44", "BISAGRA SERIE 35", "Pza.", 1.50, 1.50, 1.71, 1.65, 1.79, 1.73, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A45", "A45", "BISAGRA SERIE 45", "Pza.", 2.50, 2.50, 2.85, 2.75, 2.98, 2.88, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A46", "A46", "BRAZO DE APERTURA P/PROYECTANTE 300", "Par", 9.80, 9.80, 11.17, 10.78, 11.68, 11.27, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A47", "A47", "BRAZO DE APERTURA P/PROYECTANTE 400", "Par", 15.05, 15.05, 17.15, 16.56, 17.93, 17.31, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A48", "A48", "BRAZO DE APERTURA P/PROYECTANTE 500", "Par", 18.50, 18.50, 21.08, 20.35, 22.04, 21.28, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A49", "A49", "BRAZO DE APERTURA P/PROYECTANTE 650", "Par", 22.14, 22.14, 25.23, 24.36, 26.38, 25.47, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A50", "A50", "BRAZO DE APERTURA P/PROYECTANTE 900", "Par", 27.42, 27.42, 31.24, 30.17, 32.66, 31.54, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A51", "A51", "BRAZO DE APERTURA P/PROYECTANTE 1200", "Par", 39.58, 39.58, 45.10, 43.54, 47.15, 45.52, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A52", "A52", "MANIJA PARA PROYECTANTE", "Pza.", 3.04, 3.04, 3.47, 3.35, 3.63, 3.50, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A53", "A53", "CHAPA P/PUERTA DE ALUMINIO", "Pza.", 21.20, 20.00, 24.16, 22.00, 25.26, 23.00, "Florencio Rivero - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A54", "A54", "MANO DE OBRA CARPINTERÌA DE ALUMINIO.", "Mt²", 12.72, 10.00, 14.50, 11.00, 15.16, 11.50, "Hilarion ; 7 maestro + 3diseno - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A55", "A55", "MANO DE OBRA FACHADAS, TECHOS Y ESPECIALES", "Mt²", 12.72, 12.00, 14.50, 13.20, 15.16, 13.8, "Hilarion ; 7 maestro + 5diseno - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A56", "A56", "MANO DE OBRA COLOCACIÓN ESPEJOS", "Mt²", 12.72, 12.00, 14.50, 13.20, 15.16, 13.80, "Hilarion  - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A57", "A57", "MANO DE OBRA FABRICACIÓN MALLERAS", "Mt²", 12.72, 10.00, 14.50, 11.00, 15.16, 11.50, "Hilarion ; 7 maestro + 3diseno - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A58", "A58", "MANO DE OBRA COLOCACIÓN CRUDO", "Mt²", 6.36, 6.00, 7.25, 6.60, 7.58, 6.90, "Hilarion 4 - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A59", "A59", "MANO DE OBRA DIVISORES DE AMBIENTE Y CIELOS", "Mt²", 6.36, 6.00, 7.25, 6.60, 7.58, 6.90, "Hilarion 4 - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A60", "A60", "TESADOR PARA PUERTAS 5/16", "Pza.", 4.00, 4.00, 4.56, 4.40, 4.77, 4.60, "Perbol - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A61", "A61", "MALLA MILIMÉTRICA PLÁSTICA", "Mt²", 3.20, 2.86, 3.65, 3.15, 3.82, 3.29, "Ferretería - 20 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A62", "A62", "BISELADO HASTA 2,7 CM", "Mt lineal", 3.00, 3.00, 3.42, 3.30, 3.58, 3.45, "VICOR - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A63", "A63", "ESCUADRA DE ARMADO", "Pza.", 0.15, 0.15, 0.18, 0.17, 0.18, 0.18, "Indalum - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A64", "A64", "VIDRIO ESPEJO INCOLORO 3MM", "Mt²", 10.80, 9.72, 12.31, 10.69, 12.87, 11.18, "Revibol - 9.15 - 8.38 - 18 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A65", "A65", "VIDRIO ESPEJO INCOLORO 4MM", "Mt²", 12.96, 11.67, 14.77, 12.83, 15.44, 13.43, "Revibol - 10.98 - 9.89 - 18 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A66", "A66", "PULIDO DE VIDRIO A MÁQUINA", "Mt lineal", 1.70, 1.70, 1.94, 1.87, 2.03, 1.96, "Revibol - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A67", "A67", "PERFORACIÓN DE VIDRIO", "Hoyo", 5.60, 5.60, 6.38, 6.16, 6.67, 6.44, "Revibol - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A68", "A68", "MANO DE OBRA CELOSÍAS", "Pza.", 9.54, 9.00, 10.87, 9.90, 11.37, 10.35, "Hilarion o Silverio o Octavio 7 - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A69", "A69", "JALADOR PARA MALLERA", "Pza.", 2.00, 1.80, 2.28, 1.98, 2.39, 2.07, " - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A70", "A70", "ANCLAJES DE HIERRO (PZAS.)", "Pza.", 12.00, 12.00, 13.68, 13.20, 14.30, 13.80, " - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A71", "A71", "PERNOS DE EXPANSIÓN (PZAS.)", "Pza.", 3.00, 3.00, 3.42, 3.30, 3.58, 3.45, " - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A72", "A72", "TORNILLO Y TUERCA DE 2 Pulg. (PZAS.)", "Pza.", 1.00, 1.00, 1.14, 1.10, 1.20, 1.15, " - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A73", "A73", "MANO DE OBRA BOX DE BANO RECTO", "Mt²", 21.20, 20.00, 24.16, 22.00, 25.26, 23.00, "Box de  bano recto - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A74", "A74", "MANO DE OBRA BOX DE BANO CURVO", "Mt²", 31.80, 30.00, 36.23, 33.00, 37.88, 34.50, "Box de  bano curvo - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A75", "A75", "MANO DE OBRA FACHADA ESTRUCTURAL PEQUE", "Mt²", 15.90, 15.00, 18.12, 16.50, 18.94, 17.25, "Fachada estructural pequena - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A76", "A76", "MANO DE OBRA FACHADA ESTRUCTURAL GRANDE", "Mt²", 21.20, 20.00, 24.16, 22.00, 25.26, 23.00, "Fachada estructural alta - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A77", "A77", "MANO DE OBRA CARPINTERIA DE ALUMINIO CON TERMOPANEL", "Mt²", 14.84, 14.00, 16.91, 15.40, 17.68, 16.10, "Termopanel - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A78", "A78", "JALADORES PAR SERIE 25", "Pza.", 7.42, 7.00, 8.46, 7.7, 8.84, 8.05, " - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A79", "A79", "ALUCOBOND - WILSTRONG ", "Mt²", 42.60, 42.60, 48.54, 46.86, 50.74, 48.99, "Tecnopor 35.50 + 20 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A80", "A80", "VIDRIO LAMINADO REFLECTIVO GRIS 4+4MM", "Mt²", 55.90, 55.90, 63.69, 61.49, 66.59, 64.29, "CRIS LP 43 + 30 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A81", "A81", "VIDRIO LAMINADO REFLECTIVO AZUL 4+4MM", "Mt²", 59.80, 59.80, 68.13, 65.78, 71.23, 68.77, "CRIS LP 46 + 30 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A82", "A82", "VIDRIO LAMINADO INCOLORO 4+4MM", "Mt²", 31.20, 31.20, 35.55, 34.32, 37.17, 35.88, "CRIS LP 24 + 30 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A83", "A83", "PATIN SERIE 30 + RIEL SUP", "Pza.", 7.42, 7.00, 8.46, 7.70, 8.84, 8.05, " - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A84", "A84", "PANEL CIELO FALSO 122X61", "Mt²", 12.00, 12.00, 13.68, 13.20, 14.30, 13.80, "tecnopor  10 + 20 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A85", "A85", "PANEL CIELO FALSO 61X61", "Mt²", 14.40, 14.40, 16.41, 15.84, 17.16, 16.56, "tecnopor  12 + 20 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A86", "A86", "ALAMBRE GALVANIZADO", "Kgr.", 3.75, 3.75, 4.28, 4.13, 4.47, 4.32, "Las Lomas ( 3+25% ) - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A87", "A87", "ACRILICO", "Mt²", 19.50, 19.50, 22.22, 21.45, 23.23, 22.43, "CRIS LP 15 + 30 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A88", "A88", "VIDRIO LAMINADO REFLECTIVO BRONCE O GRIS 5+5 MM", "Mt²", 69.00, 69.00, 78.62, 75.9, 82.19, 79.35, "CLP 60 + 15 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A89", "A89", "VIDRIO TERMOPANEL DVH INCOLORO 5+5MM + 7 X (2H+2B)", "Mt²", 24.75, 24.75, 28.20, 27.23, 29.48, 28.47, "ALVICRUZ = VID + (7xPERIM.) - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A90", "A90", "VIDRIO LAMINADO INCOLORO 3+3 MM", "Mt²", 28.64, 28.64, 32.63, 31.5, 34.12, 32.94, "ALVICRUZ    24.90 + 15 por ciento - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A91", "A91", "VIDRIO TERMOPANEL DVH INCOLORO 5+6(3+3)MM + 7 X (2H+2B)", "Mt²", 41.01, 41.01, 46.73, 45.11, 48.85, 47.17, "ALVICRUZ = VID + (7xPERIM.) - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A92", "A92", "ALUMINIO  6001", "Mt. Lin.", 6.39, 6.39, 7.28, 7.03, 7.62, 7.35, "ALVICRUZ = 33.32 - cbba -  -  - santa puej - 5.55333333333333 - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A93", "A93", "ALUMINIO  6002", "Mt. Lin.", 2.16, 2.16, 2.46, 2.37, 2.58, 2.49, "ALVICRUZ = 11.22 - cbba -  -  - santa puej - 1.87 - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A94", "A94", "ALUMINIO  6004", "Mt. Lin.", 4.98, 4.98, 5.67, 5.48, 5.94, 5.73, "ALVICRUZ = 25.95 - cbba -  -  - santa puej - 4.325 - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A95", "A95", "ALUMINIO  6005", "Mt. Lin.", 3.09, 3.09, 3.53, 3.40, 3.69, 3.56, "ALVICRUZ = 16.12 - cbba -  -  - santa puej - 2.68666666666667 - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A96", "A96", "JALADORES PAR", "Pza.", 16.00, 15.00, 18.23, 16.5, 19.06, 17.25, " - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A97", "A97", "RODAMIENTO SERIE 60 ALVI", "Pza.", 5.50, 5.50, 6.27, 6.05, 6.56, 6.33, "ALVICRUZ - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A98", "A98", "MANIJA + KIT BIPUNTO SERIE 60 ALVI", "Pza.", 35.00, 35.00, 39.88, 38.50, 41.69, 40.25, "ALVICRUZ - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A99", "A99", "ESMERILADO", "Pza.", 5.00, 5.00, 5.70, 5.50, 5.96, 5.75, "ALVICRUZ - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A100", "A100", "OTRO", "Pza.", 0, 0, 0, 0, 0, 0, "ALVICRUZ - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A101", "A101", "OTRO", "Pza.", 0, 0, 0, 0, 0, 0, "ALVICRUZ - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A102", "A102", "OTRO", "Pza.", 0, 0, 0, 0, 0, 0, "ALVICRUZ - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A103", "A103", "OTRO", "Pza.", 0, 0, 0, 0, 0, 0, "ALVICRUZ - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A104", "A104", "OTRO", "Pza.", 0, 0, 0, 0, 0, 0, "ALVICRUZ - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A105", "A105", "OTRO", "Pza.", 0, 0, 0, 0, 0, 0, "ALVICRUZ - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A106", "A106", "OTRO", "Pza.", 0, 0, 0, 0, 0, 0, "ALVICRUZ - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A107", "A107", "OTRO", "Pza.", 0, 0, 0, 0, 0, 0, "ALVICRUZ - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["A108", "A108", "OTRO", "Pza.", 0, 0, 0, 0, 0, 0, "ALVICRUZ - cbba -  -  - santa puej -  - ", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["TEC", "TEC", "TECNICO", "obra", 0, 0, 0, 0, 0, 0, "sin observaciones", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["OB", "OB", "OBRA  ", "obra", 0, 0, 0, 0, 0, 0, "sin observaciones", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["CL", "CL", "CLIENTE  ", "cliente", 0, 0, 0, 0, 0, 0, "sin observaciones", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["TE", "TE", "TELEFONO  ", "telefono", 0, 0, 0, 0, 0, 0, "sin observaciones", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["DI", "DI", "DIRECCION  ", "direccion", 0, 0, 0, 0, 0, 0, "sin observaciones", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["CO", "CO", "CORREO  ", "correo", 0, 0, 0, 0, 0, 0, "sin observaciones", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["OBS", "OBS", "OBSERVACIONES  ", "observa", 0, 0, 0, 0, 0, 0, "sin observaciones", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PF8", "PF8", "PAÑOS FIJOS CON VIDRIO TEMPLADO INCOLORO DE 8 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PF8C", "PF8C", "PAÑOS FIJOS CON VIDRIO TEMPLADO COLOR DE 8 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PF10", "PF10", "PAÑOS FIJOS CON VIDRIO TEMPLADO INCOLORO DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PF10C", "PF10C", " PAÑOS FIJOS CON VIDRIO TEMPLADO COLOR DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["FTCV8", "FTCV8", "FRENTE TIPO SPYDER CON SOPORTE TUBULAR DE VIDRIO TEMPLADO INCOLORO DE 8 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["FTCV8C", "FTCV8C", "FRENTE TIPO SPYDER CON SOPORTE TUBULAR DE VIDRIO TEMPLADO COLOR DE 8 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["FTTS10", "FTTS10", "FRENTE TIPO SPYDER CON SOPORTE TUBULAR DE VIDRIO TEMPLADO INCOLORO DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["FTTS10C", "FTTS10C", "FRENTE TIPO SPYDER CON SOPORTE TUBULAR DE VIDRIO TEMPLADO COLOR DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["FTCV8", "FTCV8", "FRENTE DE VIDRIO TEMPLADO CON HERRAJES Y VIENTOS INCOLORO DE 8 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["FTCV8C", "FTCV8C", "FRENTE DE VIDRIO TEMPLADO CON HERRAJES Y VIENTOS COLOR DE 8 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["FTCV10", "FTCV10", "FRENTE DE VIDRIO TEMPLADO CON HERRAJES Y VIENTOS INCOLORO DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["FTCV10C", "FTCV10C", "FRENTE DE VIDRIO TEMPLADO CON HERRAJES Y VIENTOS COLOR DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PVC2H8", "PVC2H8", "VENTANAS CORREDIZAS DE 2 HOJAS CON VIDRIO TEMPLADO INCOLORO DE 8 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PVC2H8C", "PVC2H8C", "VENTANAS CORREDIZAS DE 2 HOJAS CON VIDRIO TEMPLADO COLOR DE 8 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PVC2H10", "PVC2H10", "VENTANAS CORREDIZAS DE 2 HOJAS CON VIDRIO TEMPLADO INCOLORO DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PVC2H10C", "PVC2H10C", "VENTANAS CORREDIZAS DE 2 HOJAS CON VIDRIO TEMPLADO COLOR DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PVC2HCF8", "PVC2HCF8", "VENTANAS CORREDIZAS DE 2 HOJAS MAS FIJO CON VIDRIO TEMPLADO INCOLORO DE 8 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PVC2HCF8C", "PVC2HCF8C", "VENTANAS CORREDIZAS DE 2 HOJAS MAS FIJO CON VIDRIO TEMPLADO COLOR DE 8 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PVC2HCF10", "PVC2HCF10", "VENTANAS CORREDIZAS DE 2 HOJAS MAS FIJO CON VIDRIO TEMPLADO INCOLORO DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PVC2HCF10C", "PVC2HCF10C", "VENTANAS CORREDIZAS DE 2 HOJAS MAS FIJO CON VIDRIO TEMPLADO COLOR DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PVC4H8", "PVC4H8", "VENTANAS CORREDIZAS DE 4 HOJAS CON VIDRIO TEMPLADO INCOLORO DE 8 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PVC4H8C", "PVC4H8C", "VENTANAS CORREDIZAS DE 4 HOJAS CON VIDRIO TEMPLADO COLOR DE 8 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PVC4H10", "PVC4H10", "VENTANAS CORREDIZAS DE 4 HOJAS CON VIDRIO TEMPLADO INCOLORO DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PVC4H10C", "PVC4H10C", "VENTANAS CORREDIZAS DE 4 HOJAS CON VIDRIO TEMPLADO COLOR DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PVC4HCF8", "PVC4HCF8", "VENTANAS CORREDIZAS DE 4 HOJAS MAS FIJO CON VIDRIO TEMPLADO INCOLORO DE 8 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PVC4HCF8C", "PVC4HCF8C", "VENTANAS CORREDIZAS DE 4 HOJAS MAS FIJO CON VIDRIO TEMPLADO COLOR DE 8 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PVC4HCF10", "PVC4HCF10", "VENTANAS CORREDIZAS DE 4 HOJAS MAS FIJO CON VIDRIO TEMPLADO INCOLORO DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PVC4HCF10C", "PVC4HCF10C", "VENTANAS CORREDIZAS DE 4 HOJAS MAS FIJO CON VIDRIO TEMPLADO COLOR DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PBS10", "PBS10", "PUERTAS BATIENTES SIMPLE DE VIDRIO TEMPLADO INCOLORO DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PBS10C", "PBS10C", "PUERTAS BATIENTES SIMPLE DE VIDRIO TEMPLADO COLOR DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PBD10", "PBD10", "PUERTAS BATIENTES DOBLE DE VIDRIO TEMPLADO INCOLORO DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PBD10C", "PBD10C", "PUERTAS BATIENTES DOBLE DE VIDRIO TEMPLADO COLOR DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PBDCFL10", "PBDCFL10", "PUERTAS BATIENTES CON FIJOS LATERALES DE VIDRIO TEMPLADO INCOLORO DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PBDCFL10C", "PBDCFL10C", "PUERTAS BATIENTES CON FIJOS LATERALES DE VIDRIO TEMPLADO COLOR DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PBDCFS10", "PBDCFS10", "PUERTAS BATIENTES CON FIJOS SUPERIOR DE VIDRIO TEMPLADO INCOLORO DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PBDCFS10C", "PBDCFS10C", "PUERTAS BATIENTES CON FIJOS SUPERIOR DE VIDRIO TEMPLADO COLOR DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PBDCFLS10", "PBDCFLS10", "PUERTAS BATIENTES CON FIJOS LATERAL Y SUPERIOR DE VIDRIO TEMPLADO INCOLORO DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PBDCFLS10C", "PBDCFLS10C", "PUERTAS BATIENTES CON FIJOS LATERAL Y SUPERIOR DE VIDRIO TEMPLADO COLOR DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PBSCFLS10", "PBSCFLS10", "PUERTAS BATIENTES SIMPLE CON FIJOS LATERAL Y SUPERIOR DE VIDRIO TEMPLADO INCOLORO DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
    ["PBSCFLS10C", "PBSCFLS10C", "PUERTAS BATIENTES SIMPLE CON FIJOS LATERAL Y SUPERIOR DE VIDRIO TEMPLADO COLOR DE 10 mm DE ESPESOR ", "Pza(s).", 0, 0, 0, 0, 0, 0, "Datos para proforma", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]]

acum = inicia
mp = inicia
util1 = 1.10
util2 = 1.15

class login:
    global acum, mp
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("390x560")
        self.ventana.title("Usuario")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)

        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="Introduzca usuario y contraseña", font=("Comic Sans", 16,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=15)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/LOGO_CRISTEMBO.png")
        self.img = self.img.resize((340,100))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand=True, fill="both", side="top", pady=0)

        self.label_usuario = Label(self.frame2, text="USUARIO",font=("Comic Sans", 16,"bold"), bg="#88ff84", fg="black")
        self.label_usuario.grid(row=0, column=0, padx=10, sticky="e")
        self.entry_usuario = Entry(self.frame2, bd=0, width=14, font=("Comic Sans", 16,"bold"))
        self.entry_usuario.grid(row=0, column=1, columnspan=3, padx=5, sticky="w")

        self.label_password = Label(self.frame2, text="CONTRASEÑA",font=("Comic Sans", 16,"bold"), bg="#88ff84", fg="black")
        self.label_password.grid(row=1, column=0, padx=10, sticky="e")
        self.entry_password = Entry(self.frame2, bd=0, width=14, font=("Comic Sans", 16,"bold"), show="*")
        self.entry_password.grid(row=1, column=1, columnspan=3, padx=5, sticky="w")

        self.boton_ingresar = Button(self.frame2, text="INGRESAR", width=12, font=("Comic Sans", 16,"bold"), command=self.entrar)
        self.boton_ingresar.grid(row=2, column=0, columnspan=2, padx=15, pady=35, sticky="w")

        self.boton_ingresar = Button(self.frame2, text="SALIR", width=12, font=("Comic Sans", 16,"bold"), command=self.salir)
        self.boton_ingresar.grid(row=2, column=1, columnspan=2, padx=15, pady=35, sticky="e")

        mainloop()

    def entrar(self):
        global nombre, contra
        nombre = self.entry_usuario.get()
        contra = self.entry_password.get()
        if (nombre == "TECNICO" and contra == "123") or (nombre == "RAFA" and contra == "555"):
            acum = inicia
            mp = inicia
            self.ventana.destroy()
            application=registro()
        else:
            messagebox.showinfo("NO", "ERROR ......... El USUARIO ó la CONTRASEÑA no son correctos, intente nuevamente ........")

    def salir(self):
        self.ventana.destroy()

class registro:
    global acum, mp
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("390x600")
        self.ventana.title("Registro")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)

        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="REGISTRO DE DATOS", font=("Comic Sans", 16,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=15)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/foto_frentes_templado.png")
        self.img = self.img.resize((260,130))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand="True", fill="both", side="top", pady=0)

        self.label_tecnico = Label(self.frame2, text="TECNICO : ",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_tecnico.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_tecnico = Entry(self.frame2, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.entry_tecnico.grid(row=0, column=1, columnspan=3, padx=5, pady=3, sticky="w")

        self.label_obra = Label(self.frame2, text="OBRA : ",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_obra.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_obra = Entry(self.frame2, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.entry_obra.grid(row=1, column=1, columnspan=3, padx=5, pady=3, sticky="w")

        self.label_cliente = Label(self.frame2, text="Cliente :",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_cliente.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_cliente = Entry(self.frame2, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.entry_cliente.grid(row=2, column=1, columnspan=3, padx=5, pady=3, sticky="w")

        self.label_telefono = Label(self.frame2, text="Teléfono : ",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_telefono.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_telefono = Entry(self.frame2, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.entry_telefono.grid(row=3, column=1, columnspan=3, padx=5, pady=3, sticky="w")

        self.label_direccion = Label(self.frame2, text="Dirección : ",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_direccion.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_direccion = Entry(self.frame2, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.entry_direccion.grid(row=4, column=1, columnspan=3, padx=5, pady=3, sticky="w")
        
        self.label_correo = Label(self.frame2, text="Correo Electrónico : ",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_correo.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.entry_correo = Entry(self.frame2, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.entry_correo.grid(row=5, column=1, columnspan=3, padx=5, pady=3, sticky="w")

        self.label_observaciones = Label(self.frame2, text="Observaciones : ",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_observaciones.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.entry_observaciones = Entry(self.frame2, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.entry_observaciones.grid(row=6, column=1, columnspan=3, padx=5, pady=3, sticky="w")

        self.boton_registrar = Button(self.frame2, text="REGISTRAR Y COTIZAR", width=20, font=("Comic Sans", 12,"bold"), command=self.registrar)
        self.boton_registrar.grid(row=7, column=0, columnspan=2, pady=35, padx=10, sticky="w")

        self.boton_salir = Button(self.frame2, text="SALIR", width=12, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=7, column=1, columnspan=2, pady=35, padx=10, sticky="e")

        mainloop()
    
    def salir(self):
        self.ventana.destroy()
        application=login()

    def registrar(self):
        if len(self.entry_tecnico.get()) != 0 and len(self.entry_obra.get()) != 0 and len(self.entry_cliente.get()) != 0 and len(self.entry_telefono.get()) != 0 and len(self.entry_direccion.get()) != 0 and len(self.entry_correo.get()) != 0 and len(self.entry_observaciones.get()) != 0:

            # inicializando listas acumuladas y parciales para calcular costos y registrar
            acum[196][3] = self.entry_tecnico.get()
            acum[197][3] = self.entry_obra.get()
            acum[198][3] = self.entry_cliente.get()
            acum[199][3] = self.entry_telefono.get()
            acum[200][3] = self.entry_direccion.get()
            acum[201][3] = self.entry_correo.get()
            acum[202][3] = self.entry_observaciones.get()

            for i in range(1, 237, 1):
                for j in range(4, 19, 1):
                    acum[i][j] = 0.00
                    mp[i][j] = 0.00

            self.ventana.destroy()
            application=opcion()
        else:
            messagebox.showinfo("NO", "ERROR .... algun dato ingresado no es correcto o no ingresaste algún dato, REVISA por favor e ingresa los datos correctamente.... ")

class opcion:
    global acum, mp
    def __init__(self):        
        self.ventana = Tk()
        self.ventana.geometry("390x700")
        self.ventana.title("Usuario")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand="True")

        self.frame1.columnconfigure(0, weight=1)
        self.frame1.columnconfigure(1, weight=1)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)
        
        self.titulo = Label(self.frame1, text="SELECCIONE LA OPCION A COTIZAR", font=("Comic Sans", 16,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=10)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/opciones_a_cotizar.png")
        self.img = self.img.resize((360,450))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand=0, fill='x', side='top', pady=3)

        self.label_opcion = Label(self.frame2, width=18, text="OPCION : ",font=("Comic Sans", 14,"bold"), bg="#88ff84", fg="black")
        self.label_opcion.grid(row=0, column=0, padx=10, sticky="e")
        self.entry_opcion = Entry(self.frame2, bd=0, width=10, font=("Comic Sans", 16,"bold"))
        self.entry_opcion.grid(row=0, column=1, columnspan=3, padx=5, sticky="w")

        self.boton_cotizar = Button(self.frame2, text="COTIZAR", width=25, font=("Comic Sans", 12,"bold"), command=self.cotizar)
        self.boton_cotizar.grid(row=1, column=0, pady=15, columnspan=1, padx=3, sticky="w")

        self.boton_proforma = Button(self.frame2, text="PROFORMA", width=25, font=("Comic Sans", 12,"bold"), command=self.proforma)
        self.boton_proforma.grid(row=1, column=1, pady=15, columnspan=1, padx=3, sticky="e")

        self.boton_proforma = Button(self.frame2, text="MATERIALES", width=25, font=("Comic Sans", 12,"bold"), command=self.material)
        self.boton_proforma.grid(row=2, column=0, pady=5, columnspan=1, padx=3, sticky="w")

        self.boton_salir = Button(self.frame2, text="SALIR", width=25, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=2, column=1, pady=5, columnspan=1, padx=3, sticky="e")

        mainloop()

    def cotizar(self):
        base = float(0)
        altura = float(0)
        cantidad = int(0)
        espesor = str("")
        color = str("")
        nvertical = int(0)
        mhorizontal = int(0)
        freno = str("")
        puertaventana = str("")

        op = self.entry_opcion.get()

        if op == "1":
            self.ventana.destroy()
            application=op1()

        elif op == "2":
            self.ventana.destroy()
            application=op2()

        elif op == "3":
            self.ventana.destroy()
            application=op3()

        elif op == "4":
            self.ventana.destroy()
            application=op4()

        elif op == "5":
            self.ventana.destroy()
            application=op5()

        elif op == "6":
            self.ventana.destroy()
            application=op6()

        elif op == "7":
            self.ventana.destroy()
            application=op7()

        elif op == "8":
            self.ventana.destroy()
            application=op8()

        elif op == "9":
            self.ventana.destroy()
            application=op9()

        elif op == "10":
            self.ventana.destroy()
            application=op10()

        elif op == "11":
            self.ventana.destroy()
            application=op11()

        elif op == "12":
            self.ventana.destroy()
            application=op12()

        elif op == "13":
            self.ventana.destroy()
            application=op13()

        elif op == "14":
            self.ventana.destroy()
            application=op14()

        else:
            messagebox.showinfo("NO", "ERROR ...... algun dato ingresado no es correcto o no ingresaste la opcion ..... intenta nuevamente ....")
    
    def proforma(self):
        print("FACTURA PROFORMA \n TECNICO : ",acum[196][3], "            OBRA : =",acum[197][3], " \n CLIENTE : ",acum[198][3], "            TELEFONO : ",acum[199][3], " \n DIRECCION : ",acum[200][3], "        CORREO : ",acum[201][3], " \n OBSERVACIONES : ",acum[202][3], " \n PRODUCTO               ==>  CANTIDAD     UNIDAD     SUPERFICIE   MT2   COSTO M.O    COSTO ACC.   COSTO VIDRIO     COSTO TOTAL")
        for i in range(203, 237, 1):
            if acum[i][4] > 0:
                print(acum[i][2], " ==> ",acum[i][4], "  ",acum[i][3], " ==> ",acum[i][5], "  Mt2   ", (round((acum[i][6]*util1*0.87/0.84), 2)), " $us. ",(round((acum[i][7]*util1*0.87/0.84), 2)), " $us.", (round((acum[i][8]*util1*0.87/0.84), 2)), " $us.", (round((acum[i][9]*util1*0.87/0.84), 2)), " $us. ")

        self.ventana.destroy()
        application=opcion()

    def material(self):
        if nombre == "RAFA" and contra == "555":
            for i in range(1, 196, 1):
                if acum[i][11] > 0:
                    print(acum[i][2], " = ",acum[i][11], "  ",acum[i][3] , " ")

            self.ventana.destroy()
            application=opcion()

        else:
            messagebox.showinfo("NO", "ERROR ......... Este USUARIO solo puede ver e imprimir la PROFORMA, el detalle de materiales solo puede ser visto por el ADMINISTRADOR, seleccione la opción correcta ........")
            
    def salir(self):
        self.ventana.destroy()
        application=login()

class op1:
    global acum, mp
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("380x740")
        self.ventana.title("Op1")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="FRENTE TEMPLADO \n TIPO SPYDER", font=("Comic Sans", 14,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=15)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/op1a.png")
        self.img = self.img.resize((260,260))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand="True", fill="both", side="top", pady=0)

        self.label_base = Label(self.frame2, text="BASE en metros : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_base.grid(row=0, column=0, padx=5, pady=3, sticky="e")
        self.entry_base = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_base.grid(row=0, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.label_altura = Label(self.frame2, text="ALTURA en metros :",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_altura.grid(row=1, column=0, padx=5, pady=3, sticky="e")
        self.entry_altura = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_altura.grid(row=1, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_cantidad = Label(self.frame2, text="CANTIDAD : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_cantidad.grid(row=2, column=0, padx=5, pady=3, sticky="e")
        self.entry_cantidad = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_cantidad.grid(row=2, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_espesor = Label(self.frame2, text="ESPESOR en mm. = 8   ó   10  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_espesor.grid(row=3, column=0, padx=5, pady=3, sticky="e")
        self.espesor_v = StringVar()
        self.lista1 = ["8 mm", "10 mm"]
        self.opciones1 = OptionMenu(self.frame2, self.espesor_v, *self.lista1)
        self.opciones1.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.espesor_v.set("???????")
        self.opciones1.grid(row=3, column=1, padx=5, pady=3, sticky="e")

        self.label_color = Label(self.frame2, text="VIDRIO INCOLORO ó COLOR  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_color.grid(row=4, column=0, padx=5, pady=3, sticky="e")
        self.color_v = StringVar()
        self.lista2 = ["Incoloro", "Color"]
        self.opciones2 = OptionMenu(self.frame2, self.color_v, *self.lista2)
        self.opciones2.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.color_v.set("???????")
        self.opciones2.grid(row=4, column=1, padx=5, pady=3, sticky="e")

        self.label_nvertical = Label(self.frame2, text="N DIV. VERTICALES : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_nvertical.grid(row=5, column=0, padx=5, pady=3, sticky="e")
        self.entry_nvertical = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_nvertical.grid(row=5, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_mhorizontal = Label(self.frame2, text="M DIV. HORIZONTALES : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_mhorizontal.grid(row=6, column=0, padx=5, pady=3, sticky="e")
        self.entry_mhorizontal = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_mhorizontal.grid(row=6, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.boton_cotizar = Button(self.frame2, text="COTIZAR Y SEGUIR", width=18, font=("Comic Sans", 11,"bold"), command=self.cotizar)
        self.boton_cotizar.grid(row=8, column=0, pady=15, columnspan=1, padx=25, sticky="w")

        self.boton_salir = Button(self.frame2, text="SALIR", width=18, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=8, column=1, pady=15, columnspan=1, padx=10, sticky="ew")

        mainloop()
    
    def salir(self):
        self.ventana.destroy()
        application=login()

    def cotizar(self):
        if len(self.entry_base.get()) != 0 and len(self.entry_altura.get()) != 0 and len(self.entry_cantidad.get()) != 0 and len(self.entry_nvertical.get()) != 0 and len(self.entry_mhorizontal.get()) != 0 and len(self.espesor_v.get()) != 0 and len(self.color_v.get()) != 0:
            while True:
                try:
                    x = float(self.entry_base.get())
                    y = float(self.entry_altura.get())
                    break

                except ValueError:
                
                    messagebox.showinfo("NO", "ERROR ....... La medida de la BASE ó ALTURA no son correctas, revise los doatos ingresados e introduzca nuevamente los valores .... RECUERDE LA SEPARACION DECIMAL ES CON PUNTO . ")
                    return(False)
                
            while True:
                try:
                    x = int(self.entry_cantidad.get())
                    y = int(self.entry_nvertical.get())
                    z = int(self.entry_mhorizontal.get())  
                    break

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... La CANTIDAD O LAS DIVISIONES, no son correctas, revise los datos ingresados e introduzca nuevamente los valores correctos.... RECUERDE QUE DEBEN SER NUMEROS SIN DECIMALES")
                    return(False)
                
            while True:
                try:
                    x = str(self.espesor_v.get())
                    y = str(self.color_v.get())
                    if x == "8 mm" or x == "10 mm":
                        if y == "Incoloro" or y == "Color":
                            break
                        else:
                            return(False)
                    else:
                        return(False)

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... El ESPESOR Y EL COLOR DEBEN SER SELECCIONADOS, revise si fueron seleccionados y seleccione la opcion deseada...")
                    return(False)
                
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            cantidad = int(self.entry_cantidad.get())
            espesor = self.espesor_v.get()
            color = self.color_v.get()
            nvertical = int(self.entry_nvertical.get())
            mhorizontal = int(self.entry_mhorizontal.get())

            mp = inicia
            
            for i in range(1, 237, 1):
                for j in range(11, 19, 1):
                    mp[i][j] = 0.00

            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    mp[i][j] = 0.00

            mp[196][3] = acum[196][3]
            mp[197][3] = acum[197][3]
            mp[198][3] = acum[198][3]
            mp[199][3] = acum[199][3]
            mp[200][3] = acum[200][3]
            mp[201][3] = acum[201][3]
            mp[202][3] = acum[202][3]

            if espesor == "8 mm":
                if color == "Incoloro":
                    mp[18][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[18][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[18][13] = round((mp[18][12] * mp[18][4]), 2) #costo del vidrio templado con factura
                    mp[18][14] = round((mp[18][12] * mp[18][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[18][13], 2)

                elif color == "Color":

                    mp[23][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[23][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[23][13] = round((mp[23][12] * mp[23][4]), 2) #costo del vidrio templado con factura
                    mp[23][14] = round((mp[23][12] * mp[23][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[23][13], 2)

            elif espesor == "10 mm":
                if color == "Incoloro":
                    mp[17][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[17][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[17][13] = round((mp[17][12] * mp[17][4]), 2) #costo del vidrio templado con factura
                    mp[17][14] = round((mp[17][12] * mp[17][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[17][13], 2)

                elif color == "Color":
                    mp[22][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[22][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[22][13] = round((mp[22][12] * mp[22][4]), 2) #costo del vidrio templado con factura
                    mp[22][14] = round((mp[22][12] * mp[22][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[22][13], 2)                

            mp[75][11] = round((cantidad * base * altura), 2)
            mp[75][12] = mp[75][11]
            mp[75][13] = round((mp[75][11] * mp[75][4]), 2)  #costo mano de obra con factura
            mp[75][14] = round((mp[75][11] * mp[75][5]), 2)  #costo mano de obra con descuento
            
            mp[1][11] = round((( cantidad * ((4 * base) + (4 * altura) + ((nvertical-1) * altura) + ((mhorizontal-1) * base))) / 6), 2) # cantidad de silicona normal
            mp[1][13] = round((mp[1][4] * mp[1][11]), 2) #costo silicona natural con factura
            mp[1][14] = round((mp[1][5] * mp[1][11]), 2) #costo silicona natural con descuento
            
            mp[3][11] = round(((cantidad * ((4 * base) + (4 * altura) + ((nvertical-1) * altura) + ((mhorizontal-1) * base))) * 2 / 20), 2) # cantidad de cinta masking
            mp[3][13] = round((mp[3][4] * mp[3][11]), 2) #costo cinta masking con factura
            mp[3][14] = round((mp[3][5] * mp[3][11]), 2) #costo cinta masking con descuento  
            
            mp[5][11] = round((cantidad * ((2 * base) + (2 * altura)) / 6), 2) # cantidad de perfil U 15 x 25 incoloro o bronce
            mp[5][13] = round((mp[5][4] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con factura
            mp[5][14] = round((mp[5][5] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con descuento

            mp[14][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tornillo de 8 x 1 1/2
            mp[14][13] = round((mp[14][4] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con factura
            mp[14][14] = round((mp[14][5] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con descuento

            mp[13][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tarugos No. 6
            mp[13][13] = round((mp[13][4] * mp[13][11]), 2) #costo de tarugos No. 6 con factura
            mp[13][14] = round((mp[13][5] * mp[13][11]), 2) #costo de tarugos No. 6 con descuento

            mp[16][11] = round((cantidad * ((nvertical - 1) * altura)), 2) # cantidad de tubo galvanizado de 4 pulg.
            mp[16][13] = round((mp[16][4] * mp[16][11]), 2) #costo de tubo galvanizado de 4 pulg. con factura
            mp[16][14] = round((mp[16][5] * mp[16][11]), 2) #costo de tubo galvanizado de 4 pulg. con descuento

            mp[76][11] = round((cantidad * (nvertical - 1) * (mhorizontal - 1)), 2) # cantidad de herrajes araña
            mp[76][13] = round((mp[76][4] * mp[76][11]), 2) #costo de herrajes araña con factura
            mp[76][14] = round((mp[76][5] * mp[76][11]), 2) #costo de herrajes araña con descuento

            mp[77][11] = round((cantidad * (nvertical - 1) * (mhorizontal - 1)), 2) # cantidad de soportes de herrajes araña
            mp[77][13] = round((mp[77][4] * mp[77][11]), 2) #costo de soportes de herrajes araña con factura
            mp[77][14] = round((mp[77][5] * mp[77][11]), 2) #costo de soportes de herrajes araña con descuento

            mp[157][11] = cantidad * (nvertical - 1) * 2 # cantidad de anclajes de hierro
            mp[157][13] = round((mp[157][4] * mp[157][11]), 2) #costo de anclajes de hierro con factura
            mp[157][14] = round((mp[157][5] * mp[157][11]), 2) #costo de anclajes de hierro con descuento

            mp[158][11] = cantidad * (nvertical - 1) * 2 * 2# cantidad de pernos de expanción
            mp[158][13] = round((mp[158][4] * mp[158][11]), 2) #costo de pernos de expanción con factura
            mp[158][14] = round((mp[158][5] * mp[158][11]), 2) #costo de pernos de expanción con descuento

            accesorios = round((mp[158][13] + mp[157][13] + mp[77][13] + mp[76][13] + mp[16][13] + mp[13][13] + mp[14][13] + mp[5][13] + mp[3][13] + mp[1][13]), 2)
            
            messagebox.showinfo("cot", str(cantidad)+"  Frente(s) de Vidrio Templado tipo Spyder \n de  "+str(base)+"  Mt. de base   x  "+str(altura)+"  Mt. de altura ==> "+str(base * altura * cantidad)+ " Mt2. \n TOTAL COSTO PARCIAL  "+str(vidrio + mp[75][13] + accesorios)+" $us \n Costo de vidrio templado =  "+str(vidrio)+"  $us \n Costo de la mano de obra  =  "+str(mp[75][13])+" $us. \n Costo de accesorios  = "+str(accesorios)+"  $us. ")  

            if espesor == "8 mm":
                if color == "Incoloro":
                    mp[207][4] = cantidad 
                    mp[207][5] = mp[75][11]
                    mp[207][6] = mp[75][13]
                    mp[207][7] = accesorios
                    mp[207][8] = vidrio
                    mp[207][9] = vidrio + accesorios + mp[75][13]

                elif color == "Color":
                    mp[208][4] = cantidad 
                    mp[208][5] = mp[75][11]
                    mp[208][6] = mp[75][13]
                    mp[208][7] = accesorios
                    mp[208][8] = vidrio
                    mp[208][9] = vidrio + accesorios + mp[75][13]

            elif espesor == "10 mm":
                if color == "Incoloro":
                    mp[209][4] = cantidad 
                    mp[209][5] = mp[75][11]
                    mp[209][6] = mp[75][13]
                    mp[209][7] = accesorios
                    mp[209][8] = vidrio
                    mp[209][9] = vidrio + accesorios + mp[75][13]

                elif color == "Color":
                    mp[210][4] = cantidad 
                    mp[210][5] = mp[75][11]
                    mp[210][6] = mp[75][13]
                    mp[210][7] = accesorios
                    mp[210][8] = vidrio
                    mp[210][9] = vidrio + accesorios + mp[75][13]   
            
            for i in range(1, 237, 1):
                for j in range(11, 19, 1):
                    acum[i][j] += mp[i][j]
            
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    acum[i][j] += mp[i][j]
        
            self.ventana.destroy()
            application=opcion()
        else:
            messagebox.showinfo("NO", "ERROR algun dato ingresado no es correcto o no ingresaste algún dato")

class op2:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("380x740")
        self.ventana.title("Op1")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="FRENTE TEMPLADO \n CON VIENTOS Y HERRAJES", font=("Comic Sans", 14,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=15)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/op2a.png")
        self.img = self.img.resize((260,260))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand="True", fill="both", side="top", pady=0)

        self.label_base = Label(self.frame2, text="BASE en metros : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_base.grid(row=0, column=0, padx=5, pady=3, sticky="e")
        self.entry_base = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_base.grid(row=0, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.label_altura = Label(self.frame2, text="ALTURA en metros :",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_altura.grid(row=1, column=0, padx=5, pady=3, sticky="e")
        self.entry_altura = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_altura.grid(row=1, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_cantidad = Label(self.frame2, text="CANTIDAD : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_cantidad.grid(row=2, column=0, padx=5, pady=3, sticky="e")
        self.entry_cantidad = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_cantidad.grid(row=2, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_espesor = Label(self.frame2, text="ESPESOR en mm. = 8   ó   10  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_espesor.grid(row=3, column=0, padx=5, pady=3, sticky="e")
        self.espesor_v = StringVar()
        self.lista1 = ["8 mm", "10 mm"]
        self.opciones1 = OptionMenu(self.frame2, self.espesor_v, *self.lista1)
        self.opciones1.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.espesor_v.set("???????")
        self.opciones1.grid(row=3, column=1, padx=5, pady=3, sticky="e")

        self.label_color = Label(self.frame2, text="VIDRIO INCOLORO ó COLOR  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_color.grid(row=4, column=0, padx=5, pady=3, sticky="e")
        self.color_v = StringVar()
        self.lista2 = ["Incoloro", "Color"]
        self.opciones2 = OptionMenu(self.frame2, self.color_v, *self.lista2)
        self.opciones2.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.color_v.set("???????")
        self.opciones2.grid(row=4, column=1, padx=5, pady=3, sticky="e")

        self.label_nvertical = Label(self.frame2, text="N DIV. VERTICALES : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_nvertical.grid(row=5, column=0, padx=5, pady=3, sticky="e")
        self.entry_nvertical = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_nvertical.grid(row=5, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_mhorizontal = Label(self.frame2, text="M DIV. HORIZONTALES : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_mhorizontal.grid(row=6, column=0, padx=5, pady=3, sticky="e")
        self.entry_mhorizontal = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_mhorizontal.grid(row=6, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.boton_cotizar = Button(self.frame2, text="COTIZAR Y SEGUIR", width=18, font=("Comic Sans", 11,"bold"), command=self.cotizar)
        self.boton_cotizar.grid(row=8, column=0, pady=15, columnspan=1, padx=25, sticky="w")

        self.boton_salir = Button(self.frame2, text="SALIR", width=18, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=8, column=1, pady=15, columnspan=1, padx=10, sticky="ew")

        mainloop()
    
    def salir(self):
        self.ventana.destroy()
        application=login()

    def cotizar(self):
        if len(self.entry_base.get()) != 0 and len(self.entry_altura.get()) != 0 and len(self.entry_cantidad.get()) != 0 and len(self.entry_nvertical.get()) != 0 and len(self.entry_mhorizontal.get()) != 0 and len(self.espesor_v.get()) != 0 and len(self.color_v.get()) != 0:
            while True:
                try:
                    x = float(self.entry_base.get())
                    y = float(self.entry_altura.get())
                    break

                except ValueError:
                
                    messagebox.showinfo("NO", "ERROR ....... La medida de la BASE ó ALTURA no son correctas, revise los doatos ingresados e introduzca nuevamente los valores .... RECUERDE LA SEPARACION DECIMAL ES CON PUNTO . ")
                    return(False)
                
            while True:
                try:
                    x = int(self.entry_cantidad.get())
                    y = int(self.entry_nvertical.get())
                    z = int(self.entry_mhorizontal.get())  
                    break

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... La CANTIDAD O LAS DIVISIONES, no son correctas, revise los datos ingresados e introduzca nuevamente los valores correctos.... RECUERDE QUE DEBEN SER NUMEROS SIN DECIMALES")
                    return(False)
                
            while True:
                try:
                    x = str(self.espesor_v.get())
                    y = str(self.color_v.get())
                    if x == "8 mm" or x == "10 mm":
                        if y == "Incoloro" or y == "Color":
                            break
                        else:
                            return(False)
                    else:
                        return(False)

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... El ESPESOR Y EL COLOR DEBEN SER SELECCIONADOS, revise si fueron seleccionados y seleccione la opcion deseada...")
                    return(False)
                
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            cantidad = int(self.entry_cantidad.get())
            espesor = self.espesor_v.get()
            color = self.color_v.get()
            nvertical = int(self.entry_nvertical.get())
            mhorizontal = int(self.entry_mhorizontal.get())

            mp = inicia

            for i in range(0, 237, 1):
                for j in range(11, 19, 1):
                    mp[i][j] = 0.00
            
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    mp[i][j] = 0.00

            mp[196][3] = acum[196][3]
            mp[197][3] = acum[197][3]
            mp[198][3] = acum[198][3]
            mp[199][3] = acum[199][3]
            mp[200][3] = acum[200][3]
            mp[201][3] = acum[201][3]
            mp[202][3] = acum[202][3]

            if espesor == "8 mm":
                if color == "Incoloro":
                    mp[18][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[18][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[18][13] = round(((mp[18][12] + (cantidad * 0.20 * altura * (nvertical-1))) * mp[18][4]), 2) #costo del vidrio templado con factura
                    mp[18][14] = round(((mp[18][12] + (cantidad * 0.20 * altura * (nvertical-1))) * mp[18][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[18][13], 2)

                elif color == "Color":
                    mp[23][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[23][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[23][13] = round(((mp[23][12] + (cantidad * 0.20 * altura * (nvertical-1))) * mp[23][4]), 2) #costo del vidrio templado con factura
                    mp[23][14] = round(((mp[23][12] + (cantidad * 0.20 * altura * (nvertical-1))) * mp[23][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[23][13], 2)

            elif espesor == "10 mm":
                if color == "Incoloro":
                    mp[17][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[17][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[17][13] = round(((mp[17][12] + (cantidad * 0.20 * altura * (nvertical-1))) * mp[17][4]), 2) #costo del vidrio templado con factura
                    mp[17][14] = round(((mp[17][12] + (cantidad * 0.20 * altura * (nvertical-1))) * mp[17][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[17][13], 2)

                elif color == "Color":
                    mp[22][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[22][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[22][13] = round(((mp[22][12] + (cantidad * 0.20 * altura * (nvertical-1))) * mp[22][4]), 2) #costo del vidrio templado con factura
                    mp[22][14] = round(((mp[22][12] + (cantidad * 0.20 * altura * (nvertical-1))) * mp[22][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[22][13], 2)                

            mp[75][11] = round((cantidad * base * altura), 2)
            mp[75][12] = mp[75][11]
            mp[75][13] = round(((mp[75][11] + (cantidad * 0.20 * altura * (nvertical-1))) * mp[75][4]), 2)  #costo mano de obra con factura
            mp[75][14] = round(((mp[75][11] + (cantidad * 0.20 * altura * (nvertical-1))) * mp[75][5]), 2)  #costo mano de obra con descuento
            
            mp[1][11] = round((( cantidad * ((4 * base) + (4 * altura) + ((nvertical-1) * altura) + ((mhorizontal-1) * base))) / 6), 2) # cantidad de silicona normal
            mp[1][13] = round((mp[1][4] * mp[1][11]), 2) #costo silicona natural con factura
            mp[1][14] = round((mp[1][5] * mp[1][11]), 2) #costo silicona natural con descuento
            
            mp[3][11] = round(((cantidad * ((4 * base) + (4 * altura) + ((nvertical-1) * altura) + ((mhorizontal-1) * base))) * 2 / 20), 2) # cantidad de cinta masking
            mp[3][13] = round((mp[3][4] * mp[3][11]), 2) #costo cinta masking con factura
            mp[3][14] = round((mp[3][5] * mp[3][11]), 2) #costo cinta masking con descuento  
            
            mp[5][11] = round((cantidad * ((2 * base) + (2 * altura)) / 6), 2) # cantidad de perfil U 15 x 25 incoloro o bronce
            mp[5][13] = round((mp[5][4] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con factura
            mp[5][14] = round((mp[5][5] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con descuento

            mp[14][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tornillo de 8 x 1 1/2
            mp[14][13] = round((mp[14][4] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con factura
            mp[14][14] = round((mp[14][5] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con descuento

            mp[13][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tarugos No. 6
            mp[13][13] = round((mp[13][4] * mp[13][11]), 2) #costo de tarugos No. 6 con factura
            mp[13][14] = round((mp[13][5] * mp[13][11]), 2) #costo de tarugos No. 6 con descuento

            mp[78][11] = round((cantidad * (nvertical - 1) * (mhorizontal - 1)), 2) # Herraje 1318.
            mp[78][13] = round((mp[78][4] * mp[78][11]), 2) # Herraje 1318. con factura
            mp[78][14] = round((mp[78][5] * mp[78][11]), 2) # Herraje 1318. con descuento

            mp[55][11] = round((cantidad * (nvertical - 1) * 2), 2) # Herraje 1302.
            mp[55][13] = round((mp[55][4] * mp[55][11]), 2) # Herraje 1302. con factura
            mp[55][14] = round((mp[55][5] * mp[55][11]), 2) # Herraje 1302. con descuento
            
            mp[56][11] = round((cantidad * (nvertical - 1) * (mhorizontal - 1)), 2) # Herraje 1306.
            mp[56][13] = round((mp[56][4] * mp[56][11]), 2) # Herraje 1306. con factura
            mp[56][14] = round((mp[56][5] * mp[56][11]), 2) # Herraje 1306. con descuento


            accesorios = round((mp[56][13] + mp[55][13] + mp[78][13] + mp[13][13] + mp[14][13] + mp[5][13] + mp[3][13] + mp[1][13]), 2)
            
            messagebox.showinfo("cot", str(cantidad)+"  Frente(s) de Vidrio Templado con vientos y herrajes \n de  "+str(base)+"  Mt. de base   x  "+str(altura)+"  Mt. de altura ==> "+str(base * altura * cantidad)+ " Mt2. \n TOTAL COSTO PARCIAL  "+str(vidrio + mp[75][13] + accesorios)+" $us \n Costo de vidrio templado =  "+str(vidrio)+"  $us \n Costo de la mano de obra  =  "+str(mp[75][13])+" $us. \n Costo de accesorios  = "+str(accesorios)+"  $us. ")  

            if espesor == "8 mm":
                if color == "Incoloro":
                    mp[211][4] = cantidad 
                    mp[211][5] = mp[75][11]
                    mp[211][6] = mp[75][13]
                    mp[211][7] = accesorios
                    mp[211][8] = vidrio
                    mp[211][9] = vidrio + accesorios + mp[75][13]

                elif color == "Color":
                    mp[212][4] = cantidad 
                    mp[212][5] = mp[75][11]
                    mp[212][6] = mp[75][13]
                    mp[212][7] = accesorios
                    mp[212][8] = vidrio
                    mp[212][9] = vidrio + accesorios + mp[75][13]

            elif espesor == "10 mm":
                if color == "Incoloro":
                    mp[213][4] = cantidad 
                    mp[213][5] = mp[75][11]
                    mp[213][6] = mp[75][13]
                    mp[213][7] = accesorios
                    mp[213][8] = vidrio
                    mp[213][9] = vidrio + accesorios + mp[75][13]

                elif color == "Color":
                    mp[214][4] = cantidad 
                    mp[214][5] = mp[75][11]
                    mp[214][6] = mp[75][13]
                    mp[214][7] = accesorios
                    mp[214][8] = vidrio 
                    mp[214][9] = vidrio + accesorios + mp[75][13]  
            
            for i in range(1, 237, 1):
                for j in range(11, 19, 1):
                    acum[i][j] += mp[i][j]
            
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    acum[i][j] += mp[i][j]

            self.ventana.destroy()
            application=opcion()
        else:
            messagebox.showinfo("NO", "ERROR algun dato ingresado no es correcto o no ingresaste algún dato")

class op3:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("380x740")
        self.ventana.title("Op1")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="PAÑOS FIJOS \n DE VIDRIO TEMPLADO", font=("Comic Sans", 14,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=15)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/op3a.png")
        self.img = self.img.resize((260,260))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand="True", fill="both", side="top", pady=0)

        self.label_base = Label(self.frame2, text="BASE en metros : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_base.grid(row=0, column=0, padx=5, pady=3, sticky="e")
        self.entry_base = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_base.grid(row=0, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.label_altura = Label(self.frame2, text="ALTURA en metros :",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_altura.grid(row=1, column=0, padx=5, pady=3, sticky="e")
        self.entry_altura = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_altura.grid(row=1, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_cantidad = Label(self.frame2, text="CANTIDAD : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_cantidad.grid(row=2, column=0, padx=5, pady=3, sticky="e")
        self.entry_cantidad = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_cantidad.grid(row=2, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_espesor = Label(self.frame2, text="ESPESOR en mm. = 8   ó   10  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_espesor.grid(row=3, column=0, padx=5, pady=3, sticky="e")
        self.espesor_v = StringVar()
        self.lista1 = ["8 mm", "10 mm"]
        self.opciones1 = OptionMenu(self.frame2, self.espesor_v, *self.lista1)
        self.opciones1.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.espesor_v.set("???????")
        self.opciones1.grid(row=3, column=1, padx=5, pady=3, sticky="e")

        self.label_color = Label(self.frame2, text="VIDRIO INCOLORO ó COLOR  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_color.grid(row=4, column=0, padx=5, pady=3, sticky="e")
        self.color_v = StringVar()
        self.lista2 = ["Incoloro", "Color"]
        self.opciones2 = OptionMenu(self.frame2, self.color_v, *self.lista2)
        self.opciones2.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.color_v.set("???????")
        self.opciones2.grid(row=4, column=1, padx=5, pady=3, sticky="e")

        self.label_nvertical = Label(self.frame2, text="N DIV. VERTICALES : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_nvertical.grid(row=5, column=0, padx=5, pady=3, sticky="e")
        self.entry_nvertical = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_nvertical.grid(row=5, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.boton_cotizar = Button(self.frame2, text="COTIZAR Y SEGUIR", width=18, font=("Comic Sans", 11,"bold"), command=self.cotizar)
        self.boton_cotizar.grid(row=8, column=0, pady=15, columnspan=1, padx=25, sticky="w")

        self.boton_salir = Button(self.frame2, text="SALIR", width=18, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=8, column=1, pady=15, columnspan=1, padx=10, sticky="ew")

        mainloop()
    
    def salir(self):
        self.ventana.destroy()
        application=login()

    def cotizar(self):
        if len(self.entry_base.get()) != 0 and len(self.entry_altura.get()) != 0 and len(self.entry_cantidad.get()) != 0 and len(self.entry_nvertical.get()) != 0 and len(self.espesor_v.get()) != 0 and len(self.color_v.get()) != 0: 

            while True:
                try:
                    x = float(self.entry_base.get())
                    y = float(self.entry_altura.get())
                    break

                except ValueError:
                
                    messagebox.showinfo("NO", "ERROR ....... La medida de la BASE ó ALTURA no son correctas, revise los doatos ingresados e introduzca nuevamente los valores .... RECUERDE LA SEPARACION DECIMAL ES CON PUNTO . ")
                    return(False)
                
            while True:
                try:
                    x = int(self.entry_cantidad.get())
                    y = int(self.entry_nvertical.get())
                    break

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... La CANTIDAD O LAS DIVISIONES, no son correctas, revise los datos ingresados e introduzca nuevamente los valores correctos.... RECUERDE QUE DEBEN SER NUMEROS SIN DECIMALES")
                    return(False)
                
            while True:
                try:
                    x = str(self.espesor_v.get())
                    y = str(self.color_v.get())
                    if x == "8 mm" or x == "10 mm":
                        if y == "Incoloro" or y == "Color":
                            break
                        else:
                            return(False)
                    else:
                        return(False)

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... El ESPESOR Y EL COLOR DEBEN SER SELECCIONADOS, revise si fueron seleccionados y seleccione la opcion deseada...")
                    return(False)
                
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            cantidad = int(self.entry_cantidad.get())
            espesor = self.espesor_v.get()
            color = self.color_v.get()
            nvertical = int(self.entry_nvertical.get())

            mp = inicia

            for i in range(0, 237, 1):
                for j in range(11, 19, 1):
                    mp[i][j] = 0.00

            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    mp[i][j] = 0.00

            mp[196][3] = acum[196][3]
            mp[197][3] = acum[197][3]
            mp[198][3] = acum[198][3]
            mp[199][3] = acum[199][3]
            mp[200][3] = acum[200][3]
            mp[201][3] = acum[201][3]
            mp[202][3] = acum[202][3]

            if espesor == "8 mm":
                if color == "Incoloro":
                    mp[18][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[18][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[18][13] = round((mp[18][12] * mp[18][4]), 2) #costo del vidrio templado con factura
                    mp[18][14] = round((mp[18][12] * mp[18][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[18][13], 2)

                elif color == "Color":

                    mp[23][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[23][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[23][13] = round((mp[23][12] * mp[23][4]), 2) #costo del vidrio templado con factura
                    mp[23][14] = round((mp[23][12] * mp[23][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[23][13], 2)

            elif espesor == "10 mm":
                if color == "Incoloro":
                    mp[17][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[17][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[17][13] = round((mp[17][12] * mp[17][4]), 2) #costo del vidrio templado con factura
                    mp[17][14] = round((mp[17][12] * mp[17][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[17][13], 2)

                elif color == "Color":
                    mp[22][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[22][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[22][13] = round((mp[22][12] * mp[22][4]), 2) #costo del vidrio templado con factura
                    mp[22][14] = round((mp[22][12] * mp[22][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[22][13], 2)                

            mp[75][11] = round((cantidad * base * altura), 2)
            mp[75][12] = mp[75][11]
            mp[75][13] = round((mp[75][11] * mp[75][4]), 2)  #costo mano de obra con factura
            mp[75][14] = round((mp[75][11] * mp[75][5]), 2)  #costo mano de obra con descuento
            
            mp[1][11] = round((( cantidad * ((4 * base) + (4 * altura) + ((nvertical-1) * altura))) / 6), 2) # cantidad de silicona normal
            mp[1][13] = round((mp[1][4] * mp[1][11]), 2) #costo silicona natural con factura
            mp[1][14] = round((mp[1][5] * mp[1][11]), 2) #costo silicona natural con descuento
            
            mp[3][11] = round(((cantidad * ((4 * base) + (4 * altura) + ((nvertical-1) * altura))) * 2 / 20), 2) # cantidad de cinta masking
            mp[3][13] = round((mp[3][4] * mp[3][11]), 2) #costo cinta masking con factura
            mp[3][14] = round((mp[3][5] * mp[3][11]), 2) #costo cinta masking con descuento  
            
            mp[5][11] = round((cantidad * ((2 * base) + (2 * altura)) / 6), 2) # cantidad de perfil U 15 x 25 incoloro o bronce
            mp[5][13] = round((mp[5][4] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con factura
            mp[5][14] = round((mp[5][5] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con descuento

            mp[14][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tornillo de 8 x 1 1/2
            mp[14][13] = round((mp[14][4] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con factura
            mp[14][14] = round((mp[14][5] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con descuento

            mp[13][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tarugos No. 6
            mp[13][13] = round((mp[13][4] * mp[13][11]), 2) #costo de tarugos No. 6 con factura
            mp[13][14] = round((mp[13][5] * mp[13][11]), 2) #costo de tarugos No. 6 con descuento

            accesorios = round((mp[13][13] + mp[14][13] + mp[5][13] + mp[3][13] + mp[1][13]), 2)
            
            messagebox.showinfo("cot", str(cantidad)+"  Paño(s) Fijo(s) de Vidrio Templado \n de  "+str(base)+"  Mt. de base   x  "+str(altura)+"  Mt. de altura ==> "+str(base * altura * cantidad)+ " Mt2. \n TOTAL COSTO PARCIAL  "+str(vidrio + mp[75][13] + accesorios)+" $us \n Costo de vidrio templado =  "+str(vidrio)+"  $us \n Costo de la mano de obra  =  "+str(mp[75][13])+" $us. \n Costo de accesorios  = "+str(accesorios)+"  $us. ")  

            if espesor == "8 mm":
                if color == "Incoloro":
                    mp[203][4] = cantidad 
                    mp[203][5] = mp[75][11]
                    mp[203][6] = mp[75][13]
                    mp[203][7] = accesorios
                    mp[203][8] = vidrio
                    mp[203][9] = vidrio + accesorios + mp[75][13]

                elif color == "Color":
                    mp[204][4] = cantidad 
                    mp[204][5] = mp[75][11]
                    mp[204][6] = mp[75][13]
                    mp[204][7] = accesorios
                    mp[204][8] = vidrio
                    mp[204][9] = vidrio + accesorios + mp[75][13]

            elif espesor == "10 mm":
                if color == "Incoloro":
                    mp[205][4] = cantidad 
                    mp[205][5] = mp[75][11]
                    mp[205][6] = mp[75][13]
                    mp[205][7] = accesorios
                    mp[205][8] = vidrio
                    mp[205][9] = vidrio + accesorios + mp[75][13]

                elif color == "Color":
                    mp[206][4] = cantidad 
                    mp[206][5] = mp[75][11]
                    mp[206][6] = mp[75][13]
                    mp[206][7] = accesorios
                    mp[206][8] = vidrio
                    mp[206][9] = vidrio + accesorios + mp[75][13] 
            
            for i in range(1, 237, 1):
                for j in range(11, 19, 1):
                    acum[i][j] += mp[i][j]
            
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    acum[i][j] += mp[i][j]

            self.ventana.destroy()
            application=opcion()
        else:
            messagebox.showinfo("NO", "ERROR algun dato ingresado no es correcto o no ingresaste algún dato")

class op4:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("380x740")
        self.ventana.title("Op1")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="PUERTA VENTANA CORREDIZA \n 2 HOJAS", font=("Comic Sans", 14,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=15)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/op4a.png")
        self.img = self.img.resize((260,260))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand="True", fill="both", side="top", pady=0)

        self.label_base = Label(self.frame2, text="BASE en metros : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_base.grid(row=0, column=0, padx=5, pady=3, sticky="e")
        self.entry_base = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_base.grid(row=0, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.label_altura = Label(self.frame2, text="ALTURA en metros :",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_altura.grid(row=1, column=0, padx=5, pady=3, sticky="e")
        self.entry_altura = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_altura.grid(row=1, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_cantidad = Label(self.frame2, text="CANTIDAD : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_cantidad.grid(row=2, column=0, padx=5, pady=3, sticky="e")
        self.entry_cantidad = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_cantidad.grid(row=2, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_espesor = Label(self.frame2, text="ESPESOR en mm. = 8   ó   10  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_espesor.grid(row=3, column=0, padx=5, pady=3, sticky="e")
        self.espesor_v = StringVar()
        self.lista1 = ["8 mm", "10 mm"]
        self.opciones1 = OptionMenu(self.frame2, self.espesor_v, *self.lista1)
        self.opciones1.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.espesor_v.set("???????")
        self.opciones1.grid(row=3, column=1, padx=5, pady=3, sticky="e")

        self.label_color = Label(self.frame2, text="VIDRIO INCOLORO ó COLOR  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_color.grid(row=4, column=0, padx=5, pady=3, sticky="e")
        self.color_v = StringVar()
        self.lista2 = ["Incoloro", "Color"]
        self.opciones2 = OptionMenu(self.frame2, self.color_v, *self.lista2)
        self.opciones2.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.color_v.set("???????")
        self.opciones2.grid(row=4, column=1, padx=5, pady=3, sticky="e")

        self.label_puertaventana = Label(self.frame2, text="PUERTA ó VENTANA ?  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_puertaventana.grid(row=7, column=0, padx=5, pady=3, sticky="e")
        self.puertaventana = StringVar()
        self.lista3 = ["Puerta", "Ventana"]
        self.opciones3 = OptionMenu(self.frame2, self.puertaventana, *self.lista3)
        self.opciones3.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.puertaventana.set(" ?????????? ")
        self.opciones3.grid(row=7, column=1, padx=5, pady=3, sticky="e")
        
        self.boton_cotizar = Button(self.frame2, text="COTIZAR Y SEGUIR", width=18, font=("Comic Sans", 11,"bold"), command=self.cotizar)
        self.boton_cotizar.grid(row=8, column=0, pady=15, columnspan=1, padx=25, sticky="w")

        self.boton_salir = Button(self.frame2, text="SALIR", width=18, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=8, column=1, pady=15, columnspan=1, padx=10, sticky="ew")

        mainloop()
    
    def salir(self):
        self.ventana.destroy()
        application=login()

    def cotizar(self):
        if len(self.entry_base.get()) != 0 and len(self.entry_altura.get()) != 0 and len(self.entry_cantidad.get()) != 0 and len(self.espesor_v.get()) != 0 and len(self.color_v.get()) != 0 and len(self.puertaventana.get()) != 0: # and len(self.freno.get()) != 0

            while True:
                try:
                    x = float(self.entry_base.get())
                    y = float(self.entry_altura.get())
                    break

                except ValueError:
                
                    messagebox.showinfo("NO", "ERROR ....... La medida de la BASE ó ALTURA no son correctas, revise los doatos ingresados e introduzca nuevamente los valores .... RECUERDE LA SEPARACION DECIMAL ES CON PUNTO . ")
                    return(False)
                
            while True:
                try:
                    x = int(self.entry_cantidad.get())
                    break

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... La CANTIDAD O LAS DIVISIONES, no son correctas, revise los datos ingresados e introduzca nuevamente los valores correctos.... RECUERDE QUE DEBEN SER NUMEROS SIN DECIMALES")
                    return(False)
                
            while True:
                try:
                    x = str(self.espesor_v.get())
                    y = str(self.color_v.get())
                    z = str(self.puertaventana.get())
                    if x == "8 mm" or x == "10 mm":
                        if y == "Incoloro" or y == "Color":
                            break
                        else:
                            return(False)
                    else:
                        return(False)

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... El ESPESOR Y EL COLOR DEBEN SER SELECCIONADOS, revise si fueron seleccionados y seleccione la opcion deseada...")
                    return(False)
                
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            cantidad = int(self.entry_cantidad.get())
            espesor = self.espesor_v.get()
            color = self.color_v.get()
            puertaventana = self.puertaventana.get()

            mp = inicia

            for i in range(0, 237, 1):
                for j in range(11, 19, 1):
                    mp[i][j] = 0.00
            
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    mp[i][j] = 0.00

            mp[196][3] = acum[196][3]
            mp[197][3] = acum[197][3]
            mp[198][3] = acum[198][3]
            mp[199][3] = acum[199][3]
            mp[200][3] = acum[200][3]
            mp[201][3] = acum[201][3]
            mp[202][3] = acum[202][3]

            if espesor == "8 mm":
                if color == "Incoloro":
                    mp[18][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[18][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[18][13] = round(((mp[18][12] + (0.05 * altura * cantidad)) * mp[18][4]), 2) #costo del vidrio templado con factura
                    mp[18][14] = round(((mp[18][12] + (0.05 * altura * cantidad)) * mp[18][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[18][13], 2)

                elif color == "Color":

                    mp[23][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[23][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[23][13] = round(((mp[23][12] + (0.05 * altura * cantidad)) * mp[23][4]), 2) #costo del vidrio templado con factura
                    mp[23][14] = round(((mp[23][12] + (0.05 * altura * cantidad)) * mp[23][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[23][13], 2)

            elif espesor == "10 mm":
                if color == "Incoloro":
                    mp[17][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[17][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[17][13] = round(((mp[17][12] + (0.05 * altura * cantidad)) * mp[17][4]), 2) #costo del vidrio templado con factura
                    mp[17][14] = round(((mp[17][12] + (0.05 * altura * cantidad)) * mp[17][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[17][13], 2)

                elif color == "Color":
                    mp[22][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[22][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[22][13] = round(((mp[22][12] + (0.05 * altura * cantidad)) * mp[22][4]), 2) #costo del vidrio templado con factura
                    mp[22][14] = round(((mp[22][12] + (0.05 * altura * cantidad)) * mp[22][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[22][13], 2)                

            mp[75][11] = round((cantidad * base * altura), 2)
            mp[75][12] = mp[75][11]
            mp[75][13] = round((mp[75][11] * mp[75][4]), 2)  #costo mano de obra con factura
            mp[75][14] = round((mp[75][11] * mp[75][5]), 2)  #costo mano de obra con descuento
            
            mp[1][11] = round(( cantidad * ((4 * base) + (2 * altura)) / 6), 2) # cantidad de silicona normal
            mp[1][13] = round((mp[1][4] * mp[1][11]), 2) #costo silicona natural con factura
            mp[1][14] = round((mp[1][5] * mp[1][11]), 2) #costo silicona natural con descuento
            
            mp[3][11] = round(( cantidad * ((4 * base) + (2 * altura)) * 2 / 20), 2) # cantidad de cinta masking
            mp[3][13] = round((mp[3][4] * mp[3][11]), 2) #costo cinta masking con factura
            mp[3][14] = round((mp[3][5] * mp[3][11]), 2) #costo cinta masking con descuento

            mp[11][11] = round(( cantidad * ((3 * base) + altura)), 2) # cantidad de felpa
            mp[11][13] = round((mp[11][4] * mp[11][11]), 2) #costo felpa con factura
            mp[11][14] = round((mp[11][5] * mp[11][11]), 2) #costo felpa con descuento   
            
            mp[5][11] = round((cantidad * 2 * altura / 6), 2) # cantidad de perfil U 15 x 25 incoloro o bronce
            mp[5][13] = round((mp[5][4] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con factura
            mp[5][14] = round((mp[5][5] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con descuento

            mp[14][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tornillo de 8 x 1 1/2
            mp[14][13] = round((mp[14][4] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con factura
            mp[14][14] = round((mp[14][5] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con descuento

            mp[13][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tarugos No. 6
            mp[13][13] = round((mp[13][4] * mp[13][11]), 2) #costo de tarugos No. 6 con factura
            mp[13][14] = round((mp[13][5] * mp[13][11]), 2) #costo de tarugos No. 6 con descuento

            mp[31][11] = round(((cantidad  * altura) / 6), 2) # cantidad de vedapre U.
            mp[31][13] = round((mp[31][4] * mp[31][11]), 2) #costo de vedapre U. con factura
            mp[31][14] = round((mp[31][5] * mp[31][11]), 2) #costo de vedapre U. con descuento

            mp[29][11] = round((cantidad * base) / 6, 2) # cantidad de Cabezol, Tapa Guia y tapa guia para templado.
            mp[29][13] = round((mp[29][4] * mp[29][11]), 2) #costo de Cabezol, Tapa Guia y tapa guia para templado con factura
            mp[29][14] = round((mp[29][5] * mp[29][11]), 2) #costo de Cabezol, Tapa Guia y tapa guia para templado con descuento

            mp[50][11] = cantidad * 2 # cantidad de rodamientos dobles herraje 1125a
            mp[50][13] = round((mp[50][4] * mp[50][11]), 2) #costo de rodamientos dobles herraje 1125a con factura
            mp[50][14] = round((mp[50][5] * mp[50][11]), 2) #costo de rodamientos dobles herraje 1125a con descuento

            if puertaventana == "Puerta":
                mp[64][11] = round(cantidad , 2) # cantidad de chapas herraje 1510
                mp[64][13] = round((mp[64][4] * mp[64][11]), 2) #costo de chapas  herraje 1510 con factura
                mp[64][14] = round((mp[64][5] * mp[64][11]), 2) #costo de chapas  herraje 1510 con descuento

                mp[66][11] = round(cantidad , 2) # cantidad de contra chapa al muro herraje 1511a 
                mp[66][13] = round((mp[66][4] * mp[66][11]), 2) #costo de contra chapa al muro  herraje 1511a con factura
                mp[66][14] = round((mp[66][5] * mp[66][11]), 2) #costo de contra chapa al muro  herraje 1511a con descuento

            elif puertaventana == "Ventana":
                mp[42][11] = cantidad # cantidad de capuchino herraje 1038c 
                mp[42][13] = round((mp[42][4] * mp[42][11]), 2) #costo de capuchino herraje 1038c  con factura
                mp[42][14] = round((mp[42][5] * mp[42][11]), 2) #costo de capuchino herraje 1038c  con descuento

                mp[70][11] = cantidad # cantidad de jaladores simple herraje 1629j
                mp[70][13] = round((mp[70][4] * mp[70][11]), 2) #costo de jaladores simple herraje 1629j con factura
                mp[70][14] = round((mp[70][5] * mp[70][11]), 2) #costo de jaladores simple herraje 1629j con descuento

                mp[61][11] = cantidad # cantidad de picaporte herraje 1335
                mp[61][13] = round((mp[61][4] * mp[61][11]), 2) #costo de picaporte herraje 1335 con factura
                mp[61][14] = round((mp[61][5] * mp[61][11]), 2) #costo de picaporte herraje 1335 con descuento

            accesorios = round((mp[61][13] + mp[70][13] + mp[42][13] +mp[66][13] + mp[64][13] + mp[50][13] + mp[29][13] + mp[31][13] + mp[13][13] + mp[14][13] + mp[5][13] + mp[11][13] + mp[3][13] + mp[1][13]), 2)
            
            messagebox.showinfo("cot", str(cantidad)+"  Frente(s) de Vidrio Templado tipo Spyder \n de  "+str(base)+"  Mt. de base   x  "+str(altura)+"  Mt. de altura ==> "+str(base * altura * cantidad)+ " Mt2. \n TOTAL COSTO PARCIAL  "+str(vidrio + mp[75][13] + accesorios)+" $us \n Costo de vidrio templado =  "+str(vidrio)+"  $us \n Costo de la mano de obra  =  "+str(mp[75][13])+" $us. \n Costo de accesorios  = "+str(accesorios)+"  $us. ")  

            if espesor == "8 mm":
                if color == "Incoloro":
                    mp[215][4] = cantidad 
                    mp[215][5] = mp[75][11]
                    mp[215][6] = mp[75][13]
                    mp[215][7] = accesorios
                    mp[215][8] = vidrio
                    mp[215][9] = vidrio + accesorios + mp[75][13]

                elif color == "Color":
                    mp[216][4] = cantidad 
                    mp[216][5] = mp[75][11]
                    mp[216][6] = mp[75][13]
                    mp[216][7] = accesorios
                    mp[216][8] = vidrio
                    mp[216][9] = vidrio + accesorios + mp[75][13]

            elif espesor == "10 mm":
                if color == "Incoloro":
                    mp[217][4] = cantidad 
                    mp[217][5] = mp[75][11]
                    mp[217][6] = mp[75][13]
                    mp[217][7] = accesorios
                    mp[217][8] = vidrio
                    mp[217][9] = vidrio + accesorios + mp[75][13]

                elif color == "Color":
                    mp[218][4] = cantidad 
                    mp[218][5] = mp[75][11]
                    mp[218][6] = mp[75][13]
                    mp[218][7] = accesorios
                    mp[218][8] = vidrio 
                    mp[218][9] = vidrio + accesorios + mp[75][13]

            for i in range(1, 237, 1):
                for j in range(11, 19, 1):
                    acum[i][j] += mp[i][j]
            
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    acum[i][j] += mp[i][j] 
      
            self.ventana.destroy()
            application=opcion()
        else:
            messagebox.showinfo("NO", "ERROR algun dato ingresado no es correcto o no ingresaste algún dato")

class op5:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("380x740")
        self.ventana.title("Op1")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="PUERTA VENTANA CORREDIZA \n 2 HOJAS CON FIJO SUPERIOR", font=("Comic Sans", 14,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=15)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/op5a.png")
        self.img = self.img.resize((260,260))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand="True", fill="both", side="top", pady=0)

        self.label_base = Label(self.frame2, text="BASE en metros : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_base.grid(row=0, column=0, padx=5, pady=3, sticky="e")
        self.entry_base = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_base.grid(row=0, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.label_altura = Label(self.frame2, text="ALTURA en metros :",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_altura.grid(row=1, column=0, padx=5, pady=3, sticky="e")
        self.entry_altura = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_altura.grid(row=1, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_cantidad = Label(self.frame2, text="CANTIDAD : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_cantidad.grid(row=2, column=0, padx=5, pady=3, sticky="e")
        self.entry_cantidad = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_cantidad.grid(row=2, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_espesor = Label(self.frame2, text="ESPESOR en mm. = 8   ó   10  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_espesor.grid(row=3, column=0, padx=5, pady=3, sticky="e")
        self.espesor_v = StringVar()
        self.lista1 = ["8 mm", "10 mm"]
        self.opciones1 = OptionMenu(self.frame2, self.espesor_v, *self.lista1)
        self.opciones1.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.espesor_v.set("???????")
        self.opciones1.grid(row=3, column=1, padx=5, pady=3, sticky="e")

        self.label_color = Label(self.frame2, text="VIDRIO INCOLORO ó COLOR  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_color.grid(row=4, column=0, padx=5, pady=3, sticky="e")
        self.color_v = StringVar()
        self.lista2 = ["Incoloro", "Color"]
        self.opciones2 = OptionMenu(self.frame2, self.color_v, *self.lista2)
        self.opciones2.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.color_v.set("???????")
        self.opciones2.grid(row=4, column=1, padx=5, pady=3, sticky="e")

        self.label_puertaventana = Label(self.frame2, text="PUERTA ó VENTANA ?  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_puertaventana.grid(row=7, column=0, padx=5, pady=3, sticky="e")
        self.puertaventana = StringVar()
        self.lista3 = ["Puerta", "Ventana"]
        self.opciones3 = OptionMenu(self.frame2, self.puertaventana, *self.lista3)
        self.opciones3.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.puertaventana.set(" ?????????? ")
        self.opciones3.grid(row=7, column=1, padx=5, pady=3, sticky="e")
        
        self.boton_cotizar = Button(self.frame2, text="COTIZAR Y SEGUIR", width=18, font=("Comic Sans", 11,"bold"), command=self.cotizar)
        self.boton_cotizar.grid(row=8, column=0, pady=15, columnspan=1, padx=25, sticky="w")

        self.boton_salir = Button(self.frame2, text="SALIR", width=18, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=8, column=1, pady=15, columnspan=1, padx=10, sticky="ew")

        mainloop()
    
    def salir(self):
        self.ventana.destroy()
        application=login()

    def cotizar(self):
        if len(self.entry_base.get()) != 0 and len(self.entry_altura.get()) != 0 and len(self.entry_cantidad.get()) != 0 and len(self.espesor_v.get()) != 0 and len(self.color_v.get()) != 0 and len(self.puertaventana.get()) != 0: # and len(self.freno.get()) != 0

            while True:
                try:
                    x = float(self.entry_base.get())
                    y = float(self.entry_altura.get())
                    break

                except ValueError:
                
                    messagebox.showinfo("NO", "ERROR ....... La medida de la BASE ó ALTURA no son correctas, revise los doatos ingresados e introduzca nuevamente los valores .... RECUERDE LA SEPARACION DECIMAL ES CON PUNTO . ")
                    return(False)
                
            while True:
                try:
                    x = int(self.entry_cantidad.get())
                    break

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... La CANTIDAD O LAS DIVISIONES, no son correctas, revise los datos ingresados e introduzca nuevamente los valores correctos.... RECUERDE QUE DEBEN SER NUMEROS SIN DECIMALES")
                    return(False)
                
            while True:
                try:
                    x = str(self.espesor_v.get())
                    y = str(self.color_v.get())
                    if x == "8 mm" or x == "10 mm":
                        if y == "Incoloro" or y == "Color":
                            break
                        else:
                            return(False)
                    else:
                        return(False)

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... El ESPESOR Y EL COLOR DEBEN SER SELECCIONADOS, revise si fueron seleccionados y seleccione la opcion deseada...")
                    return(False)
                
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            cantidad = int(self.entry_cantidad.get())
            espesor = self.espesor_v.get()
            color = self.color_v.get()
            puertaventana = self.puertaventana.get()

            mp = inicia

            for i in range(0, 237, 1):
                for j in range(11, 19, 1):
                    mp[i][j] = 0.00

            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    mp[i][j] = 0.00

            mp[196][3] = acum[196][3]
            mp[197][3] = acum[197][3]
            mp[198][3] = acum[198][3]
            mp[199][3] = acum[199][3]
            mp[200][3] = acum[200][3]
            mp[201][3] = acum[201][3]
            mp[202][3] = acum[202][3]

            if espesor == "8 mm":
                if color == "Incoloro":
                    mp[18][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[18][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[18][13] = round(((mp[18][12] + (0.05 * altura * cantidad)) * mp[18][4]), 2) #costo del vidrio templado con factura
                    mp[18][14] = round(((mp[18][12] + (0.05 * altura * cantidad)) * mp[18][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[18][13], 2)

                elif color == "Color":

                    mp[23][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[23][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[23][13] = round(((mp[23][12] + (0.05 * altura * cantidad)) * mp[23][4]), 2) #costo del vidrio templado con factura
                    mp[23][14] = round(((mp[23][12] + (0.05 * altura * cantidad)) * mp[23][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[23][13], 2)

            elif espesor == "10 mm":
                if color == "Incoloro":
                    mp[17][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[17][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[17][13] = round(((mp[17][12] + (0.05 * altura * cantidad)) * mp[17][4]), 2) #costo del vidrio templado con factura
                    mp[17][14] = round(((mp[17][12] + (0.05 * altura * cantidad)) * mp[17][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[17][13], 2)

                elif color == "Color":
                    mp[22][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[22][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[22][13] = round(((mp[22][12] + (0.05 * altura * cantidad)) * mp[22][4]), 2) #costo del vidrio templado con factura
                    mp[22][14] = round(((mp[22][12] + (0.05 * altura * cantidad)) * mp[22][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[22][13], 2)                

            mp[75][11] = round((cantidad * base * altura), 2)
            mp[75][12] = mp[75][11]
            mp[75][13] = round((mp[75][11] * mp[75][4]), 2)  #costo mano de obra con factura
            mp[75][14] = round((mp[75][11] * mp[75][5]), 2)  #costo mano de obra con descuento
            
            mp[1][11] = round(( cantidad * ((8 * base) + (2 * altura)) / 6), 2) # cantidad de silicona normal
            mp[1][13] = round((mp[1][4] * mp[1][11]), 2) #costo silicona natural con factura
            mp[1][14] = round((mp[1][5] * mp[1][11]), 2) #costo silicona natural con descuento
            
            mp[3][11] = round(( cantidad * ((8 * base) + (2 * altura)) * 2 / 20), 2) # cantidad de cinta masking
            mp[3][13] = round((mp[3][4] * mp[3][11]), 2) #costo cinta masking con factura
            mp[3][14] = round((mp[3][5] * mp[3][11]), 2) #costo cinta masking con descuento

            mp[11][11] = round(( cantidad * ((3 * base) + altura)), 2) # cantidad de felpa
            mp[11][13] = round((mp[11][4] * mp[11][11]), 2) #costo felpa con factura
            mp[11][14] = round((mp[11][5] * mp[11][11]), 2) #costo felpa con descuento   
            
            mp[5][11] = round((cantidad * ((2 * altura) + (2 * base)) / 6), 2) # cantidad de perfil U 15 x 25 incoloro o bronce
            mp[5][13] = round((mp[5][4] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con factura
            mp[5][14] = round((mp[5][5] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con descuento

            mp[14][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tornillo de 8 x 1 1/2
            mp[14][13] = round((mp[14][4] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con factura
            mp[14][14] = round((mp[14][5] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con descuento

            mp[15][11] = round(((cantidad * base) / 0.4), 2) # cantidad de tornillo de 8 x 1/2
            mp[15][13] = round((mp[15][4] * mp[15][11]), 2) #costo de tornillo de 8 x 1/2 con factura
            mp[15][14] = round((mp[15][5] * mp[15][11]), 2) #costo de tornillo de 8 x 1/2 con descuento

            mp[13][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tarugos No. 6
            mp[13][13] = round((mp[13][4] * mp[13][11]), 2) #costo de tarugos No. 6 con factura
            mp[13][14] = round((mp[13][5] * mp[13][11]), 2) #costo de tarugos No. 6 con descuento

            mp[31][11] = round(((cantidad  * altura) / 6), 2) # cantidad de vedapre U.
            mp[31][13] = round((mp[31][4] * mp[31][11]), 2) #costo de vedapre U. con factura
            mp[31][14] = round((mp[31][5] * mp[31][11]), 2) #costo de vedapre U. con descuento

            mp[29][11] = round((cantidad * base) / 6, 2) # cantidad de Cabezal, Tapa Guia y tapa guia para templado.
            mp[29][13] = round((mp[29][4] * mp[29][11]), 2) #costo de Cabezal, Tapa Guia y tapa guia para templado con factura
            mp[29][14] = round((mp[29][5] * mp[29][11]), 2) #costo de Cabezal, Tapa Guia y tapa guia para templado con descuento

            mp[50][11] = cantidad * 2 # cantidad de rodamientos dobles herraje 1125a
            mp[50][13] = round((mp[50][4] * mp[50][11]), 2) #costo de rodamientos dobles herraje 1125a con factura
            mp[50][14] = round((mp[50][5] * mp[50][11]), 2) #costo de rodamientos dobles herraje 1125a con descuento

            if puertaventana == "Puerta":
                mp[64][11] = round(cantidad , 2) # cantidad de chapas herraje 1510
                mp[64][13] = round((mp[64][4] * mp[64][11]), 2) #costo de chapas herraje 1510 con factura
                mp[64][14] = round((mp[64][5] * mp[64][11]), 2) #costo de chapas herraje 1510 con descuento

                mp[66][11] = round(cantidad , 2) # cantidad de contra chapa herraje 1511a al muro
                mp[66][13] = round((mp[66][4] * mp[66][11]), 2) #costo de contra chapa al muro herraje 1511a con factura
                mp[66][14] = round((mp[66][5] * mp[66][11]), 2) #costo de contra chapa al muro herraje 1511a con descuento

            elif puertaventana == "Ventana":
                mp[42][11] = cantidad # cantidad de capuchino herraje 1038c
                mp[42][13] = round((mp[42][4] * mp[42][11]), 2) #costo de capuchinoo herraje 1038c con factura
                mp[42][14] = round((mp[42][5] * mp[42][11]), 2) #costo de capuchinoo herraje 1038c con descuento

                mp[70][11] = cantidad # cantidad de jaladores simple 1629j
                mp[70][13] = round((mp[70][4] * mp[70][11]), 2) #costo de jaladores simple 1629j con factura
                mp[70][14] = round((mp[70][5] * mp[70][11]), 2) #costo de jaladores simple 1629j con descuento

                mp[61][11] = cantidad # cantidad de picaporte herraje 1335
                mp[61][13] = round((mp[61][4] * mp[61][11]), 2) #costo de capuchino picaporte herraje 1335 con factura
                mp[61][14] = round((mp[61][5] * mp[61][11]), 2) #costo de capuchino picaporte herraje 1335 con descuento

            accesorios = round((mp[61][13] + mp[70][13] + mp[42][13] + mp[66][13] + mp[64][13] + mp[50][13] + mp[29][13] + mp[31][13] + mp[13][13] + mp[15][13] + mp[14][13] + mp[5][13] + mp[11][13] + mp[3][13] + mp[1][13]), 2)
            
            messagebox.showinfo("cot", str(cantidad)+"  Frente(s) de Vidrio Templado tipo Spyder \n de  "+str(base)+"  Mt. de base   x  "+str(altura)+"  Mt. de altura ==> "+str(base * altura * cantidad)+ " Mt2. \n TOTAL COSTO PARCIAL  "+str(vidrio + mp[75][13] + accesorios)+" $us \n Costo de vidrio templado =  "+str(vidrio)+"  $us \n Costo de la mano de obra  =  "+str(mp[75][13])+" $us. \n Costo de accesorios  = "+str(accesorios)+"  $us. ")  

            if espesor == "8 mm":
                if color == "Incoloro":
                    mp[219][4] = cantidad 
                    mp[219][5] = mp[75][11]
                    mp[219][6] = mp[75][13]
                    mp[219][7] = accesorios
                    mp[219][8] = vidrio
                    mp[219][9] = vidrio + accesorios + mp[75][13]

                elif color == "Color":
                    mp[220][4] = cantidad 
                    mp[220][5] = mp[75][11]
                    mp[220][6] = mp[75][13]
                    mp[220][7] = accesorios
                    mp[220][8] = vidrio
                    mp[220][9] = vidrio + accesorios + mp[75][13]

            elif espesor == "10 mm":
                if color == "Incoloro":
                    mp[221][4] = cantidad 
                    mp[221][5] = mp[75][11]
                    mp[221][6] = mp[75][13]
                    mp[221][7] = accesorios
                    mp[221][8] = vidrio
                    mp[221][9] = vidrio + accesorios + mp[75][13]

                elif color == "Color":
                    mp[222][4] = cantidad 
                    mp[222][5] = mp[75][11]
                    mp[222][6] = mp[75][13]
                    mp[222][7] = accesorios
                    mp[222][8] = vidrio
                    mp[222][9] = vidrio + accesorios + mp[75][13]  

            for i in range(1, 237, 1):
                for j in range(11, 19, 1):
                    acum[i][j] += mp[i][j]
            
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    acum[i][j] += mp[i][j] 
        
            self.ventana.destroy()
            application=opcion()
        else:
            messagebox.showinfo("NO", "ERROR algun dato ingresado no es correcto o no ingresaste algún dato")

class op6:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("380x740")
        self.ventana.title("Op1")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="PUERTA VENTANA CORREDIZA \n 4 HOJAS ", font=("Comic Sans", 14,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=15)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/op6a.png")
        self.img = self.img.resize((260,260))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand="True", fill="both", side="top", pady=0)

        self.label_base = Label(self.frame2, text="BASE en metros : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_base.grid(row=0, column=0, padx=5, pady=3, sticky="e")
        self.entry_base = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_base.grid(row=0, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.label_altura = Label(self.frame2, text="ALTURA en metros :",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_altura.grid(row=1, column=0, padx=5, pady=3, sticky="e")
        self.entry_altura = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_altura.grid(row=1, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_cantidad = Label(self.frame2, text="CANTIDAD : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_cantidad.grid(row=2, column=0, padx=5, pady=3, sticky="e")
        self.entry_cantidad = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_cantidad.grid(row=2, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_espesor = Label(self.frame2, text="ESPESOR en mm. = 8   ó   10  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_espesor.grid(row=3, column=0, padx=5, pady=3, sticky="e")
        self.espesor_v = StringVar()
        self.lista1 = ["8 mm", "10 mm"]
        self.opciones1 = OptionMenu(self.frame2, self.espesor_v, *self.lista1)
        self.opciones1.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.espesor_v.set("???????")
        self.opciones1.grid(row=3, column=1, padx=5, pady=3, sticky="e")

        self.label_color = Label(self.frame2, text="VIDRIO INCOLORO ó COLOR  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_color.grid(row=4, column=0, padx=5, pady=3, sticky="e")
        self.color_v = StringVar()
        self.lista2 = ["Incoloro", "Color"]
        self.opciones2 = OptionMenu(self.frame2, self.color_v, *self.lista2)
        self.opciones2.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.color_v.set("???????")
        self.opciones2.grid(row=4, column=1, padx=5, pady=3, sticky="e")

        self.label_puertaventana = Label(self.frame2, text="PUERTA ó VENTANA ?  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_puertaventana.grid(row=7, column=0, padx=5, pady=3, sticky="e")
        self.puertaventana = StringVar()
        self.lista3 = ["Puerta", "Ventana"]
        self.opciones3 = OptionMenu(self.frame2, self.puertaventana, *self.lista3)
        self.opciones3.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.puertaventana.set(" ?????????? ")
        self.opciones3.grid(row=7, column=1, padx=5, pady=3, sticky="e")
        
        self.boton_cotizar = Button(self.frame2, text="COTIZAR Y SEGUIR", width=18, font=("Comic Sans", 11,"bold"), command=self.cotizar)
        self.boton_cotizar.grid(row=8, column=0, pady=15, columnspan=1, padx=25, sticky="w")

        self.boton_salir = Button(self.frame2, text="SALIR", width=18, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=8, column=1, pady=15, columnspan=1, padx=10, sticky="ew")

        mainloop()
    
    def salir(self):
        self.ventana.destroy()
        application=login()

    def cotizar(self):
        if len(self.entry_base.get()) != 0 and len(self.entry_altura.get()) != 0 and len(self.entry_cantidad.get()) != 0 and len(self.espesor_v.get()) != 0 and len(self.color_v.get()) != 0 and len(self.puertaventana.get()) != 0: # and len(self.freno.get()) != 0

            while True:
                try:
                    x = float(self.entry_base.get())
                    y = float(self.entry_altura.get())
                    break

                except ValueError:
                
                    messagebox.showinfo("NO", "ERROR ....... La medida de la BASE ó ALTURA no son correctas, revise los doatos ingresados e introduzca nuevamente los valores .... RECUERDE LA SEPARACION DECIMAL ES CON PUNTO . ")
                    return(False)
                
            while True:
                try:
                    x = int(self.entry_cantidad.get())
                    break

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... La CANTIDAD O LAS DIVISIONES, no son correctas, revise los datos ingresados e introduzca nuevamente los valores correctos.... RECUERDE QUE DEBEN SER NUMEROS SIN DECIMALES")
                    return(False)
                
            while True:
                try:
                    x = str(self.espesor_v.get())
                    y = str(self.color_v.get())
                    if x == "8 mm" or x == "10 mm":
                        if y == "Incoloro" or y == "Color":
                            break
                        else:
                            return(False)
                    else:
                        return(False)

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... El ESPESOR Y EL COLOR DEBEN SER SELECCIONADOS, revise si fueron seleccionados y seleccione la opcion deseada...")
                    return(False)
                
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            cantidad = int(self.entry_cantidad.get())
            espesor = self.espesor_v.get()
            color = self.color_v.get()
            puertaventana = self.puertaventana.get()

            mp = inicia
            for i in range(0, 237, 1):
                for j in range(11, 19, 1):
                    mp[i][j] = 0.00

            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    mp[i][j] = 0.00

            mp[196][3] = acum[196][3]
            mp[197][3] = acum[197][3]
            mp[198][3] = acum[198][3]
            mp[199][3] = acum[199][3]
            mp[200][3] = acum[200][3]
            mp[201][3] = acum[201][3]
            mp[202][3] = acum[202][3]

            if espesor == "8 mm":
                if color == "Incoloro":
                    mp[18][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[18][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[18][13] = round(((mp[18][12] + (0.1 * altura * cantidad)) * mp[18][4]), 2) #costo del vidrio templado con factura
                    mp[18][14] = round(((mp[18][12] + (0.1 * altura * cantidad)) * mp[18][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[18][13], 2)

                elif color == "Color":

                    mp[23][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[23][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[23][13] = round(((mp[23][12] + (0.1 * altura * cantidad)) * mp[23][4]), 2) #costo del vidrio templado con factura
                    mp[23][14] = round(((mp[23][12] + (0.1 * altura * cantidad)) * mp[23][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[23][13], 2)

            elif espesor == "10 mm":
                if color == "Incoloro":
                    mp[17][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[17][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[17][13] = round(((mp[17][12] + (0.1 * altura * cantidad)) * mp[17][4]), 2) #costo del vidrio templado con factura
                    mp[17][14] = round(((mp[17][12] + (0.1 * altura * cantidad)) * mp[17][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[17][13], 2)

                elif color == "Color":
                    mp[22][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[22][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[22][13] = round(((mp[22][12] + (0.1 * altura * cantidad)) * mp[22][4]), 2) #costo del vidrio templado con factura
                    mp[22][14] = round(((mp[22][12] + (0.1 * altura * cantidad)) * mp[22][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[22][13], 2)                

            mp[75][11] = round((cantidad * base * altura), 2)
            mp[75][12] = mp[75][11]
            mp[75][13] = round((mp[75][11] * mp[75][4]), 2)  #costo mano de obra con factura
            mp[75][14] = round((mp[75][11] * mp[75][5]), 2)  #costo mano de obra con descuento
            
            mp[1][11] = round(( cantidad * ((4 * base) + (5 * altura)) / 6), 2) # cantidad de silicona normal
            mp[1][13] = round((mp[1][4] * mp[1][11]), 2) #costo silicona natural con factura
            mp[1][14] = round((mp[1][5] * mp[1][11]), 2) #costo silicona natural con descuento
            
            mp[3][11] = round(( cantidad * ((4 * base) + (5 * altura)) * 2 / 20), 2) # cantidad de cinta masking
            mp[3][13] = round((mp[3][4] * mp[3][11]), 2) #costo cinta masking con factura
            mp[3][14] = round((mp[3][5] * mp[3][11]), 2) #costo cinta masking con descuento

            mp[11][11] = round(( cantidad * ((3 * base) + (3 * altura))), 2) # cantidad de felpa
            mp[11][13] = round((mp[11][4] * mp[11][11]), 2) #costo felpa con factura
            mp[11][14] = round((mp[11][5] * mp[11][11]), 2) #costo felpa con descuento   
            
            mp[5][11] = round((cantidad * (2 * altura) / 6), 2) # cantidad de perfil U 15 x 25 incoloro o bronce
            mp[5][13] = round((mp[5][4] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con factura
            mp[5][14] = round((mp[5][5] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con descuento

            mp[14][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tornillo de 8 x 1 1/2
            mp[14][13] = round((mp[14][4] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con factura
            mp[14][14] = round((mp[14][5] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con descuento

            mp[13][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tarugos No. 6
            mp[13][13] = round((mp[13][4] * mp[13][11]), 2) #costo de tarugos No. 6 con factura
            mp[13][14] = round((mp[13][5] * mp[13][11]), 2) #costo de tarugos No. 6 con descuento

            mp[31][11] = round(((cantidad  * 2 * altura) / 6), 2) # cantidad de vedapre U.
            mp[31][13] = round((mp[31][4] * mp[31][11]), 2) #costo de vedapre U. con factura
            mp[31][14] = round((mp[31][5] * mp[31][11]), 2) #costo de vedapre U. con descuento

            mp[30][11] = round(((cantidad  * altura) / 6), 2) # cantidad de vedapre h.
            mp[30][13] = round((mp[30][4] * mp[30][11]), 2) #costo de vedapre h. con factura
            mp[30][14] = round((mp[30][5] * mp[30][11]), 2) #costo de vedapre h. con descuento

            mp[29][11] = round((cantidad * base) / 6, 2) # cantidad de Cabezal, Tapa Guia y tapa guia para templado.
            mp[29][13] = round((mp[29][4] * mp[29][11]), 2) #costo de Cabezal, Tapa Guia y tapa guia para templado con factura
            mp[29][14] = round((mp[29][5] * mp[29][11]), 2) #costo de Cabezal, Tapa Guia y tapa guia para templado con descuento

            mp[50][11] = cantidad * 4 # cantidad de rodamientos dobles herraje 1125a
            mp[50][13] = round((mp[50][4] * mp[50][11]), 2) #costo de rodamientos dobles herraje 1125a con factura
            mp[50][14] = round((mp[50][5] * mp[50][11]), 2) #costo de rodamientos dobles herraje 1125a con descuento

            if puertaventana == "Puerta":
                mp[64][11] = round(cantidad , 2) # cantidad de chapas herraje 1510
                mp[64][13] = round((mp[64][4] * mp[64][11]), 2) #costo de chapas herraje 1510 con factura
                mp[64][14] = round((mp[64][5] * mp[64][11]), 2) #costo de chapas herraje 1510 con descuento

                mp[65][11] = round(cantidad , 2) # cantidad de contra chapa al muro herraje 1511
                mp[65][13] = round((mp[65][4] * mp[65][11]), 2) #costo de contra chapa al muro herraje 1511 con factura
                mp[65][14] = round((mp[65][5] * mp[65][11]), 2) #costo de contra chapa al muro herraje 1511 con descuento

            elif puertaventana == "Ventana":
                mp[42][11] = cantidad * 2 # cantidad de capuchino herraje 1038c
                mp[42][13] = round((mp[42][4] * mp[42][11]), 2) #costo de capuchino herraje 1038c con factura
                mp[42][14] = round((mp[42][5] * mp[42][11]), 2) #costo de capuchino herraje 1038c con descuento

                mp[70][11] = cantidad * 2 # cantidad de jaladores simples  herraje 1629j
                mp[70][13] = round((mp[70][4] * mp[70][11]), 2) #costo de jaladores simples  herraje 1629j con factura
                mp[70][14] = round((mp[70][5] * mp[70][11]), 2) #costo de jaladores simples  herraje 1629j con descuento

                mp[61][11] = cantidad * 2 # cantidad de picaporte herraje 1335
                mp[61][13] = round((mp[61][4] * mp[61][11]), 2) #costo de picaporte herraje 1335 con factura
                mp[61][14] = round((mp[61][5] * mp[61][11]), 2) #costo de picaporte herraje 1335 con descuento

            accesorios = round((mp[61][13] + mp[70][13] + mp[42][13] + mp[65][13] + mp[64][13] + mp[50][13] + mp[29][13] + mp[31][13] + mp[13][13] + mp[30][13] + mp[14][13] + mp[5][13] + mp[11][13] + mp[3][13] + mp[1][13]), 2)
            
            messagebox.showinfo("cot", str(cantidad)+"  Frente(s) de Vidrio Templado tipo Spyder \n de  "+str(base)+"  Mt. de base   x  "+str(altura)+"  Mt. de altura ==> "+str(base * altura * cantidad)+ " Mt2. \n TOTAL COSTO PARCIAL  "+str(vidrio + mp[75][13] + accesorios)+" $us \n Costo de vidrio templado =  "+str(vidrio)+"  $us \n Costo de la mano de obra  =  "+str(mp[75][13])+" $us. \n Costo de accesorios  = "+str(accesorios)+"  $us. ")  

            if espesor == "8 mm":
                if color == "Incoloro":
                    mp[223][4] = cantidad 
                    mp[223][5] = mp[75][11]
                    mp[223][6] = mp[75][13]
                    mp[223][7] = accesorios
                    mp[223][8] = vidrio
                    mp[223][9] = vidrio + accesorios + mp[75][13]

                elif color == "Color":
                    mp[224][4] = cantidad 
                    mp[224][5] = mp[75][11]
                    mp[224][6] = mp[75][13]
                    mp[224][7] = accesorios
                    mp[224][8] = vidrio
                    mp[224][9] = vidrio + accesorios + mp[75][13]

            elif espesor == "10 mm":
                if color == "Incoloro":
                    mp[225][4] = cantidad 
                    mp[225][5] = mp[75][11]
                    mp[225][6] = mp[75][13]
                    mp[225][7] = accesorios
                    mp[225][8] = vidrio
                    mp[225][9] = vidrio + accesorios + mp[75][13]

                elif color == "Color":
                    mp[226][4] = cantidad 
                    mp[226][5] = mp[75][11]
                    mp[226][6] = mp[75][13]
                    mp[226][7] = accesorios
                    mp[226][8] = vidrio 
                    mp[226][9] = vidrio + accesorios + mp[75][13] 

            for i in range(1, 237, 1):
                for j in range(11, 19, 1):
                    acum[i][j] += mp[i][j]
            
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    acum[i][j] += mp[i][j] 
        
            self.ventana.destroy()
            application=opcion()
        else:
            messagebox.showinfo("NO", "ERROR algun dato ingresado no es correcto o no ingresaste algún dato")

class op7:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("380x740")
        self.ventana.title("Op1")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="PUERTA VENTANA CORREDIZA \n 4 HOJAS CON FIJO SUPERIOR ", font=("Comic Sans", 14,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=15)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/op7a.png")
        self.img = self.img.resize((260,260))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand="True", fill="both", side="top", pady=0)

        self.label_base = Label(self.frame2, text="BASE en metros : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_base.grid(row=0, column=0, padx=5, pady=3, sticky="e")
        self.entry_base = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_base.grid(row=0, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.label_altura = Label(self.frame2, text="ALTURA en metros :",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_altura.grid(row=1, column=0, padx=5, pady=3, sticky="e")
        self.entry_altura = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_altura.grid(row=1, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_cantidad = Label(self.frame2, text="CANTIDAD : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_cantidad.grid(row=2, column=0, padx=5, pady=3, sticky="e")
        self.entry_cantidad = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_cantidad.grid(row=2, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_espesor = Label(self.frame2, text="ESPESOR en mm. = 8   ó   10  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_espesor.grid(row=3, column=0, padx=5, pady=3, sticky="e")
        self.espesor_v = StringVar()
        self.lista1 = ["8 mm", "10 mm"]
        self.opciones1 = OptionMenu(self.frame2, self.espesor_v, *self.lista1)
        self.opciones1.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.espesor_v.set("???????")
        self.opciones1.grid(row=3, column=1, padx=5, pady=3, sticky="e")

        self.label_color = Label(self.frame2, text="VIDRIO INCOLORO ó COLOR  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_color.grid(row=4, column=0, padx=5, pady=3, sticky="e")
        self.color_v = StringVar()
        self.lista2 = ["Incoloro", "Color"]
        self.opciones2 = OptionMenu(self.frame2, self.color_v, *self.lista2)
        self.opciones2.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.color_v.set("???????")
        self.opciones2.grid(row=4, column=1, padx=5, pady=3, sticky="e")

        self.label_puertaventana = Label(self.frame2, text="PUERTA ó VENTANA ?  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_puertaventana.grid(row=7, column=0, padx=5, pady=3, sticky="e")
        self.puertaventana = StringVar()
        self.lista3 = ["Puerta", "Ventana"]
        self.opciones3 = OptionMenu(self.frame2, self.puertaventana, *self.lista3)
        self.opciones3.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.puertaventana.set(" ?????????? ")
        self.opciones3.grid(row=7, column=1, padx=5, pady=3, sticky="e")
        
        self.boton_cotizar = Button(self.frame2, text="COTIZAR Y SEGUIR", width=18, font=("Comic Sans", 11,"bold"), command=self.cotizar)
        self.boton_cotizar.grid(row=8, column=0, pady=15, columnspan=1, padx=25, sticky="w")

        self.boton_salir = Button(self.frame2, text="SALIR", width=18, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=8, column=1, pady=15, columnspan=1, padx=10, sticky="ew")

        mainloop()
    
    def salir(self):
        self.ventana.destroy()
        application=login()

    def cotizar(self):
        if len(self.entry_base.get()) != 0 and len(self.entry_altura.get()) != 0 and len(self.entry_cantidad.get()) != 0 and len(self.espesor_v.get()) != 0 and len(self.color_v.get()) != 0 and len(self.puertaventana.get()) != 0: 
            while True:
                try:
                    x = float(self.entry_base.get())
                    y = float(self.entry_altura.get())
                    break

                except ValueError:
                
                    messagebox.showinfo("NO", "ERROR ....... La medida de la BASE ó ALTURA no son correctas, revise los doatos ingresados e introduzca nuevamente los valores .... RECUERDE LA SEPARACION DECIMAL ES CON PUNTO . ")
                    return(False)
                
            while True:
                try:
                    x = int(self.entry_cantidad.get())
                    break

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... La CANTIDAD O LAS DIVISIONES, no son correctas, revise los datos ingresados e introduzca nuevamente los valores correctos.... RECUERDE QUE DEBEN SER NUMEROS SIN DECIMALES")
                    return(False)
                
            while True:
                try:
                    x = str(self.espesor_v.get())
                    y = str(self.color_v.get())
                    if x == "8 mm" or x == "10 mm":
                        if y == "Incoloro" or y == "Color":
                            break
                        else:
                            return(False)
                    else:
                        return(False)

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... El ESPESOR Y EL COLOR DEBEN SER SELECCIONADOS, revise si fueron seleccionados y seleccione la opcion deseada...")
                    return(False)
                
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            cantidad = int(self.entry_cantidad.get())
            espesor = self.espesor_v.get()
            color = self.color_v.get()
            puertaventana = self.puertaventana.get()

            mp = inicia

            for i in range(0, 237, 1):
                for j in range(11, 19, 1):
                    mp[i][j] = 0.00
                    
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    mp[i][j] = 0.00

            mp[196][3] = acum[196][3]
            mp[197][3] = acum[197][3]
            mp[198][3] = acum[198][3]
            mp[199][3] = acum[199][3]
            mp[200][3] = acum[200][3]
            mp[201][3] = acum[201][3]
            mp[202][3] = acum[202][3]

            if espesor == "8 mm":
                if color == "Incoloro":
                    mp[18][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[18][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[18][13] = round(((mp[18][12] + (0.1 * altura * cantidad)) * mp[18][4]), 2) #costo del vidrio templado con factura
                    mp[18][14] = round(((mp[18][12] + (0.1 * altura * cantidad)) * mp[18][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[18][13], 2)

                elif color == "Color":

                    mp[23][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[23][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[23][13] = round(((mp[23][12] + (0.1 * altura * cantidad)) * mp[23][4]), 2) #costo del vidrio templado con factura
                    mp[23][14] = round(((mp[23][12] + (0.1 * altura * cantidad)) * mp[23][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[23][13], 2)

            elif espesor == "10 mm":
                if color == "Incoloro":
                    mp[17][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[17][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[17][13] = round(((mp[17][12] + (0.1 * altura * cantidad)) * mp[17][4]), 2) #costo del vidrio templado con factura
                    mp[17][14] = round(((mp[17][12] + (0.1 * altura * cantidad)) * mp[17][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[17][13], 2)

                elif color == "Color":
                    mp[22][11] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[22][12] = round((cantidad * base * altura), 2) # superficie en mt2
                    mp[22][13] = round(((mp[22][12] + (0.1 * altura * cantidad)) * mp[22][4]), 2) #costo del vidrio templado con factura
                    mp[22][14] = round(((mp[22][12] + (0.1 * altura * cantidad)) * mp[22][5]), 2) #costo del vidrio templado con descuento
                    vidrio = round(mp[22][13], 2)                

            mp[75][11] = round((cantidad * base * altura), 2)
            mp[75][12] = mp[75][11]
            mp[75][13] = round((mp[75][11] * mp[75][4]), 2)  #costo mano de obra con factura
            mp[75][14] = round((mp[75][11] * mp[75][5]), 2)  #costo mano de obra con descuento
            
            mp[1][11] = round(( cantidad * ((4 * base) + (5 * altura)) / 6), 2) # cantidad de silicona normal
            mp[1][13] = round((mp[1][4] * mp[1][11]), 2) #costo silicona natural con factura
            mp[1][14] = round((mp[1][5] * mp[1][11]), 2) #costo silicona natural con descuento
            
            mp[3][11] = round(( cantidad * ((4 * base) + (5 * altura)) * 2 / 20), 2) # cantidad de cinta masking
            mp[3][13] = round((mp[3][4] * mp[3][11]), 2) #costo cinta masking con factura
            mp[3][14] = round((mp[3][5] * mp[3][11]), 2) #costo cinta masking con descuento

            mp[11][11] = round(( cantidad * ((3 * base) + (3 * altura))), 2) # cantidad de felpa
            mp[11][13] = round((mp[11][4] * mp[11][11]), 2) #costo felpa con factura
            mp[11][14] = round((mp[11][5] * mp[11][11]), 2) #costo felpa con descuento   
            
            mp[5][11] = round((cantidad * ((2 * altura) + (2 * altura)) / 6), 2) # cantidad de perfil U 15 x 25 incoloro o bronce
            mp[5][13] = round((mp[5][4] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con factura
            mp[5][14] = round((mp[5][5] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con descuento

            mp[14][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tornillo de 8 x 1 1/2
            mp[14][13] = round((mp[14][4] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con factura
            mp[14][14] = round((mp[14][5] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con descuento

            mp[15][11] = round(((cantidad * base) / 0.4), 2) # cantidad de torn5llo de 8 x 1/2
            mp[15][13] = round((mp[15][4] * mp[15][11]), 2) #costo de tornillo de 8 x 1/2 con factura
            mp[15][14] = round((mp[15][5] * mp[15][11]), 2) #costo de tornillo de 8 x 1/2 con descuento

            mp[13][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tarugos No. 6
            mp[13][13] = round((mp[13][4] * mp[13][11]), 2) #costo de tarugos No. 6 con factura
            mp[13][14] = round((mp[13][5] * mp[13][11]), 2) #costo de tarugos No. 6 con descuento

            mp[31][11] = round(((cantidad  * 2 * altura) / 6), 2) # cantidad de vedapre U.
            mp[31][13] = round((mp[31][4] * mp[31][11]), 2) #costo de vedapre U. con factura
            mp[31][14] = round((mp[31][5] * mp[31][11]), 2) #costo de vedapre U. con descuento

            mp[30][11] = round(((cantidad  * altura) / 6), 2) # cantidad de vedapre h.
            mp[30][13] = round((mp[30][4] * mp[30][11]), 2) #costo de vedapre h. con factura
            mp[30][14] = round((mp[30][5] * mp[30][11]), 2) #costo de vedapre h. con descuento

            mp[29][11] = round((cantidad * base) / 6, 2) # cantidad de Cabezal, Tapa Guia y tapa guia para templado.
            mp[29][13] = round((mp[29][4] * mp[29][11]), 2) #costo de Cabezal, Tapa Guia y tapa guia para templado con factura
            mp[29][14] = round((mp[29][5] * mp[29][11]), 2) #costo de Cabezal, Tapa Guia y tapa guia para templado con descuento

            mp[50][11] = cantidad * 4 # cantidad de rodamientos dobles herraje 1125a
            mp[50][13] = round((mp[50][4] * mp[50][11]), 2) #costo de rodamientos dobles herraje 1125a con factura
            mp[50][14] = round((mp[50][5] * mp[50][11]), 2) #costo de rodamientos dobles herraje 1125a con descuento

            if puertaventana == "Puerta":
                mp[64][11] = round(cantidad , 2) # cantidad de chapas herraje 1510
                mp[64][13] = round((mp[64][4] * mp[64][11]), 2) #costo de chapas herraje 1510 con factura
                mp[64][14] = round((mp[64][5] * mp[64][11]), 2) #costo de chapas herraje 1510 con descuento

                mp[65][11] = round(cantidad , 2) # cantidad de contra chapa al muro herraje 1511
                mp[65][13] = round((mp[65][4] * mp[65][11]), 2) #costo de contra chapa al muro herraje 1511 con factura
                mp[65][14] = round((mp[65][5] * mp[65][11]), 2) #costo de contra chapa al muro herraje 1511 con descuento

            elif puertaventana == "Ventana":
                mp[42][11] = cantidad * 2 # cantidad de capuchino herraje 1038c
                mp[42][13] = round((mp[42][4] * mp[42][11]), 2) #costo de capuchino herraje 1038c con factura
                mp[42][14] = round((mp[42][5] * mp[42][11]), 2) #costo de capuchino herraje 1038c con descuento

                mp[70][11] = cantidad * 2 # cantidad de jaladores simples herraje 1629j
                mp[70][13] = round((mp[70][4] * mp[70][11]), 2) #costo de jaladores simples herraje 1629j con factura
                mp[70][14] = round((mp[70][5] * mp[70][11]), 2) #costo de jaladores simples herraje 1629j con descuento

                mp[61][11] = cantidad * 2 # cantidad de picaporte herraje 1335
                mp[61][13] = round((mp[61][4] * mp[61][11]), 2) #costo de picaporte herraje 1335 con factura
                mp[61][14] = round((mp[61][5] * mp[61][11]), 2) #costo de picaporte herraje 1335 con descuento

            accesorios = round((mp[61][13] + mp[70][13] + mp[42][13] + mp[65][13] + mp[64][13] + mp[50][13] + mp[29][13] + mp[31][13] + mp[13][13] + mp[15][13] + mp[30][13] + mp[14][13] + mp[5][13] + mp[11][13] + mp[3][13] + mp[1][13]), 2)
            
            messagebox.showinfo("cot", str(cantidad)+"  Frente(s) de Vidrio Templado tipo Spyder \n de  "+str(base)+"  Mt. de base   x  "+str(altura)+"  Mt. de altura ==> "+str(base * altura * cantidad)+ " Mt2. \n TOTAL COSTO PARCIAL  "+str(vidrio + mp[75][13] + accesorios)+" $us \n Costo de vidrio templado =  "+str(vidrio)+"  $us \n Costo de la mano de obra  =  "+str(mp[75][13])+" $us. \n Costo de accesorios  = "+str(accesorios)+"  $us. ")  

            if espesor == "8 mm":
                if color == "Incoloro":
                    mp[227][4] = cantidad 
                    mp[227][5] = mp[75][11]
                    mp[227][6] = mp[75][13]
                    mp[227][7] = accesorios
                    mp[227][8] = vidrio
                    mp[227][9] = vidrio + accesorios + mp[75][13]

                elif color == "Color":
                    mp[228][4] = cantidad 
                    mp[228][5] = mp[75][11]
                    mp[228][6] = mp[75][13]
                    mp[228][7] = accesorios
                    mp[228][8] = vidrio
                    mp[228][9] = vidrio + accesorios + mp[75][13]

            elif espesor == "10 mm":
                if color == "Incoloro":
                    mp[229][4] = cantidad 
                    mp[229][5] = mp[75][11]
                    mp[229][6] = mp[75][13]
                    mp[229][7] = accesorios
                    mp[229][8] = vidrio
                    mp[229][9] = vidrio + accesorios + mp[75][13]

                elif color == "Color":
                    mp[230][4] = cantidad 
                    mp[230][5] = mp[75][11]
                    mp[230][6] = mp[75][13]
                    mp[230][7] = accesorios
                    mp[230][8] = vidrio 
                    mp[230][9] = vidrio + accesorios + mp[75][13] 
 
            for i in range(1, 237, 1):
                for j in range(11, 19, 1):
                    acum[i][j] += mp[i][j]
            
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    acum[i][j] += mp[i][j]  

            self.ventana.destroy()
            application=opcion()
        else:
            messagebox.showinfo("NO", "ERROR algun dato ingresado no es correcto o no ingresaste algún dato")

class op8:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("380x740")
        self.ventana.title("Op1")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="PUERTA BATIENE \n 1 HOJA", font=("Comic Sans", 14,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=15)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/op8a.png")
        self.img = self.img.resize((260,260))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand="True", fill="both", side="top", pady=0)

        self.label_base = Label(self.frame2, text="BASE en metros : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_base.grid(row=0, column=0, padx=5, pady=3, sticky="e")
        self.entry_base = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_base.grid(row=0, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.label_altura = Label(self.frame2, text="ALTURA en metros :",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_altura.grid(row=1, column=0, padx=5, pady=3, sticky="e")
        self.entry_altura = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_altura.grid(row=1, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_cantidad = Label(self.frame2, text="CANTIDAD : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_cantidad.grid(row=2, column=0, padx=5, pady=3, sticky="e")
        self.entry_cantidad = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_cantidad.grid(row=2, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_color = Label(self.frame2, text="VIDRIO INCOLORO ó COLOR  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_color.grid(row=4, column=0, padx=5, pady=3, sticky="e")
        self.color_v = StringVar()
        self.lista2 = ["Incoloro", "Color"]
        self.opciones2 = OptionMenu(self.frame2, self.color_v, *self.lista2)
        self.opciones2.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.color_v.set("???????")
        self.opciones2.grid(row=4, column=1, padx=5, pady=3, sticky="e")

        self.label_freno = Label(self.frame2, text="CON FRENO O SIN FRENO ?  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_freno.grid(row=5, column=0, padx=5, pady=3, sticky="e")
        self.freno = StringVar()
        self.lista4 = ["Con Freno", "Sin Freno"]
        self.opciones4 = OptionMenu(self.frame2, self.freno, *self.lista4)
        self.opciones4.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.freno.set("?????????")
        self.opciones4.grid(row=5, column=1, padx=5, pady=3, sticky="e")
        
        self.boton_cotizar = Button(self.frame2, text="COTIZAR Y SEGUIR", width=18, font=("Comic Sans", 11,"bold"), command=self.cotizar)
        self.boton_cotizar.grid(row=8, column=0, pady=15, columnspan=1, padx=25, sticky="w")

        self.boton_salir = Button(self.frame2, text="SALIR", width=18, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=8, column=1, pady=15, columnspan=1, padx=10, sticky="ew")

        mainloop()
    
    def salir(self):
        self.ventana.destroy()
        application=login()

    def cotizar(self):
        if len(self.entry_base.get()) != 0 and len(self.entry_altura.get()) != 0 and len(self.entry_cantidad.get()) != 0 and len(self.freno.get()) != 0 and len(self.color_v.get()) != 0: 
            while True:
                try:
                    x = float(self.entry_base.get())
                    y = float(self.entry_altura.get())
                    break

                except ValueError:
                
                    messagebox.showinfo("NO", "ERROR ....... La medida de la BASE ó ALTURA no son correctas, revise los doatos ingresados e introduzca nuevamente los valores .... RECUERDE LA SEPARACION DECIMAL ES CON PUNTO . ")
                    return(False)
                
            while True:
                try:
                    x = int(self.entry_cantidad.get())
                    break

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... La CANTIDAD O LAS DIVISIONES, no son correctas, revise los datos ingresados e introduzca nuevamente los valores correctos.... RECUERDE QUE DEBEN SER NUMEROS SIN DECIMALES")
                    return(False)
                
            while True:
                try:
                    y = str(self.color_v.get())
                    w = str(self.freno.get())
                    if y == "Incoloro" or y == "Color":
                        if w == "Con Freno" or w == "Sin Freno":
                            break
                        else:
                            return(False)
                    else:
                        return(False)

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... El ESPESOR Y EL COLOR DEBEN SER SELECCIONADOS, revise si fueron seleccionados y seleccione la opcion deseada...")
                    return(False)
                
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            cantidad = int(self.entry_cantidad.get())
            color = self.color_v.get()
            freno = self.freno.get()

            mp = inicia

            for i in range(0, 237, 1):
                for j in range(11, 19, 1):
                    mp[i][j] = 0.00
                                        
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    mp[i][j] = 0.00

            mp[196][3] = acum[196][3]
            mp[197][3] = acum[197][3]
            mp[198][3] = acum[198][3]
            mp[199][3] = acum[199][3]
            mp[200][3] = acum[200][3]
            mp[201][3] = acum[201][3]
            mp[202][3] = acum[202][3]

            if color == "Incoloro":
                mp[17][11] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[17][12] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[17][13] = round((mp[17][12] * mp[17][4]), 2) #costo del vidrio templado con factura
                mp[17][14] = round((mp[17][12] * mp[17][5]), 2) #costo del vidrio templado con descuento
                vidrio = round(mp[17][13], 2)

            elif color == "Color":
                mp[22][11] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[22][12] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[22][13] = round((mp[22][12] * mp[22][4]), 2) #costo del vidrio templado con factura
                mp[22][14] = round((mp[22][12] * mp[22][5]), 2) #costo del vidrio templado con descuento
                vidrio = round(mp[22][13], 2)                

            mp[75][11] = round((cantidad * base * altura), 2)
            mp[75][12] = mp[75][11]
            mp[75][13] = round((mp[75][11] * mp[75][4]), 2)  #costo mano de obra con factura
            mp[75][14] = round((mp[75][11] * mp[75][5]), 2)  #costo mano de obra con descuento
            
            mp[38][11] = round((cantidad * 2), 2) # cantidad de Jaladores tipo C o Manijones de vidrio
            mp[38][13] = round((mp[38][4] * mp[38][11]), 2) #costo jaladores tipo C o Manijones de vidrio con factura
            mp[38][14] = round((mp[38][5] * mp[38][11]), 2) #costo jaladores tipo C o Manijones de vidrio con descuento
            
            mp[61][11] = round(cantidad, 2) # cantidad de picaportes herraje 1335
            mp[61][13] = round((mp[61][4] * mp[61][11]), 2) #costo picaportes herraje 1335 con factura
            mp[61][14] = round((mp[61][5] * mp[61][11]), 2) #costo picaportes herraje 1335 con descuento  
            
            mp[41][11] = round((cantidad * 2), 2) # cantidad de capuchino herraje 1038 
            mp[41][13] = round((mp[41][4] * mp[41][11]), 2) #costo capuchino herraje 1038 con factura
            mp[41][14] = round((mp[41][5] * mp[41][11]), 2) #costo capuchino herraje 1038 con descuento

            mp[43][11] = round(cantidad, 1) # cantidad de zocalo superior herraje 1103
            mp[43][13] = round((mp[43][4] * mp[43][11]), 2) #costo de zocalo superior herraje 1103 con factura
            mp[43][14] = round((mp[43][5] * mp[43][11]), 2) #costo de zocalo superior herraje 1103 con descuento

            mp[44][11] = round(cantidad, 1) # cantidad de zocalo inferior herraje 1101
            mp[44][13] = round((mp[44][4] * mp[44][11]), 2) #costo de zocalo inferior herraje 1101 con factura
            mp[44][14] = round((mp[44][5] * mp[44][11]), 2) #costo de zocalo inferior herraje 1101 con descuento

            mp[67][11] = round(cantidad, 1) # cantidad de chapas herraje 1520
            mp[67][13] = round((mp[67][4] * mp[67][11]), 2) #costo de chapas herraje 1520 con factura
            mp[67][14] = round((mp[67][5] * mp[67][11]), 2) #costo de chapas herraje 1520 con descuento

            mp[63][11] = round(cantidad, 1) # cantidad de contrachapa al muro herraje 1504
            mp[63][13] = round((mp[63][4] * mp[63][11]), 2) #costo de contrachapa al muro herraje 1504 con factura
            mp[63][14] = round((mp[63][5] * mp[63][11]), 2) #costo de contrachapa al muro herraje 1504 con descuento

            mp[51][11] = round(cantidad, 1) # cantidad de casquillo para picaporte herraje 1201
            mp[51][13] = round((mp[51][4] * mp[51][11]), 2) #costo de casquillo para picaporte herraje 1201 con factura
            mp[51][14] = round((mp[51][5] * mp[51][11]), 2) #costo de casquillo para picaporte herraje 1201 con descuento

            if freno == "Con Freno":
                mp[37][11] = cantidad * 1 # cantidad de frenos
                mp[37][13] = round((mp[37][4] * mp[37][11]), 2) #costo de frenos con factura
                mp[37][14] = round((mp[37][5] * mp[37][11]), 2) #costo de frenos con descuento

            elif freno == "Sin Freno":
                mp[40][11] = cantidad * 1 # cantidad de pivote loco herraje 1013
                mp[40][13] = round((mp[40][4] * mp[40][11]), 2) #costo de pivote loco herraje 1013 con factura
                mp[40][14] = round((mp[40][5] * mp[40][11]), 2) #costo de pivote loco herraje 1013 con descuento

            accesorios = round((mp[51][13] + mp[63][13] + mp[67][13] + mp[44][13] + mp[43][13] + mp[41][13] + mp[61][13] + mp[38][13] + mp[37][13] + mp[40][13]), 2)
            
            messagebox.showinfo("cot", str(cantidad)+"  Frente(s) de Vidrio Templado tipo Spyder \n de  "+str(base)+"  Mt. de base   x  "+str(altura)+"  Mt. de altura ==> "+str(base * altura * cantidad)+ " Mt2. \n TOTAL COSTO PARCIAL  "+str(vidrio + mp[75][13] + accesorios)+" $us \n Costo de vidrio templado =  "+str(vidrio)+"  $us \n Costo de la mano de obra  =  "+str(mp[75][13])+" $us. \n Costo de accesorios  = "+str(accesorios)+"  $us. ")  

            if color == "Incoloro":
                mp[231][4] = cantidad 
                mp[231][5] = mp[75][11]
                mp[231][6] = mp[75][13]
                mp[231][7] = accesorios
                mp[231][8] = vidrio
                mp[231][9] = vidrio + accesorios + mp[75][13]

            elif color == "Color":
                mp[232][4] = cantidad 
                mp[232][5] = mp[75][11]
                mp[232][6] = mp[75][13]
                mp[232][7] = accesorios
                mp[232][8] = vidrio 
                mp[232][9] = vidrio + accesorios + mp[75][13]  
         
            for i in range(1, 237, 1):
                for j in range(11, 19, 1):
                    acum[i][j] += mp[i][j]
            
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    acum[i][j] += mp[i][j]

            self.ventana.destroy()
            application=opcion()
        else:
            messagebox.showinfo("NO", "ERROR algun dato ingresado no es correcto o no ingresaste algún dato")

class op9:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("380x740")
        self.ventana.title("Op1")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="PUERTA BATIENE \n 2 HOJAS", font=("Comic Sans", 14,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=15)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/op9a.png")
        self.img = self.img.resize((260,260))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand="True", fill="both", side="top", pady=0)

        self.label_base = Label(self.frame2, text="BASE en metros : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_base.grid(row=0, column=0, padx=5, pady=3, sticky="e")
        self.entry_base = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_base.grid(row=0, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.label_altura = Label(self.frame2, text="ALTURA en metros :",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_altura.grid(row=1, column=0, padx=5, pady=3, sticky="e")
        self.entry_altura = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_altura.grid(row=1, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_cantidad = Label(self.frame2, text="CANTIDAD : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_cantidad.grid(row=2, column=0, padx=5, pady=3, sticky="e")
        self.entry_cantidad = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_cantidad.grid(row=2, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_color = Label(self.frame2, text="VIDRIO INCOLORO ó COLOR  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_color.grid(row=4, column=0, padx=5, pady=3, sticky="e")
        self.color_v = StringVar()
        self.lista2 = ["Incoloro", "Color"]
        self.opciones2 = OptionMenu(self.frame2, self.color_v, *self.lista2)
        self.opciones2.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.color_v.set("???????")
        self.opciones2.grid(row=4, column=1, padx=5, pady=3, sticky="e")

        self.label_freno = Label(self.frame2, text="CON FRENO O SIN FRENO ?  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_freno.grid(row=5, column=0, padx=5, pady=3, sticky="e")
        self.freno = StringVar()
        self.lista4 = ["Con Freno", "Sin Freno"]
        self.opciones4 = OptionMenu(self.frame2, self.freno, *self.lista4)
        self.opciones4.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.freno.set("?????????")
        self.opciones4.grid(row=5, column=1, padx=5, pady=3, sticky="e")
        
        self.boton_cotizar = Button(self.frame2, text="COTIZAR Y SEGUIR", width=18, font=("Comic Sans", 11,"bold"), command=self.cotizar)
        self.boton_cotizar.grid(row=8, column=0, pady=15, columnspan=1, padx=25, sticky="w")

        self.boton_salir = Button(self.frame2, text="SALIR", width=18, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=8, column=1, pady=15, columnspan=1, padx=10, sticky="ew")

        mainloop()
    
    def salir(self):
        self.ventana.destroy()
        application=login()

    def cotizar(self):
        if len(self.entry_base.get()) != 0 and len(self.entry_altura.get()) != 0 and len(self.entry_cantidad.get()) != 0 and len(self.freno.get()) != 0 and len(self.color_v.get()) != 0:
            while True:
                try:
                    x = float(self.entry_base.get())
                    y = float(self.entry_altura.get())
                    break

                except ValueError:
                
                    messagebox.showinfo("NO", "ERROR ....... La medida de la BASE ó ALTURA no son correctas, revise los doatos ingresados e introduzca nuevamente los valores .... RECUERDE LA SEPARACION DECIMAL ES CON PUNTO . ")
                    return(False)
                
            while True:
                try:
                    x = int(self.entry_cantidad.get())
                    break

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... La CANTIDAD O LAS DIVISIONES, no son correctas, revise los datos ingresados e introduzca nuevamente los valores correctos.... RECUERDE QUE DEBEN SER NUMEROS SIN DECIMALES")
                    return(False)
                
            while True:
                try:
                    y = str(self.color_v.get())
                    w = str(self.freno.get())
                    if y == "Incoloro" or y == "Color":
                        if w == "Con Freno" or w == "Sin Freno":
                            break
                        else:
                            return(False)
                    else:
                        return(False)

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... El ESPESOR Y EL COLOR DEBEN SER SELECCIONADOS, revise si fueron seleccionados y seleccione la opcion deseada...")
                    return(False)
                
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            cantidad = int(self.entry_cantidad.get())
            color = self.color_v.get()
            freno = self.freno.get()

            mp = inicia

            for i in range(0, 237, 1):
                for j in range(11, 19, 1):
                    mp[i][j] = 0.00
                                        
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    mp[i][j] = 0.00

            mp[196][3] = acum[196][3]
            mp[197][3] = acum[197][3]
            mp[198][3] = acum[198][3]
            mp[199][3] = acum[199][3]
            mp[200][3] = acum[200][3]
            mp[201][3] = acum[201][3]
            mp[202][3] = acum[202][3]

            if color == "Incoloro":
                mp[17][11] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[17][12] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[17][13] = round((mp[17][12] * mp[17][4]), 2) #costo del vidrio templado con factura
                mp[17][14] = round((mp[17][12] * mp[17][5]), 2) #costo del vidrio templado con descuento
                vidrio = round(mp[17][13], 2)

            elif color == "Color":
                mp[22][11] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[22][12] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[22][13] = round((mp[22][12] * mp[22][4]), 2) #costo del vidrio templado con factura
                mp[22][14] = round((mp[22][12] * mp[22][5]), 2) #costo del vidrio templado con descuento
                vidrio = round(mp[22][13], 2)                

            mp[75][11] = round((cantidad * base * altura), 2)
            mp[75][12] = mp[75][11]
            mp[75][13] = round((mp[75][11] * mp[75][4]), 2)  #costo mano de obra con factura
            mp[75][14] = round((mp[75][11] * mp[75][5]), 2)  #costo mano de obra con descuento
            
            mp[38][11] = round((cantidad * 4), 2) # cantidad de Jaladore Tipo C o manijones de vidrio
            mp[38][13] = round((mp[38][4] * mp[38][11]), 2) #costo jaladores Tipo C o manijones de vidrio con factura
            mp[38][14] = round((mp[38][5] * mp[38][11]), 2) #costo jaladores Tipo C o manijones de vidrio con descuento
            
            mp[61][11] = round((cantidad * 3), 2) # cantidad de picaportes herraje 1335
            mp[61][13] = round((mp[61][4] * mp[61][11]), 2) #costo picaportes herraje 1335 con factura
            mp[61][14] = round((mp[61][5] * mp[61][11]), 2) #costo picaportes herraje 1335 con descuento  
            
            mp[41][11] = round((cantidad * 4), 2) # cantidad de capuchino herraje 1038
            mp[41][13] = round((mp[41][4] * mp[41][11]), 2) #costo de capuchino herraje 1038 con factura
            mp[41][14] = round((mp[41][5] * mp[41][11]), 2) #costo de capuchino herraje 1038 con descuento

            mp[43][11] = round((cantidad * 2), 2) # cantidad de zocalo inferior herraje 1103
            mp[43][13] = round((mp[43][4] * mp[43][11]), 2) #costo de zocalo inferior herraje 1103 con factura
            mp[43][14] = round((mp[43][5] * mp[43][11]), 2) #costo de zocalo inferior herraje 1103 con descuento

            mp[44][11] = round((cantidad * 2), 2) # cantidad de zocalo superior herraje 1101
            mp[44][13] = round((mp[44][4] * mp[44][11]), 2) #costo de zocalo superior herraje 1101 con factura
            mp[44][14] = round((mp[44][5] * mp[44][11]), 2) #costo de zocalo superior herraje 1101 con descuento

            mp[67][11] = round(cantidad, 2) # cantidad de chapas herraje 1520
            mp[67][13] = round((mp[67][4] * mp[67][11]), 2) #costo de chapas herraje 1520 con factura
            mp[67][14] = round((mp[67][5] * mp[67][11]), 2) #costo de chapas herraje 1520 con descuento

            mp[69][11] = round(cantidad, 2) # cantidad de contrachapa  herraje 1531
            mp[69][13] = round((mp[69][4] * mp[69][11]), 2) #costo de contrachapa herraje 1531 con factura
            mp[69][14] = round((mp[69][5] * mp[69][11]), 2) #costo de contrachapa herraje 1531 con descuento

            mp[51][11] = round(cantidad * 2, 2) # cantidad de capuchino para picaporte herraje 1201
            mp[51][13] = round((mp[51][4] * mp[51][11]), 2) #costo de capuchino para picaporte herraje 1201 con factura
            mp[51][14] = round((mp[51][5] * mp[51][11]), 2) #costo de capuchino para picaporte herraje 1201 con descuento

            if freno == "Con Freno":
                mp[37][11] = cantidad * 2 # cantidad de frenos
                mp[37][13] = round((mp[37][4] * mp[37][11]), 2) #costo de frenos con factura
                mp[37][14] = round((mp[37][5] * mp[37][11]), 2) #costo de frenos con descuento

            elif freno == "Sin Freno":
                mp[40][11] = cantidad * 2 # cantidad de pivote loco herraje 1013
                mp[40][13] = round((mp[40][4] * mp[40][11]), 2) #costo de pivote loco herraje 1013 con factura
                mp[40][14] = round((mp[40][5] * mp[40][11]), 2) #costo de pivote loco herraje 1013 con descuento

            accesorios = round((mp[51][13] + mp[69][13] + mp[67][13] + mp[44][13] + mp[43][13] + mp[41][13] + mp[61][13] + mp[38][13] + mp[37][13] + mp[40][13]), 2)
            
            messagebox.showinfo("cot", str(cantidad)+"  Frente(s) de Vidrio Templado tipo Spyder \n de  "+str(base)+"  Mt. de base   x  "+str(altura)+"  Mt. de altura ==> "+str(base * altura * cantidad)+ " Mt2. \n TOTAL COSTO PARCIAL  "+str(vidrio + mp[75][13] + accesorios)+" $us \n Costo de vidrio templado =  "+str(vidrio)+"  $us \n Costo de la mano de obra  =  "+str(mp[75][13])+" $us. \n Costo de accesorios  = "+str(accesorios)+"  $us. ")  

            if color == "Incoloro":
                mp[233][4] = cantidad 
                mp[233][5] = mp[75][11]
                mp[233][6] = mp[75][13]
                mp[233][7] = accesorios
                mp[233][8] = vidrio
                mp[233][9] = vidrio + accesorios + mp[75][13]

            elif color == "Color":
                mp[234][4] = cantidad 
                mp[234][5] = mp[75][11]
                mp[234][6] = mp[75][13]
                mp[234][7] = accesorios
                mp[234][8] = vidrio 
                mp[234][9] = vidrio + accesorios + mp[75][13]  
          
            for i in range(1, 237, 1):
                for j in range(11, 19, 1):
                    acum[i][j] += mp[i][j]
            
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    acum[i][j] += mp[i][j]   
    
            self.ventana.destroy()
            application=opcion()
        else:
            messagebox.showinfo("NO", "ERROR algun dato ingresado no es correcto o no ingresaste algún dato")

class op10:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("380x740")
        self.ventana.title("Op1")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="PUERTA BATIENE \n 2 HOJAS CON 2 FIJOS LATERALES", font=("Comic Sans", 14,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=15)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/op10a.png")
        self.img = self.img.resize((260,260))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand="True", fill="both", side="top", pady=0)

        self.label_base = Label(self.frame2, text="BASE en metros : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_base.grid(row=0, column=0, padx=5, pady=3, sticky="e")
        self.entry_base = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_base.grid(row=0, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.label_altura = Label(self.frame2, text="ALTURA en metros :",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_altura.grid(row=1, column=0, padx=5, pady=3, sticky="e")
        self.entry_altura = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_altura.grid(row=1, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_cantidad = Label(self.frame2, text="CANTIDAD : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_cantidad.grid(row=2, column=0, padx=5, pady=3, sticky="e")
        self.entry_cantidad = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_cantidad.grid(row=2, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_color = Label(self.frame2, text="VIDRIO INCOLORO ó COLOR  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_color.grid(row=4, column=0, padx=5, pady=3, sticky="e")
        self.color_v = StringVar()
        self.lista2 = ["Incoloro", "Color"]
        self.opciones2 = OptionMenu(self.frame2, self.color_v, *self.lista2)
        self.opciones2.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.color_v.set("???????")
        self.opciones2.grid(row=4, column=1, padx=5, pady=3, sticky="e")

        self.label_nvertical = Label(self.frame2, text="N DIV. VERTICALES : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_nvertical.grid(row=5, column=0, padx=5, pady=3, sticky="e")
        self.entry_nvertical = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_nvertical.grid(row=5, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_freno = Label(self.frame2, text="CON FRENO O SIN FRENO ?  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_freno.grid(row=6, column=0, padx=5, pady=3, sticky="e")
        self.freno = StringVar()
        self.lista4 = ["Con Freno", "Sin Freno"]
        self.opciones4 = OptionMenu(self.frame2, self.freno, *self.lista4)
        self.opciones4.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.freno.set("?????????")
        self.opciones4.grid(row=6, column=1, padx=5, pady=3, sticky="e")
        
        self.boton_cotizar = Button(self.frame2, text="COTIZAR Y SEGUIR", width=18, font=("Comic Sans", 11,"bold"), command=self.cotizar)
        self.boton_cotizar.grid(row=8, column=0, pady=15, columnspan=1, padx=25, sticky="w")

        self.boton_salir = Button(self.frame2, text="SALIR", width=18, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=8, column=1, pady=15, columnspan=1, padx=10, sticky="ew")

        mainloop()
    
    def salir(self):
        self.ventana.destroy()
        application=login()

    def cotizar(self):
        if len(self.entry_base.get()) != 0 and len(self.entry_altura.get()) != 0 and len(self.entry_cantidad.get()) != 0 and len(self.freno.get()) != 0 and len(self.color_v.get()) != 0 and len(self.entry_nvertical.get()) != 0:
            while True:
                try:
                    x = float(self.entry_base.get())
                    y = float(self.entry_altura.get())
                    break

                except ValueError:                
                    messagebox.showinfo("NO", "ERROR ....... La medida de la BASE ó ALTURA no son correctas, revise los doatos ingresados e introduzca nuevamente los valores .... RECUERDE LA SEPARACION DECIMAL ES CON PUNTO . ")
                    return(False)
                
            while True:
                try:
                    x = int(self.entry_cantidad.get())
                    y = int(self.entry_nvertical.get())
                    break

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... La CANTIDAD O LAS DIVISIONES, no son correctas, revise los datos ingresados e introduzca nuevamente los valores correctos.... RECUERDE QUE DEBEN SER NUMEROS SIN DECIMALES")
                    return(False)
                
            while True:
                try:
                    y = str(self.color_v.get())
                    w = str(self.freno.get())
                    if y == "Incoloro" or y == "Color":
                        if w == "Con Freno" or w == "Sin Freno":
                            break
                        else:
                            return(False)
                    else:
                        return(False)

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... El ESPESOR Y EL COLOR DEBEN SER SELECCIONADOS, revise si fueron seleccionados y seleccione la opcion deseada...")
                    return(False)
                
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            cantidad = int(self.entry_cantidad.get())
            color = self.color_v.get()
            nvertical = int(self.entry_nvertical.get())
            freno = self.freno.get()

            mp = inicia

            for i in range(0, 237, 1):
                for j in range(11, 19, 1):
                    mp[i][j] = 0.00
                                        
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    mp[i][j] = 0.00

            mp[196][3] = acum[196][3]
            mp[197][3] = acum[197][3]
            mp[198][3] = acum[198][3]
            mp[199][3] = acum[199][3]
            mp[200][3] = acum[200][3]
            mp[201][3] = acum[201][3]
            mp[202][3] = acum[202][3]

            if color == "Incoloro":
                mp[17][11] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[17][12] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[17][13] = round((mp[17][12] * mp[17][4]), 2) #costo del vidrio templado con factura
                mp[17][14] = round((mp[17][12] * mp[17][5]), 2) #costo del vidrio templado con descuento
                vidrio = round(mp[17][13], 2)

            elif color == "Color":
                mp[22][11] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[22][12] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[22][13] = round((mp[22][12] * mp[22][4]), 2) #costo del vidrio templado con factura
                mp[22][14] = round((mp[22][12] * mp[22][5]), 2) #costo del vidrio templado con descuento
                vidrio = round(mp[22][13], 2)                

            mp[75][11] = round((cantidad * base * altura), 2)
            mp[75][12] = mp[75][11]
            mp[75][13] = round((mp[75][11] * mp[75][4]), 2)  #costo mano de obra con factura
            mp[75][14] = round((mp[75][11] * mp[75][5]), 2)  #costo mano de obra con descuento
            
            mp[38][11] = round((cantidad * 4), 2) # cantidad de Jaladores Tipo C o manijones de vidrio
            mp[38][13] = round((mp[38][4] * mp[38][11]), 2) #costo jaladores Tipo C o manijones de vidrio con factura
            mp[38][14] = round((mp[38][5] * mp[38][11]), 2) #costo jaladores Tipo C o manijones de vidrio con descuento
            
            mp[61][11] = round((cantidad * 3), 2) # cantidad de picaportes herraje 1335
            mp[61][13] = round((mp[61][4] * mp[61][11]), 2) #costo de picaportes herraje 1335 con factura
            mp[61][14] = round((mp[61][5] * mp[61][11]), 2) #costo de picaportes herraje 1335 con descuento  
            
            mp[41][11] = round((cantidad * 4), 2) # cantidad de capuchino herraje 1038
            mp[41][13] = round((mp[41][4] * mp[41][11]), 2) #costo de capuchino herraje 1038 con factura
            mp[41][14] = round((mp[41][5] * mp[41][11]), 2) #costo de capuchino herraje 1038 con descuento

            mp[43][11] = round((cantidad * 2), 2) # cantidad de zocalo inferior herraje 1103
            mp[43][13] = round((mp[43][4] * mp[43][11]), 2) #costo de zocalo inferior herraje 1103 con factura
            mp[43][14] = round((mp[43][5] * mp[43][11]), 2) #costo de zocalo inferior herraje 1103 con descuento

            mp[44][11] = round((cantidad * 2), 2) # cantidad de zocalo superior herraje 1101
            mp[44][13] = round((mp[44][4] * mp[44][11]), 2) #costo de zocalo superior herraje 1101 con factura
            mp[44][14] = round((mp[44][5] * mp[44][11]), 2) #costo de zocalo superior herraje 1101 con descuento

            mp[67][11] = round(cantidad, 2) # cantidad de chapas herraje 1520
            mp[67][13] = round((mp[67][4] * mp[67][11]), 2) #costo de chapas herraje 1520 con factura
            mp[67][14] = round((mp[67][5] * mp[67][11]), 2) #costo de chapas herraje 1520 con descuento

            mp[69][11] = round(cantidad, 2) # cantidad de contrachapa herraje 1531
            mp[69][13] = round((mp[69][4] * mp[69][11]), 2) #costo de contrachapa herraje 1531 con factura
            mp[69][14] = round((mp[69][5] * mp[69][11]), 2) #costo de contrachapa herraje 1531 con descuento

            mp[51][11] = round((cantidad * 2), 2) # cantidad de capuchino para picaporte herraje 1201
            mp[51][13] = round((mp[51][4] * mp[51][11]), 2) #costo de capuchino para picaporte herraje 1201 para trinco con factura
            mp[51][14] = round((mp[51][5] * mp[51][11]), 2) #costo de capuchino para picaporte herraje 1201 para trinco con descuento

            mp[1][11] = round(((cantidad * ((2 * base) + (2 * altura) + ((nvertical-1) * altura))) / 6), 2) # cantidad de silicona normal
            mp[1][13] = round((mp[1][4] * mp[1][11]), 2) #costo silicona natural con factura
            mp[1][14] = round((mp[1][5] * mp[1][11]), 2) #costo silicona natural con descuento
            
            mp[3][11] = round(((cantidad * ((2 * base) + (2 * altura) + ((nvertical-1) * altura))) * 2 / 20), 2) # cantidad de cinta masking
            mp[3][13] = round((mp[3][4] * mp[3][11]), 2) #costo cinta masking con factura
            mp[3][14] = round((mp[3][5] * mp[3][11]), 2) #costo cinta masking con descuento  
            
            mp[5][11] = round((cantidad * ((2 * base) + (2 * altura)) / 6), 2) # cantidad de perfil U 15 x 25 incoloro o bronce
            mp[5][13] = round((mp[5][4] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con factura
            mp[5][14] = round((mp[5][5] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con descuento

            mp[14][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tornillo de 8 x 1 1/2
            mp[14][13] = round((mp[14][4] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con factura
            mp[14][14] = round((mp[14][5] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con descuento

            mp[13][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tarugos No. 6
            mp[13][13] = round((mp[13][4] * mp[13][11]), 2) #costo de tarugos No. 6 con factura
            mp[13][14] = round((mp[13][5] * mp[13][11]), 2) #costo de tarugos No. 6 con descuento

            if freno == "Con Freno":
                mp[37][11] = cantidad * 2 # cantidad de frenos
                mp[37][13] = round((mp[37][4] * mp[37][11]), 2) #costo de frenos con factura
                mp[37][14] = round((mp[37][5] * mp[37][11]), 2) #costo de frenos con descuento

            elif freno == "Sin Freno":
                mp[40][11] = cantidad * 2 # cantidad de pivote loco herraje 1013
                mp[40][13] = round((mp[40][4] * mp[40][11]), 2) #costo de pivote loco herraje 1013 con factura
                mp[40][14] = round((mp[40][5] * mp[40][11]), 2) #costo de pivote loco herraje 1013 con descuento

            accesorios = round((mp[37][13] + mp[38][13] + mp[40][13] + mp[61][13] + mp[43][13] + mp[44][13] + mp[67][13] + mp[69][13] + mp[41][13] + mp[51][13] + mp[1][13] + mp[3][13] + mp[5][13] + mp[14][13] + mp[13][13]), 2)
            
            messagebox.showinfo("cot", str(cantidad)+"  Frente(s) de Vidrio Templado tipo Spyder \n de  "+str(base)+"  Mt. de base   x  "+str(altura)+"  Mt. de altura ==> "+str(base * altura * cantidad)+ " Mt2. \n TOTAL COSTO PARCIAL  "+str(vidrio + mp[75][13] + accesorios)+" $us \n Costo de vidrio templado =  "+str(vidrio)+"  $us \n Costo de la mano de obra  =  "+str(mp[75][13])+" $us. \n Costo de accesorios  = "+str(accesorios)+"  $us. ")  

            if color == "Incoloro":
                mp[235][4] = cantidad 
                mp[235][5] = mp[75][11]
                mp[235][6] = mp[75][13]
                mp[235][7] = accesorios
                mp[235][8] = vidrio
                mp[235][9] = vidrio + accesorios + mp[75][13]

            elif color == "Color":
                mp[236][4] = cantidad 
                mp[236][5] = mp[75][11]
                mp[236][6] = mp[75][13]
                mp[236][7] = accesorios
                mp[236][8] = vidrio
                mp[236][9] = vidrio + accesorios + mp[75][13] 
                          
            for i in range(1, 237, 1):
                for j in range(11, 19, 1):
                    acum[i][j] += mp[i][j]
            
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    acum[i][j] += mp[i][j]   
        
            self.ventana.destroy()
            application=opcion()
        else:
            messagebox.showinfo("NO", "ERROR algun dato ingresado no es correcto o no ingresaste algún dato")

class op11:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("380x740")
        self.ventana.title("Op1")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="PUERTA BATIENE \n 2 HOJAS CON FIJO SUPERIOR", font=("Comic Sans", 14,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=15)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/op11a.png")
        self.img = self.img.resize((260,260))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand="True", fill="both", side="top", pady=0)

        self.label_base = Label(self.frame2, text="BASE en metros : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_base.grid(row=0, column=0, padx=5, pady=3, sticky="e")
        self.entry_base = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_base.grid(row=0, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.label_altura = Label(self.frame2, text="ALTURA en metros :",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_altura.grid(row=1, column=0, padx=5, pady=3, sticky="e")
        self.entry_altura = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_altura.grid(row=1, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_cantidad = Label(self.frame2, text="CANTIDAD : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_cantidad.grid(row=2, column=0, padx=5, pady=3, sticky="e")
        self.entry_cantidad = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_cantidad.grid(row=2, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_color = Label(self.frame2, text="VIDRIO INCOLORO ó COLOR  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_color.grid(row=4, column=0, padx=5, pady=3, sticky="e")
        self.color_v = StringVar()
        self.lista2 = ["Incoloro", "Color"]
        self.opciones2 = OptionMenu(self.frame2, self.color_v, *self.lista2)
        self.opciones2.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.color_v.set("???????")
        self.opciones2.grid(row=4, column=1, padx=5, pady=3, sticky="e")

        self.label_freno = Label(self.frame2, text="CON FRENO O SIN FRENO ?  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_freno.grid(row=6, column=0, padx=5, pady=3, sticky="e")
        self.freno = StringVar()
        self.lista4 = ["Con Freno", "Sin Freno"]
        self.opciones4 = OptionMenu(self.frame2, self.freno, *self.lista4)
        self.opciones4.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.freno.set("?????????")
        self.opciones4.grid(row=6, column=1, padx=5, pady=3, sticky="e")
        
        self.boton_cotizar = Button(self.frame2, text="COTIZAR Y SEGUIR", width=18, font=("Comic Sans", 11,"bold"), command=self.cotizar)
        self.boton_cotizar.grid(row=8, column=0, pady=15, columnspan=1, padx=25, sticky="w")

        self.boton_salir = Button(self.frame2, text="SALIR", width=18, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=8, column=1, pady=15, columnspan=1, padx=10, sticky="ew")

        mainloop()
    
    def salir(self):
        self.ventana.destroy()
        application=login()

    def cotizar(self):
        if len(self.entry_base.get()) != 0 and len(self.entry_altura.get()) != 0 and len(self.entry_cantidad.get()) != 0 and len(self.freno.get()) != 0 and len(self.color_v.get()) != 0: 
            while True:
                try:
                    x = float(self.entry_base.get())
                    y = float(self.entry_altura.get())
                    break

                except ValueError:
                
                    messagebox.showinfo("NO", "ERROR ....... La medida de la BASE ó ALTURA no son correctas, revise los doatos ingresados e introduzca nuevamente los valores .... RECUERDE LA SEPARACION DECIMAL ES CON PUNTO . ")
                    return(False)
                
            while True:
                try:
                    x = int(self.entry_cantidad.get())
                    break

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... La CANTIDAD O LAS DIVISIONES, no son correctas, revise los datos ingresados e introduzca nuevamente los valores correctos.... RECUERDE QUE DEBEN SER NUMEROS SIN DECIMALES")
                    return(False)
                
            while True:
                try:
                    y = str(self.color_v.get())
                    w = str(self.freno.get())
                    if y == "Incoloro" or y == "Color":
                        if w == "Con Freno" or w == "Sin Freno":
                            break
                        else:
                            return(False)
                    else:
                        return(False)

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... El ESPESOR Y EL COLOR DEBEN SER SELECCIONADOS, revise si fueron seleccionados y seleccione la opcion deseada...")
                    return(False)
                
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            cantidad = int(self.entry_cantidad.get())
            color = self.color_v.get()
            freno = self.freno.get()

            mp = inicia

            for i in range(0, 237, 1):
                for j in range(11, 19, 1):
                    mp[i][j] = 0.00
                                        
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    mp[i][j] = 0.00

            mp[196][3] = acum[196][3]
            mp[197][3] = acum[197][3]
            mp[198][3] = acum[198][3]
            mp[199][3] = acum[199][3]
            mp[200][3] = acum[200][3]
            mp[201][3] = acum[201][3]
            mp[202][3] = acum[202][3]

            if color == "Incoloro":
                mp[17][11] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[17][12] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[17][13] = round((mp[17][12] * mp[17][4]), 2) #costo del vidrio templado con factura
                mp[17][14] = round((mp[17][12] * mp[17][5]), 2) #costo del vidrio templado con descuento
                vidrio = round(mp[17][13], 2)

            elif color == "Color":
                mp[22][11] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[22][12] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[22][13] = round((mp[22][12] * mp[22][4]), 2) #costo del vidrio templado con factura
                mp[22][14] = round((mp[22][12] * mp[22][5]), 2) #costo del vidrio templado con descuento
                vidrio = round(mp[22][13], 2)                

            mp[75][11] = round((cantidad * base * altura), 2)
            mp[75][12] = mp[75][11]
            mp[75][13] = round((mp[75][11] * mp[75][4]), 2)  #costo mano de obra con factura
            mp[75][14] = round((mp[75][11] * mp[75][5]), 2)  #costo mano de obra con descuento
            
            mp[38][11] = round((cantidad * 4), 2) # cantidad de Jaladores Tipo C o manijones de vidrio templado
            mp[38][13] = round((mp[38][4] * mp[38][11]), 2) #costo jaladores Tipo C o manijones de vidrio templado con factura
            mp[38][14] = round((mp[38][5] * mp[38][11]), 2) #costo jaladores Tipo C o manijones de vidrio templado con descuento
            
            mp[61][11] = round((cantidad * 3), 2) # cantidad de picaportes herraje 1335
            mp[61][13] = round((mp[61][4] * mp[61][11]), 2) #costo de picaportes herraje 1335 con factura
            mp[61][14] = round((mp[61][5] * mp[61][11]), 2) #costo de picaportes herraje 1335 con descuento  
            
            mp[41][11] = round((cantidad * 4), 2) # cantidad de capuchino para picaporte herraje 1038
            mp[41][13] = round((mp[41][4] * mp[41][11]), 2) #costo de capuchino para picaporte herraje 1038 con factura
            mp[41][14] = round((mp[41][5] * mp[41][11]), 2) #costo de capuchino para picaporte herraje 1038 con descuento

            mp[43][11] = round((cantidad * 2), 2) # cantidad de zocalo inferior herraje 1103
            mp[43][13] = round((mp[43][4] * mp[43][11]), 2) #costo de zocalo inferior herraje 1103 con factura
            mp[43][14] = round((mp[43][5] * mp[43][11]), 2) #costo de zocalo inferior herraje 1103 con descuento

            mp[44][11] = round((cantidad * 2), 2) # cantidad de zocalo superior herraje 1101
            mp[44][13] = round((mp[44][4] * mp[44][11]), 2) #costo de zocalo superior herraje 1101 con factura
            mp[44][14] = round((mp[44][5] * mp[44][11]), 2) #costo de zocalo superior herraje 1101 con descuento

            mp[67][11] = round(cantidad, 2) # cantidad de chapas herraje 1520
            mp[67][13] = round((mp[67][4] * mp[67][11]), 2) #costo de chapas herraje 1520 con factura
            mp[67][14] = round((mp[67][5] * mp[67][11]), 2) #costo de chapas herraje 1520 con descuento

            mp[69][11] = round(cantidad, 2) # cantidad de contrachapa herraje 1531
            mp[69][13] = round((mp[69][4] * mp[69][11]), 2) #costo de contrachapa herraje 1531 con factura
            mp[69][14] = round((mp[69][5] * mp[69][11]), 2) #costo de contrachapa herraje 1531 con descuento

            mp[51][11] = round((cantidad * 2), 2) # cantidad de capuchino para picaporte herraje 1201
            mp[51][13] = round((mp[51][4] * mp[51][11]), 2) #costo de capuchino para picaporte herraje 1201 con factura
            mp[51][14] = round((mp[51][5] * mp[51][11]), 2) #costo de capuchino para picaporte herraje 1201 con descuento

            mp[62][11] = round(cantidad, 2) # cantidad de contrapicaporte al vidrio herraje 1335c
            mp[62][13] = round((mp[62][4] * mp[62][11]), 2) #costo de contrapicaporte al vidrio herraje 1335c con factura
            mp[62][14] = round((mp[62][5] * mp[62][11]), 2) #costo de contrapicaporte al vidrio herraje 1335c con descuento

            mp[52][11] = round((cantidad * 2), 2) # cantidad de soporte con miolo superior al vidrio y al muro herraje 1203
            mp[52][13] = round((mp[52][4] * mp[52][11]), 2) #costo de soporte con miolo superior al vidrio y al muro herraje 1203 con factura
            mp[52][14] = round((mp[52][5] * mp[52][11]), 2) #costo de soporte con miolo superior al vidrio y al muro herraje 1203 con descuento

            mp[1][11] = round(((cantidad * (base + altura)) / 6), 2) # cantidad de silicona normal
            mp[1][13] = round((mp[1][4] * mp[1][11]), 2) #costo silicona natural con factura
            mp[1][14] = round((mp[1][5] * mp[1][11]), 2) #costo silicona natural con descuento
            
            mp[3][11] = round(((cantidad * (base + altura) * 2) / 20), 2) # cantidad de cinta masking
            mp[3][13] = round((mp[3][4] * mp[3][11]), 2) #costo cinta masking con factura
            mp[3][14] = round((mp[3][5] * mp[3][11]), 2) #costo cinta masking con descuento  
            
            mp[5][11] = round((cantidad * (base + altura) / 6), 2) # cantidad de perfil U 15 x 25 incoloro o bronce
            mp[5][13] = round((mp[5][4] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con factura
            mp[5][14] = round((mp[5][5] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con descuento

            mp[14][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tornillo de 8 x 1 1/2
            mp[14][13] = round((mp[14][4] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con factura
            mp[14][14] = round((mp[14][5] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con descuento

            mp[13][11] = round(((cantidad * ((base * 2) + (2 * altura))) / 0.4), 2) # cantidad de tarugos No. 6
            mp[13][13] = round((mp[13][4] * mp[13][11]), 2) #costo de tarugos No. 6 con factura
            mp[13][14] = round((mp[13][5] * mp[13][11]), 2) #costo de tarugos No. 6 con descuento

            if freno == "Con Freno":
                mp[37][11] = cantidad * 2 # cantidad de frenos
                mp[37][13] = round((mp[37][4] * mp[37][11]), 2) #costo de frenos con factura
                mp[37][14] = round((mp[37][5] * mp[37][11]), 2) #costo de frenos con descuento

            elif freno == "Sin Freno":
                mp[40][11] = cantidad * 2 # cantidad de pivote loco herraje 1013
                mp[40][13] = round((mp[40][4] * mp[40][11]), 2) #costo de pivote loco herraje 1013 con factura
                mp[40][14] = round((mp[40][5] * mp[40][11]), 2) #costo de pivote loco herraje 1013 con descuento

            accesorios = round((mp[37][13] + mp[38][13] + mp[40][13] + mp[61][13] + mp[43][13] + mp[44][13] + mp[67][13] + mp[69][13] + mp[41][13] + mp[51][13] + mp[62][13] + mp[52][13] + mp[1][13] + mp[3][13] + mp[5][13] + mp[14][13] + mp[13][13]), 2)
            
            messagebox.showinfo("cot", str(cantidad)+"  Frente(s) de Vidrio Templado tipo Spyder \n de  "+str(base)+"  Mt. de base   x  "+str(altura)+"  Mt. de altura ==> "+str(base * altura * cantidad)+ " Mt2. \n TOTAL COSTO PARCIAL  "+str(vidrio + mp[75][13] + accesorios)+" $us \n Costo de vidrio templado =  "+str(vidrio)+"  $us \n Costo de la mano de obra  =  "+str(mp[75][13])+" $us. \n Costo de accesorios  = "+str(accesorios)+"  $us. ")  

            if color == "Incoloro":
                mp[235][4] = cantidad 
                mp[235][5] = mp[75][11]
                mp[235][6] = mp[75][13]
                mp[235][7] = accesorios
                mp[235][8] = vidrio
                mp[235][9] = vidrio + accesorios + mp[75][13]

            elif color == "Color":
                mp[236][4] = cantidad 
                mp[236][5] = mp[75][11]
                mp[236][6] = mp[75][13]
                mp[236][7] = accesorios
                mp[236][8] = vidrio
                mp[236][9] = vidrio + accesorios + mp[75][13]   
                          
            for i in range(1, 237, 1):
                for j in range(11, 19, 1):
                    acum[i][j] += mp[i][j]
            
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    acum[i][j] += mp[i][j] 

            self.ventana.destroy()
            application=opcion()
        else:
            messagebox.showinfo("NO", "ERROR algun dato ingresado no es correcto o no ingresaste algún dato")

class op12:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("380x740")
        self.ventana.title("Op1")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="PUERTA BATIENE \n 2 HOJAS CON FIJOS LATERAL Y SUPERIOR AL MURO", font=("Comic Sans", 14,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=15)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/op12a.png")
        self.img = self.img.resize((260,260))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand="True", fill="both", side="top", pady=0)

        self.label_base = Label(self.frame2, text="BASE en metros : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_base.grid(row=0, column=0, padx=5, pady=3, sticky="e")
        self.entry_base = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_base.grid(row=0, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.label_altura = Label(self.frame2, text="ALTURA en metros :",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_altura.grid(row=1, column=0, padx=5, pady=3, sticky="e")
        self.entry_altura = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_altura.grid(row=1, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_cantidad = Label(self.frame2, text="CANTIDAD : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_cantidad.grid(row=2, column=0, padx=5, pady=3, sticky="e")
        self.entry_cantidad = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_cantidad.grid(row=2, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_color = Label(self.frame2, text="VIDRIO INCOLORO ó COLOR  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_color.grid(row=4, column=0, padx=5, pady=3, sticky="e")
        self.color_v = StringVar()
        self.lista2 = ["Incoloro", "Color"]
        self.opciones2 = OptionMenu(self.frame2, self.color_v, *self.lista2)
        self.opciones2.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.color_v.set("???????")
        self.opciones2.grid(row=4, column=1, padx=5, pady=3, sticky="e")

        self.label_nvertical = Label(self.frame2, text="N DIV. VERTICALES : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_nvertical.grid(row=5, column=0, padx=5, pady=3, sticky="e")
        self.entry_nvertical = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_nvertical.grid(row=5, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_freno = Label(self.frame2, text="CON FRENO O SIN FRENO ?  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_freno.grid(row=6, column=0, padx=5, pady=3, sticky="e")
        self.freno = StringVar()
        self.lista4 = ["Con Freno", "Sin Freno"]
        self.opciones4 = OptionMenu(self.frame2, self.freno, *self.lista4)
        self.opciones4.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.freno.set("?????????")
        self.opciones4.grid(row=6, column=1, padx=5, pady=3, sticky="e")
        
        self.boton_cotizar = Button(self.frame2, text="COTIZAR Y SEGUIR", width=18, font=("Comic Sans", 11,"bold"), command=self.cotizar)
        self.boton_cotizar.grid(row=8, column=0, pady=15, columnspan=1, padx=25, sticky="w")

        self.boton_salir = Button(self.frame2, text="SALIR", width=18, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=8, column=1, pady=15, columnspan=1, padx=10, sticky="ew")

        mainloop()
    
    def salir(self):
        self.ventana.destroy()
        application=login()

    def cotizar(self):
        if len(self.entry_base.get()) != 0 and len(self.entry_altura.get()) != 0 and len(self.entry_cantidad.get()) != 0 and len(self.freno.get()) != 0 and len(self.color_v.get()) != 0 and len(self.entry_nvertical.get()) != 0:
            while True:
                try:
                    x = float(self.entry_base.get())
                    y = float(self.entry_altura.get())
                    break

                except ValueError:                
                    messagebox.showinfo("NO", "ERROR ....... La medida de la BASE ó ALTURA no son correctas, revise los doatos ingresados e introduzca nuevamente los valores .... RECUERDE LA SEPARACION DECIMAL ES CON PUNTO . ")
                    return(False)
                
            while True:
                try:
                    x = int(self.entry_cantidad.get())
                    y = int(self.entry_nvertical.get())
                    break

                except ValueError:
                    messagebox.showinfo("NO", "ERROR ....... La CANTIDAD O LAS DIVISIONES, no son correctas, revise los datos ingresados e introduzca nuevamente los valores correctos.... RECUERDE QUE DEBEN SER NUMEROS SIN DECIMALES")
                    return(False)
                
            while True:
                try:
                    y = str(self.color_v.get())
                    w = str(self.freno.get())
                    if y == "Incoloro" or y == "Color":
                        if w == "Con Freno" or w == "Sin Freno":
                            break
                        else:
                            return(False)
                    else:
                        return(False)

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... El ESPESOR Y EL COLOR DEBEN SER SELECCIONADOS, revise si fueron seleccionados y seleccione la opcion deseada...")
                    return(False)
                
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            cantidad = int(self.entry_cantidad.get())
            color = self.color_v.get()
            nvertical = int(self.entry_nvertical.get())
            freno = self.freno.get()

            mp = inicia

            for i in range(0, 237, 1):
                for j in range(11, 19, 1):
                    mp[i][j] = 0.00
                                        
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    mp[i][j] = 0.00

            mp[196][3] = acum[196][3]
            mp[197][3] = acum[197][3]
            mp[198][3] = acum[198][3]
            mp[199][3] = acum[199][3]
            mp[200][3] = acum[200][3]
            mp[201][3] = acum[201][3]
            mp[202][3] = acum[202][3]

            if color == "Incoloro":
                mp[17][11] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[17][12] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[17][13] = round((mp[17][12] * mp[17][4]), 2) #costo del vidrio templado con factura
                mp[17][14] = round((mp[17][12] * mp[17][5]), 2) #costo del vidrio templado con descuento
                vidrio = round(mp[17][13], 2)

            elif color == "Color":
                mp[22][11] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[22][12] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[22][13] = round((mp[22][12] * mp[22][4]), 2) #costo del vidrio templado con factura
                mp[22][14] = round((mp[22][12] * mp[22][5]), 2) #costo del vidrio templado con descuento
                vidrio = round(mp[22][13], 2)                

            mp[75][11] = round((cantidad * base * altura), 2)
            mp[75][12] = mp[75][11]
            mp[75][13] = round((mp[75][11] * mp[75][4]), 2)  #costo mano de obra con factura
            mp[75][14] = round((mp[75][11] * mp[75][5]), 2)  #costo mano de obra con descuento
            
            mp[38][11] = round((cantidad * 4), 2) # cantidad de Jaladores Tipo C o manijomnes de vidrio templado
            mp[38][13] = round((mp[38][4] * mp[38][11]), 2) #costo jaladores Tipo C o manijomnes de vidrio templado con factura
            mp[38][14] = round((mp[38][5] * mp[38][11]), 2) #costo jaladores Tipo C o manijomnes de vidrio templado con descuento
            
            mp[61][11] = round((cantidad * 3), 2) # cantidad de picaportes herraje 1335
            mp[61][13] = round((mp[61][4] * mp[61][11]), 2) #costo picaportes herraje 1335 con factura
            mp[61][14] = round((mp[61][5] * mp[61][11]), 2) #costo picaportes herraje 1335 con descuento  
            
            mp[41][11] = round((cantidad * 4), 2) # cantidad de capuchino herraje 1038
            mp[41][13] = round((mp[41][4] * mp[41][11]), 2) #costo de capuchino herraje 1038 con factura
            mp[41][14] = round((mp[41][5] * mp[41][11]), 2) #costo de capuchino herraje 1038 con descuento

            mp[43][11] = round((cantidad * 2), 2) # cantidad de zocalo inferior herraje 1103
            mp[43][13] = round((mp[43][4] * mp[43][11]), 2) #costo de zocalo inferior herraje 1103 con factura
            mp[43][14] = round((mp[43][5] * mp[43][11]), 2) #costo de zocalo inferior herraje 1103 con descuento

            mp[44][11] = round((cantidad * 2), 2) # cantidad de zocalo superior herraje 1101
            mp[44][13] = round((mp[44][4] * mp[44][11]), 2) #costo de zocalo superior herraje 1101 con factura
            mp[44][14] = round((mp[44][5] * mp[44][11]), 2) #costo de zocalo superior herraje 1101 con descuento

            mp[67][11] = round(cantidad, 2) # cantidad de chapas herraje 1520
            mp[67][13] = round((mp[67][4] * mp[67][11]), 2) #costo de chapas herraje 1520 con factura
            mp[67][14] = round((mp[67][5] * mp[67][11]), 2) #costo de chapas herraje 1520 con descuento

            mp[69][11] = round(cantidad, 2) # cantidad de contrachapa herraje 1531
            mp[69][13] = round((mp[69][4] * mp[69][11]), 2) #costo de contrachapa herraje 1531 con factura
            mp[69][14] = round((mp[69][5] * mp[69][11]), 2) #costo de contrachapa herraje 1531 con descuento

            mp[62][11] = round((cantidad * 1), 2) # cantidad de contrapicaporte al vidrio herraje 1335c
            mp[62][13] = round((mp[62][4] * mp[62][11]), 2) #costo de contrapicaporte al vidrio herraje 1335c con factura
            mp[62][14] = round((mp[62][5] * mp[62][11]), 2) #costo de contrapicaporte al vidrio herraje 1335c con descuento

            mp[52][11] = round(cantidad, 2) # cantidad de herraje 1203
            mp[52][13] = round((mp[52][4] * mp[52][11]), 2) #costo de herraje 1203 con factura
            mp[52][14] = round((mp[52][5] * mp[52][11]), 2) #costo de herraje 1203 con descuento

            mp[53][11] = round(cantidad, 2) # cantidad de pistola porta puerta herraje 1209
            mp[53][13] = round((mp[53][4] * mp[53][11]), 2) #costo de pistola porta puerta herraje 1209 con factura
            mp[53][14] = round((mp[53][5] * mp[53][11]), 2) #costo de pistola porta puerta herraje 1209 con descuento

            mp[55][11] = round(cantidad, 2) # cantidad de soporte central simple herraje 1329
            mp[55][13] = round((mp[55][4] * mp[55][11]), 2) #costo de soporte central simple herraje 1329 con factura
            mp[55][14] = round((mp[55][5] * mp[55][11]), 2) #costo de soporte central simple herraje 1329 con descuento

            mp[60][11] = round(cantidad, 2) # cantidad de soporte central simple herraje 1329
            mp[60][13] = round((mp[60][4] * mp[60][11]), 2) #costo soporte central simple herraje 1329 con factura
            mp[60][14] = round((mp[60][5] * mp[60][11]), 2) #costo soporte central simple herraje 1329 con descuento

            mp[1][11] = round(((cantidad * ((2 * base) + (2 * altura) + ((nvertical-1) * altura))) / 6), 2) # cantidad de silicona normal
            mp[1][13] = round((mp[1][4] * mp[1][11]), 2) #costo silicona natural con factura
            mp[1][14] = round((mp[1][5] * mp[1][11]), 2) #costo silicona natural con descuento
            
            mp[3][11] = round(((cantidad * ((2 * base) + (2 * altura) + ((nvertical-1) * altura))) * 2 / 20), 2) # cantidad de cinta masking
            mp[3][13] = round((mp[3][4] * mp[3][11]), 2) #costo cinta masking con factura
            mp[3][14] = round((mp[3][5] * mp[3][11]), 2) #costo cinta masking con descuento  
            
            mp[5][11] = round((cantidad * ((2 * base) + (2 * altura)) / 6), 2) # cantidad de perfil U 15 x 25 incoloro o bronce
            mp[5][13] = round((mp[5][4] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con factura
            mp[5][14] = round((mp[5][5] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con descuento

            mp[14][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tornillo de 8 x 1 1/2
            mp[14][13] = round((mp[14][4] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con factura
            mp[14][14] = round((mp[14][5] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con descuento

            mp[13][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tarugos No. 6
            mp[13][13] = round((mp[13][4] * mp[13][11]), 2) #costo de tarugos No. 6 con factura
            mp[13][14] = round((mp[13][5] * mp[13][11]), 2) #costo de tarugos No. 6 con descuento

            if freno == "Con Freno":
                mp[37][11] = cantidad * 2 # cantidad de frenos
                mp[37][13] = round((mp[37][4] * mp[37][11]), 2) #costo de frenos con factura
                mp[37][14] = round((mp[37][5] * mp[37][11]), 2) #costo de frenos con descuento

            elif freno == "Sin Freno":
                mp[40][11] = cantidad * 2 # cantidad de pivote loco herraje 1013
                mp[40][13] = round((mp[40][4] * mp[40][11]), 2) #costo de pivote loco herraje 1013 con factura
                mp[40][14] = round((mp[40][5] * mp[40][11]), 2) #costo de pivote loco herraje 1013 con descuento

            accesorios = round((mp[37][13] + mp[38][13] + mp[40][13] + mp[61][13] + mp[43][13] + mp[44][13] + mp[67][13] + mp[69][13] + mp[41][13] + mp[62][13] + mp[52][13] + mp[53][13] + mp[55][13] + mp[60][13] + mp[1][13] + mp[3][13] + mp[5][13] + mp[14][13] + mp[13][13]), 2)
            
            messagebox.showinfo("cot", str(cantidad)+"  Frente(s) de Vidrio Templado tipo Spyder \n de  "+str(base)+"  Mt. de base   x  "+str(altura)+"  Mt. de altura ==> "+str(base * altura * cantidad)+ " Mt2. \n TOTAL COSTO PARCIAL  "+str(vidrio + mp[75][13] + accesorios)+" $us \n Costo de vidrio templado =  "+str(vidrio)+"  $us \n Costo de la mano de obra  =  "+str(mp[75][13])+" $us. \n Costo de accesorios  = "+str(accesorios)+"  $us. ")  

            if color == "Incoloro":
                mp[235][4] = cantidad 
                mp[235][5] = mp[75][11]
                mp[235][6] = mp[75][13]
                mp[235][7] = accesorios
                mp[235][8] = vidrio
                mp[235][9] = vidrio + accesorios + mp[75][13]

            elif color == "Color":
                mp[236][4] = cantidad 
                mp[236][5] = mp[75][11]
                mp[236][6] = mp[75][13]
                mp[236][7] = accesorios
                mp[236][8] = vidrio 
                mp[236][9] = vidrio + accesorios + mp[75][13]  
                                  
            for i in range(1, 237, 1):
                for j in range(11, 19, 1):
                    acum[i][j] += mp[i][j]
            
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    acum[i][j] += mp[i][j]

            self.ventana.destroy()
            application=opcion()
        else:
            messagebox.showinfo("NO", "ERROR algun dato ingresado no es correcto o no ingresaste algún dato")

class op13:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("380x740")
        self.ventana.title("Op1")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="PUERTA BATIENTE \n 2 HOJAS CON FIJOS LATERALES Y SUPERIOR", font=("Comic Sans", 14,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=15)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/op13a.png")
        self.img = self.img.resize((260,260))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand="True", fill="both", side="top", pady=0)

        self.label_base = Label(self.frame2, text="BASE en metros : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_base.grid(row=0, column=0, padx=5, pady=3, sticky="e")
        self.entry_base = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_base.grid(row=0, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.label_altura = Label(self.frame2, text="ALTURA en metros :",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_altura.grid(row=1, column=0, padx=5, pady=3, sticky="e")
        self.entry_altura = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_altura.grid(row=1, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_cantidad = Label(self.frame2, text="CANTIDAD : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_cantidad.grid(row=2, column=0, padx=5, pady=3, sticky="e")
        self.entry_cantidad = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_cantidad.grid(row=2, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_color = Label(self.frame2, text="VIDRIO INCOLORO ó COLOR  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_color.grid(row=4, column=0, padx=5, pady=3, sticky="e")
        self.color_v = StringVar()
        self.lista2 = ["Incoloro", "Color"]
        self.opciones2 = OptionMenu(self.frame2, self.color_v, *self.lista2)
        self.opciones2.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.color_v.set("???????")
        self.opciones2.grid(row=4, column=1, padx=5, pady=3, sticky="e")

        self.label_nvertical = Label(self.frame2, text="N DIV. VERTICALES : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_nvertical.grid(row=5, column=0, padx=5, pady=3, sticky="e")
        self.entry_nvertical = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_nvertical.grid(row=5, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_freno = Label(self.frame2, text="CON FRENO O SIN FRENO ?  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_freno.grid(row=6, column=0, padx=5, pady=3, sticky="e")
        self.freno = StringVar()
        self.lista4 = ["Con Freno", "Sin Freno"]
        self.opciones4 = OptionMenu(self.frame2, self.freno, *self.lista4)
        self.opciones4.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.freno.set("?????????")
        self.opciones4.grid(row=6, column=1, padx=5, pady=3, sticky="e")
        
        self.boton_cotizar = Button(self.frame2, text="COTIZAR Y SEGUIR", width=18, font=("Comic Sans", 11,"bold"), command=self.cotizar)
        self.boton_cotizar.grid(row=8, column=0, pady=15, columnspan=1, padx=25, sticky="w")

        self.boton_salir = Button(self.frame2, text="SALIR", width=18, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=8, column=1, pady=15, columnspan=1, padx=10, sticky="ew")

        mainloop()
    
    def salir(self):
        self.ventana.destroy()
        application=login()

    def cotizar(self):
        if len(self.entry_base.get()) != 0 and len(self.entry_altura.get()) != 0 and len(self.entry_cantidad.get()) != 0 and len(self.freno.get()) != 0 and len(self.color_v.get()) != 0 and len(self.entry_nvertical.get()) != 0:
            while True:
                try:
                    x = float(self.entry_base.get())
                    y = float(self.entry_altura.get())
                    break

                except ValueError:
                
                    messagebox.showinfo("NO", "ERROR ....... La medida de la BASE ó ALTURA no son correctas, revise los doatos ingresados e introduzca nuevamente los valores .... RECUERDE LA SEPARACION DECIMAL ES CON PUNTO . ")
                    return(False)
                
            while True:
                try:
                    x = int(self.entry_cantidad.get())
                    y = int(self.entry_nvertical.get())
                    break

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... La CANTIDAD O LAS DIVISIONES, no son correctas, revise los datos ingresados e introduzca nuevamente los valores correctos.... RECUERDE QUE DEBEN SER NUMEROS SIN DECIMALES")
                    return(False)
                
            while True:
                try:
                    y = str(self.color_v.get())
                    w = str(self.freno.get())
                    if y == "Incoloro" or y == "Color":
                        if w == "Con Freno" or w == "Sin Freno":
                            break
                        else:
                            return(False)
                    else:
                        return(False)

                except ValueError:
                    messagebox.showinfo("NO", "ERROR ....... El ESPESOR Y EL COLOR DEBEN SER SELECCIONADOS, revise si fueron seleccionados y seleccione la opcion deseada...")
                    return(False)
                
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            cantidad = int(self.entry_cantidad.get())
            color = self.color_v.get()
            nvertical = int(self.entry_nvertical.get())
            freno = self.freno.get()

            mp = inicia

            for i in range(0, 237, 1):
                for j in range(11, 19, 1):
                    mp[i][j] = 0.00
                                        
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    mp[i][j] = 0.00

            mp[196][3] = acum[196][3]
            mp[197][3] = acum[197][3]
            mp[198][3] = acum[198][3]
            mp[199][3] = acum[199][3]
            mp[200][3] = acum[200][3]
            mp[201][3] = acum[201][3]
            mp[202][3] = acum[202][3]

            if color == "Incoloro":
                mp[17][11] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[17][12] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[17][13] = round((mp[17][12] * mp[17][4]), 2) #costo del vidrio templado con factura
                mp[17][14] = round((mp[17][12] * mp[17][5]), 2) #costo del vidrio templado con descuento
                vidrio = round(mp[17][13], 2)

            elif color == "Color":
                mp[22][11] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[22][12] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[22][13] = round((mp[22][12] * mp[22][4]), 2) #costo del vidrio templado con factura
                mp[22][14] = round((mp[22][12] * mp[22][5]), 2) #costo del vidrio templado con descuento
                vidrio = round(mp[22][13], 2)                

            mp[75][11] = round((cantidad * base * altura), 2)
            mp[75][12] = mp[75][11]
            mp[75][13] = round((mp[75][11] * mp[75][4]), 2)  #costo mano de obra con factura
            mp[75][14] = round((mp[75][11] * mp[75][5]), 2)  #costo mano de obra con descuento
            
            mp[38][11] = round((cantidad * 4), 2) # cantidad de Jaladores
            mp[38][13] = round((mp[38][4] * mp[38][11]), 2) #costo jaladores con factura
            mp[38][14] = round((mp[38][5] * mp[38][11]), 2) #costo jaladores con descuento
            
            mp[61][11] = round((cantidad * 3), 2) # cantidad de trincos
            mp[61][13] = round((mp[61][4] * mp[61][11]), 2) #costo trincos con factura
            mp[61][14] = round((mp[61][5] * mp[61][11]), 2) #costo trincos con descuento  
            
            mp[41][11] = round((cantidad * 4), 2) # cantidad de contra trinco
            mp[41][13] = round((mp[41][4] * mp[41][11]), 2) #costo de contra trinco con factura
            mp[41][14] = round((mp[41][5] * mp[41][11]), 2) #costo de contra trinco con descuento

            mp[43][11] = round((cantidad * 2), 2) # cantidad de zocalo inferior
            mp[43][13] = round((mp[43][4] * mp[43][11]), 2) #costo de zocalo inferior con factura
            mp[43][14] = round((mp[43][5] * mp[43][11]), 2) #costo de zocalo inferior con descuento

            mp[44][11] = round((cantidad * 2), 2) # cantidad de zocalo superior
            mp[44][13] = round((mp[44][4] * mp[44][11]), 2) #costo de zocalo superior con factura
            mp[44][14] = round((mp[44][5] * mp[44][11]), 2) #costo de zocalo superior con descuento

            mp[67][11] = round(cantidad, 2) # cantidad de chapas.
            mp[67][13] = round((mp[67][4] * mp[67][11]), 2) #costo de chapas con factura
            mp[67][14] = round((mp[67][5] * mp[67][11]), 2) #costo de chapas con descuento

            mp[69][11] = round(cantidad, 2) # cantidad de contrachapa
            mp[69][13] = round((mp[69][4] * mp[69][11]), 2) #costo de contrachapa con factura
            mp[69][14] = round((mp[69][5] * mp[69][11]), 2) #costo de contrachapa con descuento

            mp[62][11] = round((cantidad * 1), 2) # cantidad de casquillo para trinco
            mp[62][13] = round((mp[62][4] * mp[62][11]), 2) #costo de casquillo para trinco con factura
            mp[62][14] = round((mp[62][5] * mp[62][11]), 2) #costo de casquillo para trinco con descuento

            mp[53][11] = round(cantidad * 2, 2) # cantidad de contrachapa
            mp[53][13] = round((mp[53][4] * mp[53][11]), 2) #costo de contrachapa con factura
            mp[53][14] = round((mp[53][5] * mp[53][11]), 2) #costo de contrachapa con descuento

            mp[55][11] = round(cantidad * 2, 2) # cantidad de contrachapa
            mp[55][13] = round((mp[55][4] * mp[55][11]), 2) #costo de contrachapa con factura
            mp[55][14] = round((mp[55][5] * mp[55][11]), 2) #costo de contrachapa con descuento

            mp[60][11] = round(cantidad * 2, 2) # cantidad de contrachapa
            mp[60][13] = round((mp[60][4] * mp[60][11]), 2) #costo de contrachapa con factura
            mp[60][14] = round((mp[60][5] * mp[60][11]), 2) #costo de contrachapa con descuento

            mp[1][11] = round(((cantidad * ((2 * base) + (2 * altura) + ((nvertical-1) * altura))) / 6), 2) # cantidad de silicona normal
            mp[1][13] = round((mp[1][4] * mp[1][11]), 2) #costo silicona natural con factura
            mp[1][14] = round((mp[1][5] * mp[1][11]), 2) #costo silicona natural con descuento
            
            mp[3][11] = round(((cantidad * ((2 * base) + (2 * altura) + ((nvertical-1) * altura))) * 2 / 20), 2) # cantidad de cinta masking
            mp[3][13] = round((mp[3][4] * mp[3][11]), 2) #costo cinta masking con factura
            mp[3][14] = round((mp[3][5] * mp[3][11]), 2) #costo cinta masking con descuento  
            
            mp[5][11] = round((cantidad * ((2 * base) + (2 * altura)) / 6), 2) # cantidad de perfil U 15 x 25 incoloro o bronce
            mp[5][13] = round((mp[5][4] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con factura
            mp[5][14] = round((mp[5][5] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con descuento

            mp[14][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tornillo de 8 x 1 1/2
            mp[14][13] = round((mp[14][4] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con factura
            mp[14][14] = round((mp[14][5] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con descuento

            mp[13][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tarugos No. 6
            mp[13][13] = round((mp[13][4] * mp[13][11]), 2) #costo de tarugos No. 6 con factura
            mp[13][14] = round((mp[13][5] * mp[13][11]), 2) #costo de tarugos No. 6 con descuento

            if freno == "Con Freno":
                mp[37][11] = cantidad * 2 # cantidad de frenos
                mp[37][13] = round((mp[37][4] * mp[37][11]), 2) #costo de frenos con factura
                mp[37][14] = round((mp[37][5] * mp[37][11]), 2) #costo de frenos con descuento

            elif freno == "Sin Freno":
                mp[40][11] = cantidad * 2 # cantidad de pivote loco
                mp[40][13] = round((mp[40][4] * mp[40][11]), 2) #costo de pivote loco con factura
                mp[40][14] = round((mp[40][5] * mp[40][11]), 2) #costo de pivote loco con descuento

            accesorios = round((mp[37][13] + mp[38][13] + mp[40][13] + mp[61][13] + mp[43][13] + mp[44][13] + mp[67][13] + mp[69][13] + mp[41][13] + mp[62][13] + mp[53][13] + mp[55][13] + mp[60][13] + mp[1][13] + mp[3][13] + mp[5][13] + mp[14][13] + mp[13][13]), 2)
            
            messagebox.showinfo("cot", str(cantidad)+"  Frente(s) de Vidrio Templado tipo Spyder \n de  "+str(base)+"  Mt. de base   x  "+str(altura)+"  Mt. de altura ==> "+str(base * altura * cantidad)+ " Mt2. \n TOTAL COSTO PARCIAL  "+str(vidrio + mp[75][13] + accesorios)+" $us \n Costo de vidrio templado =  "+str(vidrio)+"  $us \n Costo de la mano de obra  =  "+str(mp[75][13])+" $us. \n Costo de accesorios  = "+str(accesorios)+"  $us. ")  

            if color == "Incoloro":
                mp[235][4] = cantidad 
                mp[235][5] = mp[75][11]
                mp[235][6] = mp[75][13]
                mp[235][7] = accesorios
                mp[235][8] = vidrio
                mp[235][9] = vidrio + accesorios + mp[75][13]

            elif color == "Color":
                mp[236][4] = cantidad 
                mp[236][5] = mp[75][11]
                mp[236][6] = mp[75][13]
                mp[236][7] = accesorios
                mp[236][8] = vidrio  
                mp[236][9] = vidrio + accesorios + mp[75][13] 

            for i in range(1, 237, 1):
                for j in range(11, 19, 1):
                    acum[i][j] += mp[i][j]
            
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    acum[i][j] += mp[i][j]

            self.ventana.destroy()
            application=opcion()
        else:
            messagebox.showinfo("NO", "ERROR algun dato ingresado no es correcto o no ingresaste algún dato")

class op14:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("380x740")
        self.ventana.title("Op1")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="PUERTA BATIENE \n 1 HOJA CON FIJOS LATERALES Y SUPERIOR", font=("Comic Sans", 14,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=15)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/op14a.png")
        self.img = self.img.resize((260,260))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand="True", fill="both", side="top", pady=0)

        self.label_base = Label(self.frame2, text="BASE en metros : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_base.grid(row=0, column=0, padx=5, pady=3, sticky="e")
        self.entry_base = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_base.grid(row=0, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.label_altura = Label(self.frame2, text="ALTURA en metros :",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_altura.grid(row=1, column=0, padx=5, pady=3, sticky="e")
        self.entry_altura = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_altura.grid(row=1, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_cantidad = Label(self.frame2, text="CANTIDAD : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_cantidad.grid(row=2, column=0, padx=5, pady=3, sticky="e")
        self.entry_cantidad = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_cantidad.grid(row=2, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_color = Label(self.frame2, text="VIDRIO INCOLORO ó COLOR  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_color.grid(row=4, column=0, padx=5, pady=3, sticky="e")
        self.color_v = StringVar()
        self.lista2 = ["Incoloro", "Color"]
        self.opciones2 = OptionMenu(self.frame2, self.color_v, *self.lista2)
        self.opciones2.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.color_v.set("???????")
        self.opciones2.grid(row=4, column=1, padx=5, pady=3, sticky="e")

        self.label_nvertical = Label(self.frame2, text="N DIV. VERTICALES : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_nvertical.grid(row=5, column=0, padx=5, pady=3, sticky="e")
        self.entry_nvertical = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_nvertical.grid(row=5, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_freno = Label(self.frame2, text="CON FRENO O SIN FRENO ?  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_freno.grid(row=6, column=0, padx=5, pady=3, sticky="e")
        self.freno = StringVar()
        self.lista4 = ["Con Freno", "Sin Freno"]
        self.opciones4 = OptionMenu(self.frame2, self.freno, *self.lista4)
        self.opciones4.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.freno.set("?????????")
        self.opciones4.grid(row=6, column=1, padx=5, pady=3, sticky="e")
        
        self.boton_cotizar = Button(self.frame2, text="COTIZAR Y SEGUIR", width=18, font=("Comic Sans", 11,"bold"), command=self.cotizar)
        self.boton_cotizar.grid(row=8, column=0, pady=15, columnspan=1, padx=25, sticky="w")

        self.boton_salir = Button(self.frame2, text="SALIR", width=18, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=8, column=1, pady=15, columnspan=1, padx=10, sticky="ew")

        mainloop()
    
    def salir(self):
        self.ventana.destroy()
        application=login()

    def cotizar(self):
        if len(self.entry_base.get()) != 0 and len(self.entry_altura.get()) != 0 and len(self.entry_cantidad.get()) != 0 and len(self.freno.get()) != 0 and len(self.color_v.get()) != 0 and len(self.entry_nvertical.get()) != 0:
            while True:
                try:
                    x = float(self.entry_base.get())
                    y = float(self.entry_altura.get())
                    break

                except ValueError:                
                    messagebox.showinfo("NO", "ERROR ....... La medida de la BASE ó ALTURA no son correctas, revise los doatos ingresados e introduzca nuevamente los valores .... RECUERDE LA SEPARACION DECIMAL ES CON PUNTO . ")
                    return(False)
                
            while True:
                try:
                    x = int(self.entry_cantidad.get())
                    y = int(self.entry_nvertical.get())
                    break

                except ValueError:

                    messagebox.showinfo("NO", "ERROR ....... La CANTIDAD O LAS DIVISIONES, no son correctas, revise los datos ingresados e introduzca nuevamente los valores correctos.... RECUERDE QUE DEBEN SER NUMEROS SIN DECIMALES")
                    return(False)
                
            while True:
                try:
                    y = str(self.color_v.get())
                    w = str(self.freno.get())
                    if y == "Incoloro" or y == "Color":
                        if w == "Con Freno" or w == "Sin Freno":
                            break
                        else:
                            return(False)
                    else:
                        return(False)

                except ValueError:
                    messagebox.showinfo("NO", "ERROR ....... El ESPESOR Y EL COLOR DEBEN SER SELECCIONADOS, revise si fueron seleccionados y seleccione la opcion deseada...")
                    return(False)
                
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            cantidad = int(self.entry_cantidad.get())
            color = self.color_v.get()
            nvertical = int(self.entry_nvertical.get())
            freno = self.freno.get()

            mp = inicia

            for i in range(0, 237, 1):
                for j in range(11, 19, 1):
                    mp[i][j] = 0.00
                                                            
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    mp[i][j] = 0.00

            mp[196][3] = acum[196][3]
            mp[197][3] = acum[197][3]
            mp[198][3] = acum[198][3]
            mp[199][3] = acum[199][3]
            mp[200][3] = acum[200][3]
            mp[201][3] = acum[201][3]
            mp[202][3] = acum[202][3]

            if color == "Incoloro":
                mp[17][11] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[17][12] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[17][13] = round((mp[17][12] * mp[17][4]), 2) #costo del vidrio templado con factura
                mp[17][14] = round((mp[17][12] * mp[17][5]), 2) #costo del vidrio templado con descuento
                vidrio = round(mp[17][13], 2)

            elif color == "Color":
                mp[22][11] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[22][12] = round((cantidad * base * altura), 2) # superficie en mt2
                mp[22][13] = round((mp[22][12] * mp[22][4]), 2) #costo del vidrio templado con factura
                mp[22][14] = round((mp[22][12] * mp[22][5]), 2) #costo del vidrio templado con descuento
                vidrio = round(mp[22][13], 2)                

            mp[75][11] = round((cantidad * base * altura), 2)
            mp[75][12] = mp[75][11]
            mp[75][13] = round((mp[75][11] * mp[75][4]), 2)  #costo mano de obra con factura
            mp[75][14] = round((mp[75][11] * mp[75][5]), 2)  #costo mano de obra con descuento
            
            mp[38][11] = round((cantidad * 2), 2) # cantidad de Jaladores
            mp[38][13] = round((mp[38][4] * mp[38][11]), 2) #costo jaladores con factura
            mp[38][14] = round((mp[38][5] * mp[38][11]), 2) #costo jaladores con descuento
            
            mp[61][11] = round((cantidad * 1), 2) # cantidad de picaportes herraje 1335
            mp[61][13] = round((mp[61][4] * mp[61][11]), 2) #costo picaportes herraje 1335 con factura
            mp[61][14] = round((mp[61][5] * mp[61][11]), 2) #costo picaportes herraje 1335 con descuento  
            
            mp[41][11] = round((cantidad * 2), 2) # cantidad de capuchino herraje 1038
            mp[41][13] = round((mp[41][4] * mp[41][11]), 2) #costo de capuchino herraje 1038 con factura
            mp[41][14] = round((mp[41][5] * mp[41][11]), 2) #costo de capuchino herraje 1038 con descuento

            mp[43][11] = round((cantidad * 1), 2) # cantidad de zocalo inferior herraje 1103
            mp[43][13] = round((mp[43][4] * mp[43][11]), 2) #costo de zocalo inferior herraje 1103 con factura
            mp[43][14] = round((mp[43][5] * mp[43][11]), 2) #costo de zocalo inferior herraje 1103 con descuento

            mp[44][11] = round((cantidad * 1), 2) # cantidad de zocalo superior herraje 1101
            mp[44][13] = round((mp[44][4] * mp[44][11]), 2) #costo de zocalo superior herraje 1101 con factura
            mp[44][14] = round((mp[44][5] * mp[44][11]), 2) #costo de zocalo superior herraje 1101 con descuento

            mp[67][11] = round(cantidad, 2) # cantidad de chapas herraje 1520
            mp[67][13] = round((mp[67][4] * mp[67][11]), 2) #costo de chapas herraje 1520 con factura
            mp[67][14] = round((mp[67][5] * mp[67][11]), 2) #costo de chapas herraje 1520 con descuento

            mp[69][11] = round(cantidad, 2) # cantidad de contrachapa herraje 1531
            mp[69][13] = round((mp[69][4] * mp[69][11]), 2) #costo de contrachapa herraje 1531 con factura
            mp[69][14] = round((mp[69][5] * mp[69][11]), 2) #costo de contrachapa herraje 1531 con descuento

            mp[62][11] = round((cantidad * 1), 2) # cantidad de contrapicaporte al vidrio herraje 1335c
            mp[62][13] = round((mp[62][4] * mp[62][11]), 2) #costo contrapicaporte al vidrio herraje 1335c con factura
            mp[62][14] = round((mp[62][5] * mp[62][11]), 2) #costo contrapicaporte al vidrio herraje 1335c con descuento

            mp[52][11] = round(cantidad * 1, 2) # cantidad de soporte al vidrio y al muro para puerta herraje 1203
            mp[52][13] = round((mp[52][4] * mp[52][11]), 2) #costo soporte al vidrio y al muro para puerta herraje 1203 con factura
            mp[52][14] = round((mp[52][5] * mp[52][11]), 2) #costo soporte al vidrio y al muro para puerta herraje 1203 con descuento

            mp[57][11] = round(cantidad * 1, 2) # cantidad de pistola herraje 1310
            mp[57][13] = round((mp[57][4] * mp[57][11]), 2) #costo de pistola herraje 1310 con factura
            mp[57][14] = round((mp[57][5] * mp[57][11]), 2) #costo de pistola herraje 1310 con descuento

            mp[55][11] = round(cantidad * 1, 2) # cantidad de soporte central herraje 1302
            mp[55][13] = round((mp[55][4] * mp[55][11]), 2) #costo de soporte central herraje 1302 con factura
            mp[55][14] = round((mp[55][5] * mp[55][11]), 2) #costo de soporte central herraje 1302 con descuento

            mp[60][11] = round(cantidad * 1, 2) # cantidad de soporte esquinero herraje 1329
            mp[60][13] = round((mp[60][4] * mp[60][11]), 2) #costo de soporte esquinero herraje 1329 con factura
            mp[60][14] = round((mp[60][5] * mp[60][11]), 2) #costo de soporte esquinero herraje 1329 con descuento

            mp[1][11] = round(((cantidad * ((2 * base) + (2 * altura) + ((nvertical-1) * altura))) / 6), 2) # cantidad de silicona normal
            mp[1][13] = round((mp[1][4] * mp[1][11]), 2) #costo silicona natural con factura
            mp[1][14] = round((mp[1][5] * mp[1][11]), 2) #costo silicona natural con descuento
            
            mp[3][11] = round(((cantidad * ((2 * base) + (2 * altura) + ((nvertical-1) * altura))) * 2 / 20), 2) # cantidad de cinta masking
            mp[3][13] = round((mp[3][4] * mp[3][11]), 2) #costo cinta masking con factura
            mp[3][14] = round((mp[3][5] * mp[3][11]), 2) #costo cinta masking con descuento  
            
            mp[5][11] = round((cantidad * ((2 * base) + (2 * altura)) / 6), 2) # cantidad de perfil U 15 x 25 incoloro o bronce
            mp[5][13] = round((mp[5][4] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con factura
            mp[5][14] = round((mp[5][5] * mp[5][11]), 2) #costo de perfil U 15 x 25 incoloro o bronce con descuento

            mp[14][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tornillo de 8 x 1 1/2
            mp[14][13] = round((mp[14][4] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con factura
            mp[14][14] = round((mp[14][5] * mp[14][11]), 2) #costo de tornillo de 8 x 1 1/2 con descuento

            mp[13][11] = round(((cantidad * ((2 * base) + (2 * altura))) / 0.4), 2) # cantidad de tarugos No. 6
            mp[13][13] = round((mp[13][4] * mp[13][11]), 2) #costo de tarugos No. 6 con factura
            mp[13][14] = round((mp[13][5] * mp[13][11]), 2) #costo de tarugos No. 6 con descuento

            if freno == "Con Freno":
                mp[37][11] = cantidad * 1 # cantidad de frenos
                mp[37][13] = round((mp[37][4] * mp[37][11]), 2) #costo de frenos con factura
                mp[37][14] = round((mp[37][5] * mp[37][11]), 2) #costo de frenos con descuento

            elif freno == "Sin Freno":
                mp[40][11] = cantidad * 1 # cantidad de pivote loco herraje 1013
                mp[40][13] = round((mp[40][4] * mp[40][11]), 2) #costo de pivote loco herraje 1013 con factura
                mp[40][14] = round((mp[40][5] * mp[40][11]), 2) #costo de pivote loco herraje 1013 con descuento

            accesorios = round((mp[37][13] + mp[38][13] + mp[40][13] + mp[61][13] + mp[43][13] + mp[44][13] + mp[67][13] + mp[69][13] + mp[41][13] + mp[62][13] + mp[52][13] + mp[57][13] + mp[55][13] + mp[60][13] + mp[1][13] + mp[3][13] + mp[5][13] + mp[14][13] + mp[13][13]), 2)
            
            messagebox.showinfo("cot", str(cantidad)+"  Frente(s) de Vidrio Templado tipo Spyder \n de  "+str(base)+"  Mt. de base   x  "+str(altura)+"  Mt. de altura ==> "+str(base * altura * cantidad)+ " Mt2. \n TOTAL COSTO PARCIAL  "+str(vidrio + mp[75][13] + accesorios)+" $us \n Costo de vidrio templado =  "+str(vidrio)+"  $us \n Costo de la mano de obra  =  "+str(mp[75][13])+" $us. \n Costo de accesorios  = "+str(accesorios)+"  $us. ")  

            if color == "Incoloro":
                mp[235][4] = cantidad 
                mp[235][5] = mp[75][11]
                mp[235][6] = mp[75][13]
                mp[235][7] = accesorios
                mp[235][8] = vidrio
                mp[235][9] = vidrio + accesorios + mp[75][13]

            elif color == "Color":
                mp[236][4] = cantidad 
                mp[236][5] = mp[75][11]
                mp[236][6] = mp[75][13]
                mp[236][7] = accesorios
                mp[236][8] = vidrio
                mp[236][9] = vidrio + accesorios + mp[75][13]  

            for i in range(1, 237, 1):
                for j in range(11, 19, 1):
                    acum[i][j] += mp[i][j]
            
            for i in range(203, 237, 1):
                for j in range(4, 10, 1):
                    acum[i][j] += mp[i][j] 
        
            self.ventana.destroy()
            application=opcion()
        else:
            messagebox.showinfo("NO", "ERROR algun dato ingresado no es correcto o no ingresaste algún dato")

login()


