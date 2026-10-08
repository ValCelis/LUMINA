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
### 22-sep-2026

**Estatus:** 4/6 de la estructura esperada.

Agregaron la carpeta `datos/`, bien. Les falta: en `practica1` a `practica6` crear la carpeta `resultados/` (ya tienen `src/`); y en `proyecto/` crear la carpeta `src/` (ya tienen `resultados/` y `datos/`).

### 23-sep-2026

**Estatus:** 6/6 de la estructura esperada.

¡Felicidades, completaron toda la estructura! Terminaron `resultados/` en `practica3` a `practica6` y agregaron `src/` a `proyecto/`. Ya les dejamos su dataset (`citas_medicas-ruido_100.csv` y `_100000.csv`) dentro de `datos/`.

📖 **Práctica 1 ya está disponible.** La encontrarán en `labs/P1/P1_setup_reconocimiento.md`, dentro del repositorio del profesor: https://github.com/ESCOMLCD/pcd202701/blob/main/labs/P1/P1_setup_reconocimiento.md — léanla completa antes de empezar a programar, ahí está todo lo que deben hacer, el formato exacto de `resumen.txt` y la fecha de entrega (mar 6-oct).

### 26-sep-2026

**Estatus:** 6/6 de la estructura esperada.

Siguen con la estructura completa, sin pendientes.


### SEMILLA21
**CITAS MEDICAS.**
Holaa, practica 1 terminada.
