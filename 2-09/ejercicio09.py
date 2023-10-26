from guizero import App, Box, Text, TextBox, PushButton

# Variables globales
n = 0
contador = 0
suma_cuadrados_pares = 0
suma_cubos_impares = 0
suma_total = 0

# Función para solicitar la cantidad de números
def pedir_cantidad():
    global n
    n = int(cantidad_box.value)
    cantidad_box.disable()
    siguiente_numero()

# Función para ingresar el siguiente número
def siguiente_numero():
    global contador
    if contador < n:
        text_box.value = f"Ingrese el número {contador + 1}:"
        numero_box.enable()
        calcular_button.enable()
    else:
        mostrar_resultado()

# Función para calcular el cuadrado o el cubo del número ingresado
def calcular_cuadrado_o_cubo():
    global contador, suma_cuadrados_pares, suma_cubos_impares
    numero = int(numero_box.value)
    
    if numero >= 0:
        if numero % 2 == 0:  # Es par
            cuadrado = numero ** 2
            suma_cuadrados_pares += cuadrado
        else:  # Es impar
            cubo = numero ** 3
            suma_cubos_impares += cubo
    
        contador += 1
        numero_box.clear()
        siguiente_numero()
    else:
        text_box.value = "Por favor, ingrese un número positivo."

# Función para mostrar el resultado
def mostrar_resultado():
    global suma_total
    suma_total = suma_cuadrados_pares + suma_cubos_impares
    resultado.value = f"La suma de los cuadrados de los números pares es: {suma_cuadrados_pares}\n"
    resultado.value += f"La suma de los cubos de los números impares es: {suma_cubos_impares}\n"
    resultado.value += f"La suma total es: {suma_total}"

# Crear una aplicación GUI
app = App("Suma de Cuadrados y Cubos de Números")

# Crear una caja para organizar elementos
box = Box(app, layout="grid")

# Etiqueta y cuadro de texto para ingresar la cantidad de números
Text(box, text="Cantidad de números a calcular:", grid=[0, 0])
cantidad_box = TextBox(box, grid=[1, 0])
cantidad_button = PushButton(box, text="Aceptar", command=pedir_cantidad, grid=[2, 0])

# Etiqueta, cuadro de texto y botón para ingresar los números
text_box = Text(box, text="", grid=[0, 1])
numero_box = TextBox(box, grid=[1, 1])
calcular_button = PushButton(box, text="Calcular", command=calcular_cuadrado_o_cubo, grid=[2, 1])
calcular_button.disable()
numero_box.disable()

# Etiqueta para mostrar el resultado
resultado = Text(box, text="", grid=[0, 2, 3, 1])

# Iniciar la aplicación
app.display()