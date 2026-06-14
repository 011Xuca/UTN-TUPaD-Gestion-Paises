import archivos
import gestion

ARCHIVO_CSV = "datos/paises.csv"

paises = archivos.cargar_paises(ARCHIVO_CSV)
print(f"Se cargaron {len(paises)} paises.\n")

def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        
        if texto:
            return texto
        
        print("Error: el campo no puede estar vacio.")

def leer_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            
            if valor >= 0:
                return valor
            
            print("Error: no puede ser negativo.")
        except ValueError:
            print("Error: debe ingresar un número entero.")

def mostrar_paises(paises):
    if not paises:
        print("No hay paises para mostrar.\n")
        return
    
    print(f"\n{'Nombre'} | {'Poblacion'} | {'Superficie'} | {'Continente'}")
    
    for p in paises:
        print(f"{p['nombre']} |{p['poblacion']} | {p['superficie']} | {p['continente']}")

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

def mostrar_estadisticas(paises):
    estadisticas = gestion.calcular_estadisticas(paises)
    
    if not estadisticas:
        print("No hay datos cargados.\n")
        return
    
    print(f"Mayor poblacion: {estadisticas['mayor_poblacion']['nombre']} ({estadisticas['mayor_poblacion']['poblacion']})")
    print(f"Menor poblacion: {estadisticas['menor_poblacion']['nombre']} ({estadisticas['menor_poblacion']['poblacion']})")
    print(f"Promedio poblacion: {estadisticas['promedio_poblacion']:.2f}")
    print(f"Promedio superficie: {estadisticas['promedio_superficie']:.2f}")
    print("Paises por continente:")
    
    for continente, cantidad in estadisticas["por_continente"].items():
        print(f"  {continente}: {cantidad}")

while True:
    print("1) Agregar  2) Actualizar  3) Buscar  4) Filtrar 5) Ordenar  6) Estadisticas  7) Mostrar todos  8) Guardar y salir")
    
    op = input("Opcion: ")
    if op == "1":
        gestion.agregar_pais(paises, leer_texto("Nombre: "), leer_entero("Poblacion: "), leer_entero("Superficie: "), leer_texto("Continente: "))
        print("Pais agregado.\n")
    elif op == "2":
        nombre = leer_texto("Nombre del pais: ")
        
        if gestion.actualizar_pais(paises, nombre, leer_entero("Nueva poblacion: "), leer_entero("Nueva superficie: ")):
            print("Actualizado correctamente.\n")
        else:
            print("Pais no encontrado.\n")
            
    elif op == "3":
        mostrar_paises(gestion.buscar_pais(paises, leer_texto("Buscar: ")))
    elif op == "4":
        mostrar_paises(menu_filtrar(paises))
    elif op == "5":
        mostrar_paises(menu_ordenar(paises))
    elif op == "6":
        mostrar_estadisticas(paises)
    elif op == "7":
        mostrar_paises(paises)
    elif op == "8":
        if archivos.guardar_paises(ARCHIVO_CSV, paises):
            print("Datos guardados. ¡Hasta luego!")
        break
    else:
        print("Opcion invalida.\n")