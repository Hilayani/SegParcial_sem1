from guizero import App, Box, Text, TextBox, PushButton

# Función para calcular la edad
def calcular_edad():
    try:
        anio_nacimiento = int(input_box.value)
        anio_actual = 2023  # Puedes reemplazar esto con el año actual
        if anio_nacimiento > 0 and anio_nacimiento <= anio_actual:
            edad = anio_actual - anio_nacimiento
            resultado.value = f"Usted va a cumplir {edad + 1} años este año."
        else:
            resultado.value = "Por favor, ingrese un año de nacimiento válido."
    except ValueError:
        resultado.value = "Por favor, ingrese un año de nacimiento válido."

# Crear una aplicación GUI
app = App("Calculadora de Edad", width=300, height=200)

# Crear una caja para organizar elementos
box = Box(app, layout="grid")

# Etiqueta y cuadro de texto para ingresar el año de nacimiento
Text(box, text="Ingrese su año de nacimiento:", grid=[0, 0])
input_box = TextBox(box, grid=[1, 0])

# Botón para calcular la edad
calcular_button = PushButton(box, text="Calcular Edad", command=calcular_edad, grid=[0, 1, 2, 1])

# Etiqueta para mostrar el resultado
resultado = Text(box, text="", grid=[0, 2, 2, 1])

# Iniciar la aplicación
app.display()