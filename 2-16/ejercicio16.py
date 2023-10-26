#Crea el dfd del menú de una calculadora funcional que puede sumar, restar, multiplicar y 
#dividir al seleccionar el tipo de operación y dar dos números

from guizero import App, Box, Text, TextBox, PushButton, Combo

# Función para realizar la operación seleccionada
def realizar_operacion():
    try:
        numero1 = float(numero1_box.value)
        numero2 = float(numero2_box.value)
        operacion = operacion_combo.value

        if operacion == "Sumar":
            resultado = numero1 + numero2
        elif operacion == "Restar":
            resultado = numero1 - numero2
        elif operacion == "Multiplicar":
            resultado = numero1 * numero2
        elif operacion == "Dividir":
            resultado = numero1 / numero2
        else:
            resultado = "Operación no válida"

        resultado_label.value = f"Resultado: {resultado:.2f}"
    except ValueError:
        resultado_label.value = "Por favor, ingrese números válidos."

# Crear una aplicación GUI
app = App("Calculadora", width=300, height=300)

# Crear una caja para organizar elementos
box = Box(app, layout="grid")

# Etiqueta y cuadro de texto para ingresar el primer número
Text(box, text="Número 1:", grid=[0, 0])

# Cuadro de texto para ingresar el primer número
numero1_box = TextBox(box, grid=[1, 0])

# Etiqueta y cuadro de texto para ingresar el segundo número
Text(box, text="Número 2:", grid=[0, 1])

# Cuadro de texto para ingresar el segundo número
numero2_box = TextBox(box, grid=[1, 1])

# Etiqueta y cuadro de texto para seleccionar la operación
Text(box, text="Operación:", grid=[0, 2])

# Cuadro combinado (Combo) para seleccionar la operación
operaciones = ["Sumar", "Restar", "Multiplicar", "Dividir"]
operacion_combo = Combo(box, options=operaciones, grid=[1, 2])

# Botón para realizar la operación
calcular_button = PushButton(box, text="Calcular", command=realizar_operacion, grid=[0, 3, 2, 1])

# Etiqueta para mostrar el resultado
resultado_label = Text(box, text="", grid=[0, 4, 2, 1])

# Iniciar la aplicación
app.display()