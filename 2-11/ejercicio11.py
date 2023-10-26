from guizero import App, Box, Text, TextBox, PushButton

# Variables globales
contador = 0
suma = 0

# Función para pedir un número entre 5 y 10, inclusive
def pedir_numero():
    global contador, suma
    numero = input_box.value
    try:
        numero = int(numero)
        if 5 <= numero <= 10:
            suma += numero
            contador += 1
            input_box.clear()
            if contador < 5:
                resultado.value = f"Llevamos {contador} número(s) capturado(s)."
            else:
                resultado.value = f"La suma de los 5 números es: {suma}"
                input_box.disable()
                pedir_button.disable()
        else:
            resultado.value = "Por favor, ingrese un número entre 5 y 10, inclusive."
    except ValueError:
        resultado.value = "Por favor, ingrese un número válido."

# Crear una aplicación GUI
app = App("Suma de Números entre 5 y 10", width=300, height=200)

# Crear una caja para organizar elementos
box = Box(app, layout="grid")

# Etiqueta y cuadro de texto para ingresar un número
Text(box, text="Ingrese un número entre 5 y 10, inclusive:", grid=[0, 0])
input_box = TextBox(box, grid=[1, 0])

# Botón para pedir el número
pedir_button = PushButton(box, text="Pedir Número", command=pedir_numero, grid=[0, 1, 2, 1])

# Etiqueta para mostrar el resultado
resultado = Text(box, text="", grid=[0, 2, 2, 1])

# Iniciar la aplicación
app.display()