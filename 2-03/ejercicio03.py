from guizero import App, Box, Text, PushButton, TextBox

# Función para calcular la edad
def calcular_edad():
    try:
        año_nacimiento = int(input_año_nacimiento.value)
        año_actual = int(input_año_actual.value)

        if año_nacimiento > año_actual:
            resultado_text.value = "El año de nacimiento no puede ser mayor al año actual"
        else:
            edad = año_actual - año_nacimiento
            resultado_text.value = f"Su edad es: {edad} años"
        resultado_text.show()  # Mostrar el resultado o mensaje de error
    except ValueError:
        resultado_text.value = "Ingrese años válidos"
        resultado_text.show()  # Mostrar el mensaje de error

# Crear la aplicación
app = App("Calculadora de Edad", width=300, height=180)

# Crear una caja para organizar los elementos de manera vertical
main_box = Box(app, layout="grid")

# Etiquetas y campos de entrada
año_nacimiento_label = Text(main_box, "Año de nacimiento:", grid=[0, 0])
input_año_nacimiento = TextBox(main_box, grid=[1, 0])
año_actual_label = Text(main_box, "Año actual:", grid=[0, 1])
input_año_actual = TextBox(main_box, grid=[1, 1])

# Botón para calcular la edad
calcular_button = PushButton(main_box, text="Calcular Edad", command=calcular_edad, grid=[0, 2, 2, 1])

# Etiqueta para mostrar el resultado
resultado_text = Text(main_box, "", grid=[0, 3, 2, 1], visible=False)

# Ejecutar la aplicación
app.display()