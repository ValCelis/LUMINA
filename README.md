# LUMINA

> **SEMILLA: 21**

En este repositorio haremos las practicas para programación para ciencia de datos

PONLE EL NOMBRE DE TU EQUIPO AQUI PARA QUE YO SEPA CUAL TEMA TE TOCO

EQUIPO:14-LUMINA

Integrantes: 
Carrillo Perez Mariana.
Dominguez Celis Aketzalli Valeria.

TEMA: Citas Medicas

Observaciones Repositorio:
1- No tiene requirements.txt
2- No tiene la carpeta datos/ 
3- No tiene las carpetas practica1 a practica6
4- No tiene la carpeta proyecto/

Listo ya estan los archivos requeridos.


---

## Observaciones del profesor

### Práctica 2 — evaluación (27-oct-2026)

**Calificación: 90 / 100**

Entregada el **26-oct-2026 a las 20:48**, dentro del plazo (la entrega cerraba el lun 26-oct), así que no lleva penalización por retraso.

**Lo que destaca:** 13 funciones y el cálculo correcto en **todos** los campos: los números coinciden con la referencia sin una sola diferencia. Lo único que los separó del 100 fueron los nombres.

**Criterios cubiertos al 100 %:** Requisitos de Git (3+ commits, rama integrada); Requisitos de código (5 funciones, `lambda`, `map`/`filter`); Encabezado del JSON: archivo, pareja, seed; `valores_unicos_categorica`; `conteo_por_categoria`; `categoria_mas_frecuente`; `top_3_categorias`; `promedio_por_categoria`; `filtrado` (percentil 90).

**Observaciones:**

1. El script se llama `analisis2.py` y debe llamarse **`analisis_python.py`**. El enunciado pide los nombres literales y lo advertía justo porque en P1 dos equipos perdieron puntos por esto.
2. Dentro de `estadisticas_numerica_1` y `estadisticas_numerica_2` nombraron los campos `n_validos`, `min` y `max`; el enunciado los pide como **`n_valores_validos`**, **`minimo`** y **`maximo`**. Los valores son correctos —coinciden exacto con la referencia—, así que esos campos se contaron a mitad de punto: lo que falló es el nombre del campo, no el cálculo. Conviene corregirlo porque de P3 en adelante la revisión del JSON es automática y busca esos nombres.

**Desglose:**

| Criterio | Obtenido | Máximo |
|---|:---:|:---:|
| Nombres exactos de los entregables | 5 | 10 |
| Requisitos de Git (3+ commits, rama integrada) | 8 | 8 |
| Requisitos de código (5 funciones, `lambda`, `map`/`filter`) | 12 | 12 |
| Encabezado del JSON: archivo, pareja, seed | 6 | 6 |
| `valores_unicos_categorica` | 10 | 10 |
| `conteo_por_categoria` | 10 | 10 |
| `categoria_mas_frecuente` | 6 | 6 |
| `top_3_categorias` | 8 | 8 |
| `estadisticas_numerica_1` (con mediana) | 9 | 12 |
| `estadisticas_numerica_2` (con mediana) | 6 | 8 |
| `promedio_por_categoria` | 6 | 6 |
| `filtrado` (percentil 90) | 4 | 4 |
| **Total** | **90** | **100** |

### 13-oct-2026 — Correcciones de la Práctica 1

**Calificación de P1: 81 → 90 / 100.**

**Corrigieron sus tres observaciones y además la nota opcional** (commit del 12-oct). Son el
único equipo del grupo que atendió también lo que era solo una sugerencia:

1. Ya abre con `=== RESUMEN DEL DATASET ===`.
2. Ya están los cinco encabezados de sección: `--- Dimensiones ---`,
   `--- Primeras 5 filas ---`, `--- Columna categórica: ... ---`,
   `--- Columna numérica: ... ---` y `--- Calidad de datos ---`.
3. La semilla ya dice **21**.
4. Aplicaron el `.strip()` que se les sugirió sin que contara para la calificación: ahora
   reportan 21 valores únicos y `Pediatria` con 13724, idéntico a la solución de referencia.

Su `resumen.txt` quedó alineado con la referencia en todos los campos. Lo único que sobra es
una línea `Errores numéricos: 0` que no está en el formato pedido; quítenla para que la
salida sea exactamente la del enunciado.

**Cómo se aplicó el reconocimiento.** Nueve de los diez equipos que tenían observaciones las atendieron entre el 8 y el 12 de octubre. A quien corrigió y tenía 90 o más, su práctica queda en **99**; a quien tenía menos de 90, en **90**. El 100 se reserva para quien entregó bien desde la primera vez. En la tabla de calificaciones del curso su celda aparece como `anterior/vigente`: el primer número es la entrega original y **el segundo es el que cuenta**.

