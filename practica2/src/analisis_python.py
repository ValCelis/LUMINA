
import json
import os

RUTA_ENTRADA = "datos/citas_medicas-ruido_100000.csv"
RUTA_SALIDA = "practica2/resultados/analisis_python.json"

NOMBRE_ARCHIVO = "citas_medicas-ruido_100000.csv"
PAREJA = "Valeria Celis y Mariana Carrillo"
SEED = 21

COLUMNA_CATEGORICA = "especialidad"
COLUMNA_NUMERICA_1 = "tiempo_espera_min"
COLUMNA_NUMERICA_2 = "edad_paciente"


def a_float(texto):
    try:
        return float(texto)
    except (ValueError, TypeError):
        return None


def es_convertible(texto):
    return a_float(texto) is not None


def leer_datos(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        encabezado = archivo.readline().rstrip("\r\n")
        columnas = [columna.strip() for columna in encabezado.split("|")]
        datos = []

        for linea in archivo:
            linea = linea.rstrip("\r\n")

            if linea == "":
                continue

            valores = linea.split("|")

            if len(valores) < len(columnas):
                valores.extend([""] * (len(columnas) - len(valores)))

            fila = dict(zip(columnas, valores[:len(columnas)]))
            fila = {
                columna: valor.strip()
                for columna, valor in fila.items()
            }

            datos.append(fila)

    return columnas, datos


def valores_unicos(datos, columna):
    valores = set()

    for fila in datos:
        valor = fila.get(columna, "").strip()

        if valor != "":
            valores.add(valor)

    return sorted(valores)


def conteo_por_categoria(datos, columna):
    conteo = {}

    for fila in datos:
        valor = fila.get(columna, "").strip()

        if valor != "":
            if valor in conteo:
                conteo[valor] += 1
            else:
                conteo[valor] = 1

    return conteo


def top_3_categorias(conteo):
    ordenadas = sorted(
        conteo.items(),
        key=lambda par: (-par[1], par[0])
    )

    return [
        {"valor": valor, "conteo": cantidad}
        for valor, cantidad in ordenadas[:3]
    ]


def obtener_numeros(datos, columna):
    textos = [fila.get(columna, "").strip() for fila in datos]
    textos_validos = list(filter(es_convertible, textos))
    numeros = list(map(a_float, textos_validos))

    return numeros


def mediana(numeros):
    if len(numeros) == 0:
        return None

    ordenados = sorted(numeros)
    n = len(ordenados)
    medio = n // 2

    if n % 2 == 1:
        resultado = ordenados[medio]
    else:
        resultado = (
            ordenados[medio - 1] + ordenados[medio]
        ) / 2

    return round(resultado, 2)


def estadisticas(datos, columna):
    numeros = obtener_numeros(datos, columna)

    if len(numeros) == 0:
        minimo = None
        maximo = None
        promedio = None
        valor_mediana = None
    else:
        minimo = min(numeros)
        maximo = max(numeros)
        promedio = round(sum(numeros) / len(numeros), 2)
        valor_mediana = mediana(numeros)

    return {
        "columna": columna,
        "n_valores_validos": len(numeros),
        "minimo": minimo,
        "maximo": maximo,
        "promedio": promedio,
        "mediana": valor_mediana
    }


def promedio_por_categoria(datos, categorica, numerica):
    grupos = {}

    for fila in datos:
        categoria = fila.get(categorica, "").strip()
        numero = a_float(fila.get(numerica, "").strip())

        if categoria != "" and numero is not None:
            if categoria not in grupos:
                grupos[categoria] = []

            grupos[categoria].append(numero)

    promedios = {}

    for categoria, numeros in grupos.items():
        promedios[categoria] = round(
            sum(numeros) / len(numeros), 2
        )

    return promedios


def percentil(numeros, p):
    if len(numeros) == 0:
        return None

    ordenados = sorted(numeros)
    indice = int(p * len(ordenados))

    if indice >= len(ordenados):
        indice = len(ordenados) - 1

    return ordenados[indice]


def analizar_filtrado(datos, columna):
    numeros = obtener_numeros(datos, columna)
    umbral = percentil(numeros, 0.9)

    if umbral is None:
        return {
            "condicion": f"{columna} > None",
            "umbral_usado": None,
            "n_registros_que_cumplen": 0,
            "porcentaje": 0.0
        }

    cumplen = list(filter(lambda numero: numero > umbral, numeros))
    cantidad = len(cumplen)

    porcentaje = round(
        (cantidad / len(numeros)) * 100, 2
    ) if len(numeros) > 0 else 0.0

    return {
        "condicion": f"{columna} > {umbral}",
        "umbral_usado": umbral,
        "n_registros_que_cumplen": cantidad,
        "porcentaje": porcentaje
    }


def main():
    columnas, datos = leer_datos(RUTA_ENTRADA)

    columnas_necesarias = [
        COLUMNA_CATEGORICA,
        COLUMNA_NUMERICA_1,
        COLUMNA_NUMERICA_2
    ]

    for columna in columnas_necesarias:
        if columna not in columnas:
            raise ValueError(
                f"No se encontro la columna requerida: {columna}"
            )

    unicos = valores_unicos(datos, COLUMNA_CATEGORICA)
    conteo = conteo_por_categoria(datos, COLUMNA_CATEGORICA)

    if conteo:
        categoria_frecuente = sorted(
            conteo.items(),
            key=lambda par: (-par[1], par[0])
        )[0]

        mas_frecuente = {
            "valor": categoria_frecuente[0],
            "conteo": categoria_frecuente[1]
        }
    else:
        mas_frecuente = {
            "valor": None,
            "conteo": 0
        }

    resultado = {
        "archivo": NOMBRE_ARCHIVO,
        "pareja": PAREJA,
        "seed": SEED,
        "valores_unicos_categorica": {
            "columna": COLUMNA_CATEGORICA,
            "n_valores_unicos": len(unicos),
            "valores": unicos
        },
        "conteo_por_categoria": conteo,
        "categoria_mas_frecuente": mas_frecuente,
        "top_3_categorias": top_3_categorias(conteo),
        "estadisticas_numerica_1": estadisticas(
            datos, COLUMNA_NUMERICA_1
        ),
        "estadisticas_numerica_2": estadisticas(
            datos, COLUMNA_NUMERICA_2
        ),
        "promedio_por_categoria": promedio_por_categoria(
            datos,
            COLUMNA_CATEGORICA,
            COLUMNA_NUMERICA_1
        ),
        "filtrado": analizar_filtrado(
            datos, COLUMNA_NUMERICA_1
        )
    }

    os.makedirs(os.path.dirname(RUTA_SALIDA), exist_ok=True)

    with open(RUTA_SALIDA, "w", encoding="utf-8") as archivo:
        json.dump(
            resultado,
            archivo,
            indent=2,
            ensure_ascii=False
        )

    print("Analisis terminado correctamente.")
    print("Filas analizadas:", len(datos))
    print("Columnas encontradas:", len(columnas))
    print("Archivo generado:", RUTA_SALIDA)


if __name__ == "__main__":
    main()
