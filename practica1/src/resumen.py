archivo = open("datos/citas_medicas-ruido_100000.csv", "r")
encabezado = archivo.readline()
columnas = encabezado.strip().split("|")
indice_especialidad = columnas.index("especialidad")
indice_tiempo_espera = columnas.index("tiempo_espera_min")

contador = 0
filas = 0
conteo_especialidad = {}
valores_numericos = []
vacios_por_columna = [0] * len(columnas)
vacios_totales = 0
errores_numericos = 0

for linea in archivo:
    datos = linea.strip().split("|")
    filas += 1
    for i in range(len(datos)):
        if datos[i].strip() == "":
            vacios_por_columna[i] += 1
            vacios_totales += 1

    especialidad = datos[indice_especialidad]
    if especialidad != "":
        if especialidad in conteo_especialidad:
            conteo_especialidad[especialidad] += 1
        else:
            conteo_especialidad[especialidad] = 1

    tiempo_espera = datos[indice_tiempo_espera]
    if tiempo_espera != "":
        try:
            valor = float(tiempo_espera)
            valores_numericos.append(valor)
        except ValueError:
            errores_numericos += 1

    if contador < 5:
        print(datos)
        contador += 1

print("Filas:", filas)
print("Columnas:", len(columnas))
print("Nombres de columnas:", columnas)

especialidad_mas_frecuente = ""
mayor_cantidad = 0

for especialidad in conteo_especialidad:
    if conteo_especialidad[especialidad] > mayor_cantidad:
        mayor_cantidad = conteo_especialidad[especialidad]
        especialidad_mas_frecuente = especialidad

print("Valores únicos:", len(conteo_especialidad))
print("Valor más frecuente:", especialidad_mas_frecuente)
print("Apariciones:", mayor_cantidad)
print("Valores válidos:", len(valores_numericos))
print("Mínimo:", min(valores_numericos))
print("Máximo:", max(valores_numericos))
print("Celdas vacías totales:", vacios_totales)
print("Celdas vacías por columna:", vacios_por_columna)
print("Errores numéricos:", errores_numericos)
