from guizero import App, Box, Text, TextBox, PushButton, ListBox

# Lista para almacenar los años de nacimiento
años_nacimiento = []

# Variable para llevar un registro de la cantidad deseada de personas
cantidad_personas = 0

# Función para calcular la edad promedio
def calcular_edad_promedio():
    try:
        if cantidad_personas == len(años_nacimiento):
            edades = [2023 - int(año) for año in años_nacimiento]
            edad_promedio = sum(edades) / len(edades)
            resultado.value = f"Edad promedio: {edad_promedio:.2f} años"
        else:
            resultado.value = "Asegúrese de ingresar el año de nacimiento de todas las personas."
    except ValueError:
        resultado.value = "Asegúrese de ingresar años de nacimiento válidos."

# Función para agregar el año de nacimiento
def agregar_año():
    try:
        año = int(entrada_año.value)
        if año <= 2023:
            años_nacimiento.append(entrada_año.value)
            lista_años.append(entrada_año.value)
            entrada_año.clear()
            if len(años_nacimiento) == cantidad_personas:
                agregar_button.disable()
        else:
            entrada_año.clear()
    except ValueError:
        entrada_año.clear()

# Función para configurar la cantidad de personas
def configurar_cantidad():
    global cantidad_personas
    try:
        cantidad_personas = int(cantidad_personas_input.value)
        if cantidad_personas > 0:
            cantidad_personas_input.disable()
            configurar_button.disable()
            entrada_año.enable()
            agregar_button.enable()
            calcular_button.enable()
        else:
            cantidad_personas_input.clear()
    except ValueError:
        cantidad_personas_input.clear()

# Crear la aplicación y la ventana
app = App("Calculadora de Edad Promedio", width=350, height=300)

# Crear contenedores
main_box = Box(app, layout="grid")

# Etiquetas y campos de entrada
cantidad_personas_label = Text(main_box, "Ingrese la cantidad de personas:", grid=[0, 0, 2, 1])
cantidad_personas_input = TextBox(main_box, grid=[2, 0])
configurar_button = PushButton(main_box, configurar_cantidad, text="Configurar", grid=[3, 0])

año_nacimiento_label = Text(main_box, "Ingrese el año de nacimiento:", grid=[0, 1])
entrada_año = TextBox(main_box, grid=[1, 1])
agregar_button = PushButton(main_box, agregar_año, text="Agregar", grid=[2, 1])

lista_años_label = Text(main_box, "Años de nacimiento ingresados:", grid=[0, 2, 2, 1])
lista_años = ListBox(main_box, items=[], grid=[2, 2, 2, 4])

calcular_button = PushButton(main_box, calcular_edad_promedio, text="Calcular Edad Promedio", grid=[0, 7, 4, 1])
resultado = Text(main_box, "", grid=[0, 8, 4, 1])

# Ejecutar la aplicación
app.display()
