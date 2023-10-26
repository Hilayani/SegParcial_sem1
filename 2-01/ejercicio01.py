from guizero import App, Box, Text, PushButton, TextBox

# Función para calcular el promedio
def calcular_promedio():
    try:
        num1 = float(input_numero1.value)
        num2 = float(input_numero2.value)
        num3 = float(input_numero3.value)

        promedio = (num1 + num2 + num3) / 3

        resultado_text.value = f"El promedio es: {promedio:.2f}"
    except ValueError:
        resultado_text.value = "Ingrese números válidos"

# Crear la aplicación
app = App("Calculadora de Promedio", width=300, height=200)

# Crear una caja para organizar los elementos
main_box = Box(app, layout="grid")

# Etiquetas y campos de entrada
numero1_label = Text(main_box, "Número 1:", grid=[0, 0])
input_numero1 = TextBox(main_box, grid=[1, 0])
numero2_label = Text(main_box, "Número 2:", grid=[0, 1])
input_numero2 = TextBox(main_box, grid=[1, 1])
numero3_label = Text(main_box, "Número 3:", grid=[0, 2])
input_numero3 = TextBox(main_box, grid=[1, 2])

# Botón para calcular el promedio
calcular_button = PushButton(main_box, text="Calcular Promedio", command=calcular_promedio, grid=[0, 3, 2, 1])

# Etiqueta para mostrar el resultado
resultado_text = Text(main_box, "", grid=[0, 4, 2, 1])

# Ejecutar la aplicación
app.display()