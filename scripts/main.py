import archivos
import gestion

# Ruta del archivo donde se guardan los datos de los paises
ARCHIVO_CSV = "datos/paises.csv"

# Carga los paises al iniciar el programa
paises = archivos.cargar_paises(ARCHIVO_CSV)

print("\n" +"-" * 58 + f"\nSe cargaron {len(paises)} paises.")

# Pide un texto al usuario y valida que no este vacio
def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        
        if texto:
            return texto
        
        print("Error: el campo no puede estar vacio.")

# Pide un numero entero al usuario y valida que sea valido y no negativo
def leer_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            
            if valor >= 0:
                return valor
            
            print("Error: no puede ser negativo.")
        except ValueError:
            print("Error: debe ingresar un número entero.")

# Muestra una lista de paises en formato de tabla
def mostrar_paises(paises):
    if not paises:
        print("No hay paises para mostrar.\n")
        return
    
    ancho_nombre = max(len(p["nombre"]) for p in paises)
    ancho_nombre = max(ancho_nombre, len("Nombre"))
    
    ancho_poblacion = max(len(str(p["poblacion"])) for p in paises)
    ancho_poblacion = max(ancho_poblacion, len("Poblacion"))
    
    ancho_superficie = max(len(str(p["superficie"])) for p in paises)
    ancho_superficie = max(ancho_superficie, len("Superficie"))
    
    ancho_continente = max(len(p["continente"]) for p in paises)
    ancho_continente = max(ancho_continente, len("Continente"))
    
    separador = "+-" + "-" * ancho_nombre + "-+-" + "-" * ancho_poblacion + "-+-" + "-" * ancho_superficie + "-+-" + "-" * ancho_continente + "-+"
    
    print("LISTADO DE PAISES".center(len(separador) + 2, "-"))
    
    print(" " + separador)
    print(f" | {'Nombre':^{ancho_nombre}} | {'Poblacion':^{ancho_poblacion}} | {'Superficie':^{ancho_superficie}} | {'Continente':^{ancho_continente}} |")
    print(" " + separador)
    
    for p in paises:
        print(f" | {p['nombre'].title():^{ancho_nombre}} | {p['poblacion']:>{ancho_poblacion}} | {p['superficie']:>{ancho_superficie}} | {p['continente'].title():^{ancho_continente}} |")
    
    print(" " + separador)

# Submenu para elegir y aplicar un filtro
def menu_filtrar(paises):
    print("1) Continente  2) Poblacion  3) Superficie")
    op = input("Filtrar por: ").strip()
    if op == "1":
        return gestion.filtrar_por_continente(paises, leer_texto("Continente: "))
    if op == "2":
        return gestion.filtrar_por_poblacion(paises, leer_entero("Minimo: "), leer_entero("Maximo: "))
    if op == "3":
        return gestion.filtrar_por_superficie(paises, leer_entero("Minimo: "), leer_entero("Maximo: "))
    print("Opcion invalida.")
    return []

# Submenu para elegir criterio y orden (asc/desc)
def menu_ordenar(paises):
    print("1) Nombre  2) Poblacion  3) Superficie")
    op = input("Ordenar por: ")
    
    desc = input("¿Descendente? (s/n): ").strip().lower() == "s"
    if op == "1":
        return gestion.ordenar_por_nombre(paises, desc)
    if op == "2":
        return gestion.ordenar_por_poblacion(paises, desc)
    if op == "3":
        return gestion.ordenar_por_superficie(paises, desc)
    
    print("Opcion invalida.")
    return []

# Muestra las estadisticas calculadas en pantalla
def mostrar_estadisticas(paises):
    estadisticas = gestion.calcular_estadisticas(paises)
    
    if not estadisticas:
        print("No hay datos cargados.\n")
        return
    
    print(f"Mayor poblacion: {estadisticas['mayor_poblacion']['nombre'].title()} ({estadisticas['mayor_poblacion']['poblacion']})")
    print(f"Menor poblacion: {estadisticas['menor_poblacion']['nombre'].title()} ({estadisticas['menor_poblacion']['poblacion']})")
    print(f"Promedio poblacion: {estadisticas['promedio_poblacion']:.2f}")
    print(f"Promedio superficie: {estadisticas['promedio_superficie']:.2f}")
    print("Paises por continente:")
    
    for continente, cantidad in estadisticas["por_continente"].items():
        print(f" - {continente.title()}: {cantidad}")

# Bucle principal del programa: muestra el menu y procesa la opcion elegida
while True:
    print("MENU DE GESTION DE PAISES".center(58, "-"))
    print("""
                    1. Agregar.
                    2. Actualizar.
                    3. Buscar.
                    4. Filtrar.
                    5. Ordenar.
                    6. Estadisticas.
                    7. Mostrar todos.
                    8. Guardar y salir.""")
    print("-" * 58)
    op = input("Opcion: ")
    print("-" * 58)
    if op == "1":
        try:
            gestion.agregar_pais(paises, leer_texto("Nombre: "), leer_entero("Poblacion: "), leer_entero("Superficie: "), leer_texto("Continente: "))
            print("Pais agregado.\n")
        except ValueError as error:
            print(f"Error al querer registrar el pais: {error}\n")
            
    elif op == "2":
        nombre = leer_texto("Nombre del pais: ")
        
        if gestion.actualizar_pais(paises, nombre, leer_entero("Nueva poblacion: "), leer_entero("Nueva superficie: ")):
            print("Actualizado correctamente.\n")
        else:
            print("Pais no encontrado.\n")
            
    elif op == "3":
        mostrar_paises(gestion.buscar_pais(paises, leer_texto("Buscar: ")))
        print("-" * 58)
    elif op == "4":
        mostrar_paises(menu_filtrar(paises))
        print("-" * 58)
    elif op == "5":
        mostrar_paises(menu_ordenar(paises))
        print("-" * 58)
    elif op == "6":
        mostrar_estadisticas(paises)
        print("-" * 58)
    elif op == "7":
        mostrar_paises(paises)
    elif op == "8":
        if archivos.guardar_paises(ARCHIVO_CSV, paises):
            print("Datos guardados. ¡Hasta luego!")
        break
    else:
        print("Opcion invalida.\n")