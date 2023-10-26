from guizero import App, Box, Text, TextBox, PushButton

# Función para determinar el día de la semana
def determinar_dia_semana():
    try:
        numero = int(numero_box.value)  # Convertir el número ingresado a entero
        if 1 <= numero <= 7:  # Verificar si el número está en el rango del 1 al 7
            # Lista de días de la semana
            dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
            dia_semana = dias_semana[numero - 1]  # Obtener el día correspondiente
            resultado.value = f"El número {numero} corresponde a {dia_semana}."
        else:
            resultado.value = "Por favor, ingrese un número entre 1 y 7."
    except ValueError:
        resultado.value = "Por favor, ingrese un número válido."

# Crear una aplicación GUI
app = App("Día de la Semana", width=300, height=200)

# Crear una caja para organizar elementos
box = Box(app, layout="grid")

# Etiqueta para ingresar el número
Text(box, text="Ingrese un número del 1 al 7:", grid=[0, 0])

# Cuadro de texto para ingresar el número
numero_box = TextBox(box, grid=[1, 0])

# Botón para determinar el día de la semana
determinar_button = PushButton(box, text="Determinar Día de la Semana", command=determinar_dia_semana, grid=[0, 1, 2, 1])

# Etiqueta para mostrar el resultado
resultado = Text(box, text="", grid=[0, 2, 2, 1])

# Iniciar la aplicación
app.display()