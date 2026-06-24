# Gestion de Datos de Paises en Python

Programa de consola que gestiona un dataset de paises (nombre, poblacion,
superficie y continente), permitiendo agregar, actualizar, buscar, filtrar,
ordenar y obtener estadisticas, con persistencia en un archivo CSV.

## Integrantes
- Facundo Emanuel Yramain (Comision 4)
- Noe Ezequiel Martinez (Comision 11)

## Requisitos
- Python 3
- No requiere librerias externas (usa unicamente el modulo `csv` de la
  libreria estandar)

## Estructura del proyecto
```
.
├── main.py        # Punto de entrada: menu principal e interaccion con el usuario
├── gestion.py      # Logica de negocio: alta, busqueda, filtros, orden y estadisticas
├── archivos.py     # Lectura y escritura del archivo CSV
└── paises.csv      # Dataset base (se carga al iniciar y se sobrescribe al salir)
```

## Como ejecutar
1. Clonar el repositorio o descargar los archivos.
2. Ubicarse en la carpeta del proyecto (todos los archivos estan en la raiz).
3. Ejecutar:
```
py main.py
```

## Formato del archivo `paises.csv`
El archivo usa coma como separador y la primera fila son los encabezados:

```
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
Japon,125800000,377975,Asia
```

| Campo       | Tipo   | Descripcion                             |
|-------------|--------|-----------------------------------------|
| nombre      | texto  | Nombre del pais                         |
| poblacion   | entero | Cantidad de habitantes                  |
| superficie  | entero | Superficie en km2                       |
| continente  | texto  | America, Europa, Asia, Africa u Oceania |

Si el archivo no existe al iniciar el programa, se crea uno vacio con los
encabezados correspondientes.

## Menu de opciones
Al ejecutar el programa se muestra el siguiente menu:

```
1. Agregar.
2. Actualizar.
3. Buscar.
4. Filtrar.
5. Ordenar.
6. Estadisticas.
7. Mostrar todos.
8. Guardar y salir.
```

### 1. Agregar
Solicita nombre, poblacion, superficie y continente, y agrega el pais a la
lista en memoria. Valida que poblacion y superficie sean numeros enteros
positivos; si se ingresa un valor no numerico, se informa el error y se
vuelve a pedir el dato.

### 2. Actualizar
Busca un pais por nombre y permite modificar sus datos. Si el pais no
existe, se informa por consola y se vuelve al menu.

### 3. Buscar
Permite buscar paises por coincidencia parcial del nombre (no hace falta
escribir el nombre completo ni respetar mayusculas/minusculas).

### 4. Filtrar
Permite filtrar el listado por continente, poblacion o superficie (minimo
y/o maximo).

### 5. Ordenar
Permite ordenar el listado por nombre, poblacion o superficie, en orden
ascendente o descendente, usando `sorted()` con `lambda` como clave.

### 6. Estadisticas
Muestra pais con mayor y menor poblacion, promedio de poblacion y
superficie, y cantidad de paises por continente.

### 7. Mostrar todos
Lista todos los paises cargados en formato de tabla.

### 8. Guardar y salir
Sobrescribe `paises.csv` con el estado actual de la lista en memoria y
cierra el programa. Si no se elige esta opcion, los cambios no se
persisten.

## Manejo de errores
El programa contempla, entre otros, los siguientes casos:
- Ingreso de texto no numerico en poblacion o superficie.
- Busqueda o actualizacion de un pais inexistente.
- Archivo `paises.csv` vacio o no encontrado al iniciar.

## Links del proyecto
- Repositorio en GitHub: https://github.com/011Xuca/UTN-TUPaD-Gestion-Paises
- Video demostrativo: ...
