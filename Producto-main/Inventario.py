# Sistema de Inventario Mejorado
# Guarda los productos en inventario.txt
# Carga los productos al iniciar
# Maneja errores con try-except

# Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio


# Diccionario {ID: Producto}
productos = {}


# ===============================
# CARGAR INVENTARIO DESDE ARCHIVO
# ===============================
try:
    with open("inventario.txt", "r") as archivo:
        for linea in archivo:
            try:
                id, nombre, cantidad, precio = linea.strip().split(",")
                productos[id] = Producto(id, nombre, int(cantidad), float(precio))
            except ValueError:
                print("Línea dañada encontrada y omitida.")
    print("Inventario cargado correctamente.")
except FileNotFoundError:
    print("No existe inventario.txt. Se creará automáticamente.")
    open("inventario.txt", "w").close()
except Exception as e:
    print("Error al cargar el archivo:", e)


# ===============================
# FUNCIÓN PARA GUARDAR EN ARCHIVO
# ===============================
def guardar_en_archivo():
    try:
        with open("inventario.txt", "w") as archivo:
            for p in productos.values():
                archivo.write(f"{p.id},{p.nombre},{p.cantidad},{p.precio}\n")
        print("Inventario guardado correctamente.")
    except PermissionError:
        print("Error: No tienes permisos para escribir en el archivo.")
    except Exception as e:
        print("Error inesperado:", e)


# ===============================
# MENÚ PRINCIPAL
# ===============================
while True:
    print("\n1. Agregar")
    print("2. Mostrar")
    print("3. Eliminar")
    print("4. Salir")

    opcion = input("Opción: ")

    # AGREGAR
    if opcion == "1":
        id = input("ID: ")
        nombre = input("Nombre: ")

        try:
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
        except ValueError:
            print("Error: Debes ingresar números válidos.")
            continue

        if id in productos:
            print("El ID ya existe.")
        else:
            productos[id] = Producto(id, nombre, cantidad, precio)
            guardar_en_archivo()
            print("Producto agregado correctamente.")

    # MOSTRAR
    elif opcion == "2":
        if not productos:
            print("Inventario vacío.")
        else:
            for p in productos.values():
                print(p.id, p.nombre, p.cantidad, p.precio)

    # ELIMINAR
    elif opcion == "3":
        id = input("ID a eliminar: ")
        if id in productos:
            del productos[id]
            guardar_en_archivo()
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    # SALIR
    elif opcion == "4":
        print("Fin del programa.")
        break

    else:
        print("Opción incorrecta.")
