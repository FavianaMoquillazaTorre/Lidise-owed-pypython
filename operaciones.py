inputtext1 = Element("inputtext1")
inputtext2 = Element("inputtext2")
salidasuma = Element("salidasuma")
salidaresta = Element("salidaresta")
salidamultiplicacion = Element("salidamultiplicacion")
salidadivision = Element("salidadivision")

def clear(*args, **kwargs):
    inputtext1.clear()
    inputtext2.clear()
    salidasuma.clear()
    salidaresta.clear()
    salidamultiplicacion.clear()
    salidadivision.clear()

def Calcular(*args, **kwargs):
    totalsuma = int(inputtext1.value) + int(inputtext2.value)
    salidasuma.write(totalsuma)
    
    totalresta = int(inputtext1.value) - int(inputtext2.value)
    salidaresta.write(totalresta)
    totalmultiplicacion = int(inputtext1.value) * int(inputtext2.value)
    salidamultiplicacion.write(totalmultiplicacion)
    totaldivision = int(inputtext1.value) / int(inputtext2.value)
    salidadivision.write(totaldivision)