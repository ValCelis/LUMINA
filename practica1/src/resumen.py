archivo = open("datos/citas_medicas-ruido_100.csv", "r")
encabezado = archivo.readline()
columnas = encabezado.strip().split("|")
contador=0
filas=0

conteo_especialidad ={}
valores_numericos=[]
vacios_por_columna = [0, 0, 0, 0, 0, 0, 0, 0, 0]
vacios_totales = 0

for linea in archivo:
    datos = linea.strip().split("|")
    filas +=1

    for i in range(len(datos)):
        if datos[i].strip() == "":
            vacios_por_columna[i] += 1
            vacios_totales += 1
    
    especialidad=datos[0]
    if especialidad !="":
        if especialidad in conteo_especialidad:
            conteo_especialidad[especialidad] += 1
        else:
            conteo_especialidad[especialidad] = 1
        tiempo_espera = datos[3]

    if tiempo_espera != "":
        valor = float(tiempo_espera)
        valores_numericos.append(valor)

    if contador < 5:
        print (datos)
        contador += 1

print("Filas:",filas)
print("columnas:",len (columnas))
print ("conteo especialidad:",conteo_especialidad)

especialidad_mas_frecuente = ""
mayor_cantidad = 0

for especialidad in conteo_especialidad:
    if conteo_especialidad[especialidad] > mayor_cantidad:
        mayor_cantidad = conteo_especialidad[especialidad]
        especialidad_mas_frecuente = especialidad

print("Valores únicos:", len(conteo_especialidad))
print("Valor más frecuente:", especialidad_mas_frecuente)
print("Apariciones:", mayor_cantidad)
print("Valores validos:", len(valores_numericos))
print("Mínimo:", min(valores_numericos))
print("Máximo:", max(valores_numericos))
print("Celdas vacías totales:", vacios_totales)
print("Celdas vacías por columna:", vacios_por_columna)
