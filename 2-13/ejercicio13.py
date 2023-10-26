from guizero import App, Box, Text, TextBox, PushButton

# Función para generar la secuencia
def generar_secuencia():
    try:
        cantidad = int(input_box.value)
        if cantidad > 0:
            secuencia = "".join(["0" if i % 2 == 0 else "1" for i in range(cantidad)])
            resultado.value = "Secuencia: " + secuencia
        else:
            resultado.value = "Por favor, ingrese un número positivo mayor que cero."
    except ValueError:
        resultado.value = "Por favor, ingrese un número válido."

# Crear una aplicación GUI
app = App("Generador de Secuencia 0/1", width=300, height=200)

# Crear una caja para organizar elementos
box = Box(app, layout="grid")

# Etiqueta para la cantidad de números
Text(box, text="Cantidad de números:", grid=[0, 0])

# Cuadro de texto para ingresar la cantidad
input_box = TextBox(box, grid=[1, 0])

# Botón para generar la secuencia
generar_button = PushButton(box, text="Generar Secuencia", command=generar_secuencia, grid=[0, 1, 2, 1])

# Etiqueta para mostrar la secuencia generada
resultado = Text(box, text="", grid=[0, 2, 2, 1])

# Iniciar la aplicación
app.display()