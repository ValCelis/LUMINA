archivo = open("datos/citas_medicas-ruido_100000.csv", "r")
encabezado = archivo.readline()
columnas = encabezado.strip().split("|")
indice_especialidad = columnas.index("especialidad")
indice_tiempo_espera = columnas.index("tiempo_espera_min")

contador = 0
filas = 0

primeras_filas=[]

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
        primeras_filas.append(datos)
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

valores_unicos= len(conteo_especialidad)

print("Valores válidos:", len(valores_numericos))
print("Mínimo:", min(valores_numericos))
print("Máximo:", max(valores_numericos))
print("Celdas vacías totales:", vacios_totales)
print("Celdas vacías por columna:", vacios_por_columna)
print("Errores numéricos:", errores_numericos)



with open("practica1/resultados/resumen.txt", "w") as salida:
    salida.write("RESUMEN DE LA PRACTICA\n")
    salida.write("Archivo: citas_medicas-ruido_100000.csv\n")
    salida.write("Pareja: Valeria Celis y Mariana Carrillo\n")
    salida.write("Seed: 100000\n")

    salida.write("\nDimensiones\n")
    salida.write(f"Filas: {filas}\n")
    salida.write(f"Columnas: {len(columnas)}\n")
    salida.write(f"Nombres de columnas: {', '.join(columnas)}\n")

    salida.write("\nPrimeras 5 filas\n")
    salida.write(" | ".join(columnas) + "\n")

    for fila in primeras_filas:
        salida.write(" | ".join(fila) + "\n")

    salida.write("\nColumna categórica: especialidad\n")
    salida.write(f"Valores únicos: {valores_unicos}\n")
    salida.write(f"Valor más frecuente: {especialidad_mas_frecuente} ({mayor_cantidad} apariciones)\n")

    salida.write("\nColumna numérica: tiempo_espera_min\n")
    salida.write(f"Valores válidos (no vacíos): {len(valores_numericos)}\n")
    salida.write(f"Mínimo: {min(valores_numericos)}\n")
    salida.write(f"Máximo: {max(valores_numericos)}\n")

    salida.write("\nCalidad de datos\n")
    salida.write(f"Celdas vacías totales: {vacios_totales}\n")
    salida.write("Celdas vacías por columna:\n")

    for i in range(len(columnas)):
        salida.write(f"  {columnas[i]}: {vacios_por_columna[i]}\n")

print("Resumen terminado")
