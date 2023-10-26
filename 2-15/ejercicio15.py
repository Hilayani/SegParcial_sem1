#La tienda "Branko" debe vender productos a n alumnos, ofrecen: tortas, tacos, hotdogs y pizzas. 
#Imprime los productos vendidos en total.

from guizero import App, Box, Text, TextBox, PushButton

# Variables globales
cantidad_personas = 0
productos_vendidos = {
    "Torta": 0,
    "Tacos": 0,
    "Hotdogs": 0,
    "Pizza": 0
}
contador_comidas = 0

# Función para registrar y contar los productos vendidos
def registrar_venta():
    global contador_comidas
    comida = comida_box.value
    
    if comida in productos_vendidos:
        productos_vendidos[comida] += 1
        contador_comidas += 1
        resultado.value = f"Se ha vendido {contador_comidas} comida(s) en total.\n\nProductos vendidos:\n"
        for producto, cantidad in productos_vendidos.items():
            resultado.value += f"{producto}: {cantidad}\n"
        comida_box.clear()
    else:
        resultado.value = "Por favor, ingrese un producto válido (Torta, Tacos, Hotdogs o Pizza)."

# Función para preguntar la cantidad de personas a las que se venderá
def pedir_cantidad_personas():
    global cantidad_personas
    cantidad_personas = int(cantidad_personas_box.value)
    cantidad_personas_box.disable()
    resultado.value = "Ingrese el producto vendido, (Torta, Tacos, Hotdogs o Pizza)"

# Crear una aplicación GUI
app = App("Registro de Ventas en Tienda 'Branko'", width=300, height=300)

# Crear una caja para organizar elementos
box = Box(app, layout="grid")

# Etiqueta para ingresar la cantidad de personas
Text(box, text="Cantidad de personas a las que se les venderá:", grid=[0, 0])

# Cuadro de texto para ingresar la cantidad de personas
cantidad_personas_box = TextBox(box, grid=[1, 0])

# Botón para aceptar la cantidad de personas
cantidad_personas_button = PushButton(box, text="Aceptar", command=pedir_cantidad_personas, grid=[2, 0])

# Etiqueta para ingresar el producto vendido
Text(box, text="", grid=[0, 1])

# Cuadro de texto para ingresar el producto vendido
comida_box = TextBox(box, grid=[1, 1])

# Botón para registrar la venta
registrar_button = PushButton(box, text="Registrar Venta", command=registrar_venta, grid=[2, 1])

# Etiqueta para mostrar el resultado
resultado = Text(box, text="", grid=[0, 2, 3, 1])

# Iniciar la aplicación
app.display()