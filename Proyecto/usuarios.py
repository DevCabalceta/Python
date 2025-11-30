import tkinter as tk
from tkinter import messagebox, ttk

# ==============================
#   CLASE USUARIO
# ==============================
class Usuario:
    def __init__(self, codigo, nombre, correo, rol):
        self.codigo = codigo
        self.nombre = nombre
        self.correo = correo
        self.rol = rol

# =========================================
#   CLASE SISTEMA PARA GESTIONAR USUARIOS
# =========================================
class SistemaUsuarios:
    def __init__(self):
        self.usuarios = []  # Lista interna para almacenar usuarios

    # Crear usuario
    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    # Editar usuario según índice
    def editar_usuario(self, index, usuario_editado):
        self.usuarios[index] = usuario_editado

    # Eliminar usuario por índice
    def eliminar_usuario(self, index):
        del self.usuarios[index]

    # Obtener todos los usuarios
    def obtener_usuarios(self):
        return self.usuarios

# ============================
#   VENTANA PRINCIPAL TKINTER
# ============================
app = tk.Tk()
app.title("Mantenimiento de Usuarios")
app.geometry("900x600")

# Sistema
sistema = SistemaUsuarios()

# ===============================
#   TITULO
# ===============================
titulo = tk.Label(app, text="Mantenimiento de Usuarios", font=("Arial", 20, "bold"))
titulo.pack(pady=10)

# ===============================
#   FORMULARIO DE USUARIO
# ===============================
frame_form = tk.Frame(app)
frame_form.pack(pady=10)

# Etiquetas + Entradas
tk.Label(frame_form, text="Código:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
tk.Label(frame_form, text="Nombre:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
tk.Label(frame_form, text="Correo:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5)
tk.Label(frame_form, text="Rol:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5)

input_codigo = tk.Entry(frame_form, font=("Arial", 12))
input_nombre = tk.Entry(frame_form, font=("Arial", 12))
input_correo = tk.Entry(frame_form, font=("Arial", 12))

input_codigo.grid(row=0, column=1, padx=10)
input_nombre.grid(row=1, column=1, padx=10)
input_correo.grid(row=2, column=1, padx=10)

# ComboBox para rol
roles = ["administrador", "digitador", "contabilidad"]
input_rol = ttk.Combobox(frame_form, values=roles, state="readonly", font=("Arial", 12))
input_rol.grid(row=3, column=1, padx=10)

# Índice de edición (-1 indica que NO se está editando)
indice_edicion = -1

# ===============================
#   FUNCIONES DEL CRUD
# ===============================
def validar_campos():
    """Verifica que ningún campo esté vacío."""
    if (not input_codigo.get().strip() or 
        not input_nombre.get().strip() or
        not input_correo.get().strip() or
        not input_rol.get().strip()):
        return False
    return True

def limpiar_inputs():
    """Limpia los campos del formulario."""
    input_codigo.delete(0, tk.END)
    input_nombre.delete(0, tk.END)
    input_correo.delete(0, tk.END)
    input_rol.set("")

def crear_usuario():
    """Crea un nuevo usuario y lo agrega a la tabla."""
    global indice_edicion

    if not validar_campos():
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return
    
    nuevo = Usuario(
        input_codigo.get(),
        input_nombre.get(),
        input_correo.get(),
        input_rol.get()
    )

    # Si NO es edición, agrega uno nuevo
    if indice_edicion == -1:
        sistema.agregar_usuario(nuevo)
        messagebox.showinfo("Éxito", "Usuario agregado correctamente")
    else:
        # Si estamos editando
        sistema.editar_usuario(indice_edicion, nuevo)
        indice_edicion = -1
        boton_guardar.config(text="Crear Usuario")
        messagebox.showinfo("Éxito", "Usuario editado correctamente")

    actualizar_tabla()
    limpiar_inputs()


def cargar_datos_edicion():
    """Carga en los inputs el usuario seleccionado para editar."""
    global indice_edicion
    seleccion = tabla.focus()

    if not seleccion:
        messagebox.showwarning("Advertencia", "Seleccione un usuario de la tabla")
        return

    indice_edicion = int(tabla.item(seleccion)['text'])

    usuario = sistema.obtener_usuarios()[indice_edicion]

    # Cargar en los campos
    input_codigo.delete(0, tk.END)
    input_codigo.insert(0, usuario.codigo)

    input_nombre.delete(0, tk.END)
    input_nombre.insert(0, usuario.nombre)

    input_correo.delete(0, tk.END)
    input_correo.insert(0, usuario.correo)

    input_rol.set(usuario.rol)

    boton_guardar.config(text="Guardar Cambios")

def eliminar_usuario():
    """Elimina un usuario de la tabla."""
    seleccion = tabla.focus()

    if not seleccion:
        messagebox.showwarning("Advertencia", "Seleccione un usuario de la tabla")
        return

    indice = int(tabla.item(seleccion)['text'])

    confirm = messagebox.askyesno("Confirmación", "¿Desea eliminar este usuario?")
    if confirm:
        sistema.eliminar_usuario(indice)
        actualizar_tabla()
        messagebox.showinfo("Eliminado", "Usuario eliminado correctamente")

# ===============================
#   TABLA DE USUARIOS 
# ===============================
frame_tabla = tk.Frame(app)
frame_tabla.pack(pady=10)

tabla = ttk.Treeview(frame_tabla, columns=("Codigo", "Nombre", "Correo", "Rol"), show="headings")
tabla.pack()

tabla.heading("Codigo", text="Código")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Correo", text="Correo")
tabla.heading("Rol", text="Rol")

tabla.column("Codigo", width=100)
tabla.column("Nombre", width=200)
tabla.column("Correo", width=200)
tabla.column("Rol", width=150)

def actualizar_tabla():
    """Refresca la tabla de usuarios."""
    # Limpiar tabla
    for fila in tabla.get_children():
        tabla.delete(fila)

    # Insertar datos actualizados
    for index, usuario in enumerate(sistema.obtener_usuarios()):
        tabla.insert("", "end", text=index, values=(usuario.codigo, usuario.nombre, usuario.correo, usuario.rol))

# ===============================
#   BOTONES CRUD
# ===============================
frame_botones = tk.Frame(app)
frame_botones.pack(pady=20)

boton_guardar = tk.Button(frame_botones, text="Crear Usuario", font=("Arial", 12), width=15, command=crear_usuario)
boton_guardar.grid(row=0, column=0, padx=10)

boton_editar = tk.Button(frame_botones, text="Editar", font=("Arial", 12), width=15, command=cargar_datos_edicion)
boton_editar.grid(row=0, column=1, padx=10)

boton_eliminar = tk.Button(frame_botones, text="Eliminar", font=("Arial", 12), width=15, command=eliminar_usuario)
boton_eliminar.grid(row=0, column=2, padx=10)

# ===============================
#   MAIN LOOP
# ===============================
app.mainloop()
