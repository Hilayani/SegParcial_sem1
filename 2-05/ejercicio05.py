from guizero import App, Box, Text, TextBox, PushButton

# Listas para almacenar calificaciones
aprobados = []
reprobados = []
calificaciones_ingresadas = []

# Función para agregar calificaciones y mostrar el resultado
def agregar_calificacion():
    calificacion = input_calificacion.value
    try:
        calificacion = float(calificacion)
        if 0 <= calificacion <= 10:
            calificaciones_ingresadas.append(calificacion)
            if calificacion >= 7:
                aprobados.append(calificacion)
            else:
                reprobados.append(calificacion)
            input_calificacion.clear()
            mostrar_resultado()
        else:
            error_text.value = "Error: La calificación debe estar entre 0 y 10"
    except ValueError:
        error_text.value = "Error: Ingrese una calificación válida"

# Función para mostrar el resultado
def mostrar_resultado():
    aprobados_text.value = f"Aprobados: {len(aprobados)}"
    reprobados_text.value = f"Reprobados: {len(reprobados)}"
    total_calificaciones_text.value = f"Total calificaciones: {len(calificaciones_ingresadas)}"
    error_text.value = ""  # Limpiar cualquier mensaje de error anterior

# Crear una aplicación Guizero
app = App("Calculadora de Aprobados")

# Crear contenedores para los elementos
input_box = Box(app, layout="grid")
resultado_box = Box(app, layout="grid")

# Elementos
Text(input_box, text="Calificación: ", grid=[0, 0])
input_calificacion = TextBox(input_box, grid=[1, 0])
agregar_button = PushButton(input_box, text="Agregar Calificación", command=agregar_calificacion, grid=[2, 0])
aprobados_text = Text(resultado_box, text="", grid=[0, 0])
reprobados_text = Text(resultado_box, text="", grid=[0, 1])
total_calificaciones_text = Text(resultado_box, text="", grid=[0, 2])
error_text = Text(resultado_box, text="", grid=[0, 3], color="red")

app.display()