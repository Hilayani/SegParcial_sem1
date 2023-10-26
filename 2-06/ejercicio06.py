from guizero import App, Box, Text, TextBox, PushButton

# Función para calcular el cuadrado del número
def calcular_cuadrado():
    try:
        numero = float(input_numero.value)
        if numero >= 0:
            cuadrado = numero ** 2
            resultado.value = f"El cuadrado de {numero} es {cuadrado}"
        else:
            resultado.value = "Por favor, ingrese un número positivo."
    except ValueError:
        resultado.value = "Por favor, ingrese un número válido."

# Crear una aplicación GUI
app = App("Calculadora de Cuadrado", width=300, height=150)

# Crear una caja para organizar los elementos
main_box = Box(app, layout="grid")

# Etiqueta y cuadro de texto para ingresar el número
numero_label = Text(main_box, "Ingrese un número positivo:", grid=[0, 0])
input_numero = TextBox(main_box, grid=[1, 0])

# Botón para calcular el cuadrado
calcular_button = PushButton(main_box, text="Calcular Cuadrado", command=calcular_cuadrado, grid=[0, 1, 2, 1])

# Etiqueta para mostrar el resultado
resultado = Text(main_box, "", grid=[0, 2, 2, 1])

# Ejecutar la aplicación
app.display()