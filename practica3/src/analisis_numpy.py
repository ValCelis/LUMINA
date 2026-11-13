import numpy as np
import json
import time
import os
import argparse


def leer_csv(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        encabezados = archivo.readline().strip().split("|")
        datos = []

        for linea in archivo:
            fila = linea.rstrip("\n\r").split("|")
            datos.append(fila)

    return encabezados, datos


def limpiar_columna(encabezados, datos, nombre_columna):
    indice = encabezados.index(nombre_columna)
    valores = []

    for fila in datos:
        if indice >= len(fila):
            continue

        valor = fila[indice].strip()

        if valor == "":
            continue

        try:
            numero = float(valor)

            if np.isfinite(numero):
                valores.append(numero)

        except ValueError:
            continue

    return np.array(valores, dtype=np.float64)


def calcular_estadisticas(valores, columna):
    if valores.size == 0:
        raise ValueError(
            f"La columna {columna} no tiene valores válidos."
        )

    return {
        "columna": columna,
        "n_valores_validos": int(valores.size),
        "media": round(float(np.mean(valores)), 2),
        "desviacion_estandar": round(float(np.std(valores)), 2),
        "minimo": round(float(np.min(valores)), 2),
        "maximo": round(float(np.max(valores)), 2),
        "mediana": round(float(np.median(valores)), 2),
        "percentil_25": round(float(np.percentile(valores, 25)), 2),
        "percentil_75": round(float(np.percentile(valores, 75)), 2)
    }


def limites_k_sigma(valores, k=3):
    media = np.mean(valores)
    desviacion = np.std(valores)

    limite_inferior = media - k * desviacion
    limite_superior = media + k * desviacion

    return limite_inferior, limite_superior


def detectar_outliers(valores):
    if valores.size == 0:
        raise ValueError(
            "No hay valores válidos para detectar outliers."
        )

    limite_inferior, limite_superior = limites_k_sigma(valores, 3)

    mascara = (
        (valores < limite_inferior) |
        (valores > limite_superior)
    )

    outliers = valores[mascara]

    cantidad = int(outliers.size)
    porcentaje = (cantidad / valores.size) * 100

    if cantidad > 0:
        minimo = round(float(np.min(outliers)), 2)
        maximo = round(float(np.max(outliers)), 2)
    else:
        minimo = None
        maximo = None

    return {
        "metodo": "desviacion_estandar_3",
        "limite_inferior": round(float(limite_inferior), 2),
        "limite_superior": round(float(limite_superior), 2),
        "n_outliers": cantidad,
        "porcentaje": round(float(porcentaje), 2),
        "outliers_minimo": minimo,
        "outliers_maximo": maximo
    }



def benchmark(valores):
    if valores.size == 0:
        raise ValueError(
            "No hay valores válidos para realizar el benchmark."
        )

    lista = valores.tolist()
    n = len(lista)
    repeticiones = 10

    # Comprobar equivalencia antes de medir los tiempos
    suma = 0.0

    for valor in lista:
        suma += valor

    media_python = suma / n

    suma_cuadrados = 0.0

    for valor in lista:
        suma_cuadrados += (valor - media_python) ** 2

    desviacion_python = (suma_cuadrados / n) ** 0.5

    media_numpy = np.mean(valores)
    desviacion_numpy = np.std(valores)

    coinciden = np.allclose(
        [media_python, desviacion_python],
        [media_numpy, desviacion_numpy]
    )

    if not coinciden:
        raise ValueError(
            "Los resultados de Python y NumPy no coinciden."
        )

    # Medir Python puro
    inicio_python = time.perf_counter()

    for _ in range(repeticiones):
        suma = 0.0

        for valor in lista:
            suma += valor

        media = suma / n

        suma_cuadrados = 0.0

        for valor in lista:
            suma_cuadrados += (valor - media) ** 2

        desviacion = (suma_cuadrados / n) ** 0.5

    tiempo_python = (
        time.perf_counter() - inicio_python
    ) / repeticiones

    # Medir NumPy
    inicio_numpy = time.perf_counter()

    for _ in range(repeticiones):
        media = np.mean(valores)
        desviacion = np.std(valores)

    tiempo_numpy = (
        time.perf_counter() - inicio_numpy
    ) / repeticiones

    if tiempo_numpy > 0:
        factor = round(
            float(tiempo_python / tiempo_numpy), 2
        )
    else:
        factor = None

    return {
        "n_filas": int(n),
        "tiempo_bucle_python_seg": round(
            float(tiempo_python), 6
        ),
        "tiempo_numpy_seg": round(
            float(tiempo_numpy), 6
        ),
        "factor_velocidad": factor,
        "operacion_medida": "calcular media y desviacion estandar"
    }


def guardar_json(resultado, ruta):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(
            resultado,
            archivo,
            indent=4,
            ensure_ascii=False,
            allow_nan=False
        )


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--pareja", required=True)
    parser.add_argument("--seed", required=True, type=int)

    args = parser.parse_args()

    columnas = [
        "tiempo_espera_min",
        "edad_paciente"
    ]

    # Obtener la carpeta raíz del proyecto
    ruta_base = os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    )

    # Ruta del archivo CSV
    nombre_archivo = "citas_medicas-ruido_100000.csv"

    ruta_csv = os.path.join(
        ruta_base,
        "datos",
        nombre_archivo
    )

    if not os.path.exists(ruta_csv):
        raise FileNotFoundError(
            f"No se encontró el archivo {ruta_csv}"
        )

    # Leer el archivo
    encabezados, datos = leer_csv(ruta_csv)

    resultados = []
    resultados_outliers = []
    valores_columnas = []

    # Analizar las dos columnas numéricas
    for columna in columnas:

        if columna not in encabezados:
            raise ValueError(
                f"No se encontró la columna {columna}"
            )

        valores = limpiar_columna(
            encabezados,
            datos,
            columna
        )

        estadisticas = calcular_estadisticas(
            valores,
            columna
        )

        outliers = detectar_outliers(valores)

        resultados.append(estadisticas)
        resultados_outliers.append(outliers)
        valores_columnas.append(valores)

    # Benchmark sobre la primera columna numérica
    resultado_benchmark = benchmark(valores_columnas[0])

    # Construir el resultado final
    resultado_final = {
        "archivo": nombre_archivo,
        "pareja": args.pareja,
        "seed": args.seed,
        "numerica_1": resultados[0],
        "numerica_2": resultados[1],
        "outliers_numerica_1": resultados_outliers[0],
        "outliers_numerica_2": resultados_outliers[1],
        "benchmark": resultado_benchmark
    }

    # Guardar JSON
    ruta_json = os.path.join(
        ruta_base,
        "practica3",
        "resultados",
        "analisis_numpy.json"
    )

    guardar_json(resultado_final, ruta_json)

    print("Análisis terminado correctamente.")
    print(f"Archivo generado: {ruta_json}")

    print("\nValores válidos:")

    for resultado in resultados:
        print(
            resultado["columna"],
            resultado["n_valores_validos"]
        )

    print("\nBenchmark:")
    print("Los resultados de Python y NumPy coinciden.")
    print(
    "Factor de velocidad:",
    resultado_benchmark["factor_velocidad"]
)
    
if __name__ == "__main__":
    main()