### Práctica 1 — evaluación (8-oct-2026, 00:51 h)

**Calificación: 81 / 100**

Entregada el **3-oct-2026 a las 22:39**, dentro del plazo (la entrega cerraba el mar 6-oct), así que no lleva penalización por retraso.

**Criterios cubiertos al 100%:** Estructura del monorepo (6/6); Nombres exactos de los entregables; Requisitos de Git (3+ commits, rama mergeada); Python puro (sin `csv` ni `pandas`, lectura con `open`); Dimensiones: filas, columnas, nombres; Columna categórica (nombre, únicos, más frecuente); Columna numérica_1 (nombre, válidos, mín, máx); Calidad de datos (celdas vacías).

**Observaciones:**

1. Falta la línea de encabezado `=== RESUMEN DEL DATASET ===` con la que debe abrir el archivo.
2. Faltan los encabezados de sección del formato pedido: `--- Dimensiones ---`, `--- Primeras 5 filas ---`, `--- Columna categórica: ... ---`, `--- Columna numérica: ... ---`, `--- Calidad de datos ---`. El contenido puede estar, pero las secciones deben ir delimitadas tal como las muestra el enunciado.
3. La semilla reportada es incorrecta: pusieron `Seed: 100000` y su semilla es **21**.
4. Nota, **sin efecto en la calificación**: en la columna categórica no aplicaron `.strip()` al valor antes de contarlo, así que las variantes con espacios sobrantes cuentan como categorías distintas y reportan 28 valores únicos en lugar de 21. El enunciado no pedía ese `.strip()`, así que su lectura es válida y no se descontó nada. Tómenlo en cuenta de aquí en adelante: en P4 y P5 van a limpiar justo este tipo de ruido.
5. Vimos que el 7-oct a las 17:34 corrigieron la semilla en el `resumen.txt` (de `100000` a `21`). Se los reconocemos, pero la calificación de arriba corresponde a la entrega que estaba dentro del plazo, que es la que se califica. Tomar la versión corregida implicaría contarla como entrega del 7-oct, un día después del cierre, y con la penalización por retraso el resultado sería **menor** que el que tienen. Por eso se queda la calificación de la entrega original.

**Desglose:**

| Criterio | Obtenido | Máximo |
|---|:---:|:---:|
| Estructura del monorepo (6/6) | 8 | 8 |
| Nombres exactos de los entregables | 10 | 10 |
| Requisitos de Git (3+ commits, rama mergeada) | 10 | 10 |
| Python puro (sin `csv` ni `pandas`, lectura con `open`) | 8 | 8 |
| Formato del `resumen.txt` (encabezado y secciones) | 0 | 9 |
| Encabezado: Archivo, Pareja, Seed | 5 | 10 |
| Dimensiones: filas, columnas, nombres | 10 | 10 |
| Primeras 5 filas (separadas con barra y espacios) | 0 | 5 |
| Columna categórica (nombre, únicos, más frecuente) | 12 | 12 |
| Columna numérica_1 (nombre, válidos, mín, máx) | 13 | 13 |
| Calidad de datos (celdas vacías) | 5 | 5 |
| **Total** | **81** | **100** |

### 26-sep-2026

**Estatus:** 6/6 de la estructura esperada.

Siguen con la estructura completa, sin pendientes.

### 23-sep-2026

**Estatus:** 6/6 de la estructura esperada.

¡Felicidades, completaron toda la estructura! Terminaron `resultados/` en `practica3` a `practica6` y agregaron `src/` a `proyecto/`. Ya les dejamos su dataset (`citas_medicas-ruido_100.csv` y `_100000.csv`) dentro de `datos/`.

📖 **Práctica 1 ya está disponible.** La encontrarán en `labs/P1/P1_setup_reconocimiento.md`, dentro del repositorio del profesor: https://github.com/ESCOMLCD/pcd202701/blob/main/labs/P1/P1_setup_reconocimiento.md — léanla completa antes de empezar a programar, ahí está todo lo que deben hacer, el formato exacto de `resumen.txt` y la fecha de entrega (mar 6-oct).

### 22-sep-2026

**Estatus:** 4/6 de la estructura esperada.

Agregaron la carpeta `datos/`, bien. Les falta: en `practica1` a `practica6` crear la carpeta `resultados/` (ya tienen `src/`); y en `proyecto/` crear la carpeta `src/` (ya tienen `resultados/` y `datos/`).

### SEMILLA21
**CITAS MEDICAS.**
Holaa, practica 1 terminada.

Practica1 corregida

### 26 / 10 / 2026
**PRACTICA2 TERMINADA**
SEMILLA21
**CITAS MÉDICAS**
