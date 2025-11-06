# • Crea un sistema para gestionar un inventario de productos. Debe cumplir con lo 
# siguiente: 
# • Clase Producto con atributos: codigo, nombre, precio, cantidad. 
# • Usted tiene un vector de productos.  
# • Implemente los métodos por medio de un menú.  
# o agregar_producto(producto) 
# o eliminar_producto(codigo) 
# o buscar_producto(codigo) 
# o valor_total() (suma de precio * cantidad de todos los productos).

class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"Código: {self.codigo} | Nombre: {self.nombre} | Precio: {self.precio} | Cantidad: {self.cantidad}"

productos = []

def agregar_producto():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    producto = Producto(codigo, nombre, precio, cantidad)
    productos.append(producto)
    print(f"\nProducto '{nombre}' agregado correctamente.\n")

def eliminar_producto():
    codigo = input("Ingrese el código del producto a eliminar: ")
    for producto in productos:
        if producto.codigo == codigo:
            productos.remove(producto)
            print(f"\nProducto '{producto.nombre}' eliminado correctamente.\n")
            return
    print("\nNo se encontró un producto con ese código.\n")

def buscar_producto():
    codigo = input("Ingrese el código del producto a buscar: ")
    for producto in productos:
        if producto.codigo == codigo:
            print("\nProducto encontrado:")
            print(producto)
            return
    print("\nProducto no encontrado.\n")

def valor_total():
    total = sum(p.precio * p.cantidad for p in productos)
    print(f"\nValor total del inventario: {total}\n")

while True:

    menu = int(input("Bienvenido al Sistema para gestionar un inventario de productos \n"
                     "1. Agregar Producto\n"
                     "2. Eliminar Producto\n"
                     "3. Buscar Producto\n"
                     "4. Valor total de Productos \n"
                     "5. Salir \n"
                     "Seleccione una opcion: "))
    
    match menu:
        case 1:
            agregar_producto()
        case 2:
            eliminar_producto()
        case 3:
            buscar_producto()
        case 4:
            valor_total()
        case 5:
            print("Saliendo del Sistema...")
            break
        case __:
            print("Opción incorrecta, seleccione nuevamente.")