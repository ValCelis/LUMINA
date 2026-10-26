
import os

# Archivo que vamos a analizar
ruta_entrada = "datos/citas_medicas-ruido_100000.csv"

# Archivo donde guardaremos los resultados
ruta_salida = "practica2/resultados/resumen.txt"

archivo = open(ruta_entrada, "r", encoding="utf-8")

encabezado = archivo.readline()
columnas = encabezado.rstrip("\n").split("|")

indice_especialidad = columnas.index("especialidad")
indice_tiempo_espera = columnas.index("tiempo_espera_min")

filas = 0
primeras_filas = []

conteo_especialidad = {}
tiempos = []

vacios_por_columna = [0] * len(columnas)
vacios_totales = 0

# Leer el archivo línea por línea
for linea in archivo:
    datos = linea.rstrip("\n").split("|")
    filas += 1

    # Guardar las primeras cinco filas
    if len(primeras_filas) < 5:
        primeras_filas.append(datos)

    # Contar celdas vacías
    for i in range(len(columnas)):
        if i >= len(datos) or datos[i].strip() == "":
            vacios_por_columna[i] += 1
            vacios_totales += 1

    # Contar las especialidades
    if indice_especialidad < len(datos):
        especialidad = datos[indice_especialidad].strip()

        if especialidad != "":
            if especialidad in conteo_especialidad:
                conteo_especialidad[especialidad] += 1
            else:
                conteo_especialidad[especialidad] = 1

    # Guardar los tiempos de espera como texto
    if indice_tiempo_espera < len(datos):
        tiempos.append(datos[indice_tiempo_espera].strip())
    else:
        tiempos.append("")

archivo.close()


# Verificar si un texto representa un número válido
def es_numero(valor):
    if valor == "":
        return False

    try:
        float(valor)
        return True
    except ValueError:
        return False


# FILTER: conservar solamente los tiempos numéricos válidos
tiempos_validos = list(filter(es_numero, tiempos))

# MAP: convertir los textos válidos a números decimales
valores_numericos = list(map(lambda x: float(x), tiempos_validos))

# LAMBDA: obtener los tiempos mayores o iguales a cero
tiempos_no_negativos = list(
    filter(lambda x: x >= 0, valores_numericos)
)

# Contar errores numéricos no vacíos
errores_numericos = 0

for tiempo in tiempos:
    if tiempo != "" and not es_numero(tiempo):
        errores_numericos += 1


# Encontrar la especialidad más frecuente
especialidad_mas_frecuente = ""
mayor_cantidad = 0

for especialidad in conteo_especialidad:
    if conteo_especialidad[especialidad] > mayor_cantidad:
        mayor_cantidad = conteo_especialidad[especialidad]
        especialidad_mas_frecuente = especialidad


# Mostrar resultados en la terminal
print("=== RESUMEN DEL DATASET ===")
print("Filas:", filas)
print("Columnas:", len(columnas))
print("Nombres de columnas:", columnas)

print("\n--- Especialidad ---")
print("Valores únicos:", len(conteo_especialidad))
print("Valor más frecuente:", especialidad_mas_frecuente)
print("Apariciones:", mayor_cantidad)

print("\n--- Tiempo de espera ---")
print("Valores numéricos válidos:", len(valores_numericos))
print("Tiempos mayores o iguales a cero:", len(tiempos_no_negativos))

if valores_numericos:
    print("Mínimo:", min(valores_numericos))
    print("Máximo:", max(valores_numericos))

print("\n--- Calidad de datos ---")
print("Celdas vacías totales:", vacios_totales)
print("Celdas vacías por columna:", vacios_por_columna)
print("Errores numéricos:", errores_numericos)


# Crear la carpeta de resultados si no existe
os.makedirs("practica2/resultados", exist_ok=True)

# Escribir los resultados en el archivo TXT
with open(ruta_salida, "w", encoding="utf-8") as salida:

    salida.write("=== RESUMEN DEL DATASET ===\n")
    salida.write("Archivo: " + ruta_entrada + "\n")

    salida.write("\n--- Dimensiones ---\n")
    salida.write(f"Filas: {filas}\n")
    salida.write(f"Columnas: {len(columnas)}\n")
    salida.write(f"Nombres de columnas: {', '.join(columnas)}\n")

    salida.write("\n--- Primeras 5 filas ---\n")
    salida.write(" | ".join(columnas) + "\n")

    for fila in primeras_filas:
        salida.write(" | ".join(fila) + "\n")

    salida.write("\n--- Especialidad ---\n")
    salida.write(f"Valores únicos: {len(conteo_especialidad)}\n")
    salida.write(
        f"Valor más frecuente: {especialidad_mas_frecuente} "
        f"({mayor_cantidad} apariciones)\n"
    )

    salida.write("\n--- Tiempo de espera ---\n")
    salida.write(f"Valores numéricos válidos: {len(valores_numericos)}\n")
    salida.write(
        f"Tiempos mayores o iguales a cero: {len(tiempos_no_negativos)}\n"
    )

    if valores_numericos:
        salida.write(f"Mínimo: {min(valores_numericos)}\n")
        salida.write(f"Máximo: {max(valores_numericos)}\n")

    salida.write("\n--- Calidad de datos ---\n")
    salida.write(f"Celdas vacías totales: {vacios_totales}\n")
    salida.write(f"Errores numéricos: {errores_numericos}\n")
    salida.write("Celdas vacías por columna:\n")

    for i in range(len(columnas)):
        salida.write(
            f"  {columnas[i]}: {vacios_por_columna[i]}\n"
        )

print("\nResumen terminado.")
print("Resultados guardados en:", ruta_salida)
