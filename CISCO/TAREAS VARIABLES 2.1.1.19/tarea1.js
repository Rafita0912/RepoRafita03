let precioRosa=8;
let cantidadRosas=70;
let precioLirio=10;
let cantidadLirios=50;
let precioTulipan=2;
let cantidadTulipanes=120;
let precioTotalRosas=precioRosa*cantidadRosas;
let precioTotalLirios=precioLirio*cantidadLirios;
let precioTotalTulipanes=precioTulipan*cantidadTulipanes;
let totalFlores=precioTotalRosas+precioTotalLirios+precioTotalTulipanes
console.log("Rosa :  Precio Unitario : ",precioRosa,"  Cantidad : ",cantidadRosas,"  Valor : ",precioTotalRosas);
console.log("Lirio :  Precio Unitario : ",precioLirio,"  Cantidad : ",cantidadLirios,"  Valor : ",precioTotalLirios);
console.log("Tulipan :  Precio Unitario : ",precioTulipan,"  Cantidad : ",cantidadTulipanes,"  Valor : ",precioTotalTulipanes);
console.log("Total : ",totalFlores);