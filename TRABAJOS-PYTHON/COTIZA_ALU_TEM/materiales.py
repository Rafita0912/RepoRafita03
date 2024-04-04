def materia_prima():
    materia = [["Código", "codigo de la empresa", "descripción del producto", "unidad de medida", "precio de venta", "precio de venta con descuento", "observaciones"], 
               ["mp1", "mp1", "materia prima basica 1", "mt. lin.", 3.45, 3.1, "observaciones"], 
               ["mp2", "mp2", "materia prima basica 2", "unidad(es)", 3.45, 3.1, "observaciones"]]
    return materia;
mp = materia_prima()
for mppv in mp:
    print(mppv[2], " = ", mppv[4], "$us x", mppv[3])
