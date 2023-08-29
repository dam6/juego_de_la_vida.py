'''
Creado por dam6 
https://github.com/dam6
'''

# ------------ Variables globales --------------------------------------------

tablero = []
vivas = []

# ------------ Presentación --------------------------------------------

def cabecera(texto):
    '''
    Uso: Muestra por pantalla una cabecera con el mismo formato para cada funcion que se presenta al usuario.
    Recibe: Un texto para cada funcion.
    Devuelve: Nada.
    Dependencias: Ninguna.
    '''
    print("")
    print(f"-------------- {texto} --------------")
    print("")

def informacion(texto):
    '''
    Uso: Muestra por pantalla informacion relevante al ususario.
    Recibe: Un texto para cada funcion.
    Devuelve: Nada.
    Dependencias: Ninguna.
    '''
    print("")
    print(f"Info: {texto}")

# ------------ Funciones Tablero --------------------------------------------

def crearTablero(tablero, vivas):
    '''
    Uso: Crea o sobreescribe el tablero de juego con los parametros definidos por el usuaio.
    Recibe: El tableo actual. 
    Devuelve: El nuevo tablero.
    Dependencias: cabecera(), pedirEntero(), informacion(), finjuego(), actualizarTablero()
    '''
    cabecera("CREAR TABLERO")
    print("Elige de cuantas filas y columnas estara formado tu tablero")
    while True: #Bucle hasta que se den inputs aceptables
        num_fil = pedirEntero("Elige un numero de filas: ")
        num_col = pedirEntero("Elige un numero de columnas: ")
                
        if (num_col == "SALIR") or (num_fil == "SALIR"): #Si el usuario elige salir
            informacion("Has elegido salir. No se creara ningun tablero.")
            tablero = []
            return tablero
        elif (num_fil > 2) and (num_col > 2): #Si el usuario crea un tablero correctamente
            tablero =[ [0 for columna in range(num_col)] for fila in range(num_fil)]
            tablero = actualizarTablero(tablero, vivas)
            return tablero
        else: #Si los inputs del usuario no son validos
            informacion("Introduce valores validos para crear un tablero.")

def mostrarTablero(tablero):
    '''
    Uso: Muestra por pantalla el tablero actual.
    Recibe: El tablero actual.
    Devuelve: Nada.
    Dependencias: cabecera()
    '''
    cabecera("MOSTRAR TABLERO")
    for f in tablero:
        for c in f:
            print(c, end=' ')
        print("")

def dimensionesTablero(tablero):
    '''
    Uso: Comprueba el numero de filas y columnas que tiene el tablero actual.
    Recibe: El tablero actual. 
    Devuelve: Una tupla con el numero de filas y columnas del tablero actual. En ese orden.
    Dependencias: Ninguna.
    '''
    num_fil = len(tablero)
    num_col = len(tablero[0])
    return num_fil, num_col

def actualizarTablero(tablero, vivas):
    '''
    Uso: Actualiza la situacion del tablero cuando cambian las celulas vivas o las dimensiones de este.
    Recibe: El tablero actual y la lista de celulas vivas. 
    Devuelve: El tablero actual.
    Dependencias: dimensionesTablero()
    '''
    num_fil, num_col = dimensionesTablero(tablero)
    for c in range(num_col):
        for f in range(num_fil):
            pos = f,c #Forma una tupla para comprobar la posicion en la lista de celulas vivas
            if pos not in vivas:
                tablero[f][c] = " " #Si la posicion no esta en la lista
            else:
                tablero[f][c] = "+" #Si la posicion esta en la lista
    return tablero

# ------------ Interacción con el usuario --------------------------------------------

def pedirEntero(texto):
    '''
    Uso: Interactua con el usuario pidiendole un valor numerico entero. Mientras el valor no sea válido, vuelve a pedir.
    Recibe: El texto que se presenta al usuario.
    Devuelve: El valor proporcionado por el usuario.
    Dependencias: cabecera(), informacion()
    '''
    cabecera("PEDIR ENTERO")
    while True: #Bucle hasta que se den inputs aceptables
        try:
            num = int(input(texto))
            if (num >= 0): #Aceptado
                return num
            elif (num == -1): #Elige salir
                return "SALIR"
        except: #Si no es un numero entero
            informacion("Introduce un valor entero")

def pedirOpcion(opciones):
    '''
    Uso: Interactua con el usuario mostrando las opciones disponibles en la pantalla actual y validando la elección del usuario. Mientras el valor no sea válido, vuelve a pedir.
    Recibe: Un diccionario con pares del tipo "opcion":"descripcion". Tanto "opcion" como "descripcion" son de tipo texto.
    Devuelve: La opción que selecciona el usuario.
    Dependencias: cabecera(), informacion()
    '''
    cabecera("PEDIR OPCION")
    print("Elige una opcion del siguiente menu")
    print(opciones)
    print("")
    while True: #Bucle hasta que se den inputs aceptables
        operacion = input("Elige una opcion: ")
        if operacion in opciones.keys(): #Si el input esta en las opciones
            return operacion
        else: #Si el input no esta en las opciones
            print("Introduce un valor valido")

def pediryvalidarCoordenada(tablero):
    '''
    Uso: Interactua con el usuario pidiendole una posicion formada por una fila y una columna y se valida la entrada.
    Recibe: El tablero actual.
    Devuelve: Texto "SALIR" o "Valido" y la posicion validada.
    Dependencias: dimensionesTablero(), pedirEntero(), informacion()
    '''
    num_fil, num_col = dimensionesTablero(tablero)
    while True: #Bucle hasta que se den inputs aceptables
        posicion = pedirEntero(f"Elige la fila. De 0 a {num_fil-1}. -1 para SALIR: "),pedirEntero(f"Elige la columna. De 0 a {num_col-1}. -1 para SALIR: ")
        if "SALIR" in posicion: #Si el usuario elige salir
            return "SALIR", posicion
        elif ((posicion[0] <= num_fil-1 ) and (posicion[1] <= num_col-1)): #Si la entrada esta dentro del tablero
            return "Valido", posicion
        else: #Si la entrada es incorrecta
            informacion("Elige una posicion dentro del tablero")

def editarVivasTerminal(tablero, vivas):
    '''
    Uso: Uso: Interactua con el usuario permitiendo añadir o borrar celulas en una posicion del tablero especifica mediante escribir la posicion. En cualquier momento de la partida. Las posiciones forman tuplas dentro de una lista.
    Recibe: El tablero actual. 
    Devuelve: Una lista de tuplas que forman las posiciones de las celulas vivas.
    Dependencias: cabecera(), pediryvalidarCoordenada(), actualizarTablero(), mostrarTablero(), informacion()
    '''
    cabecera("EDITAR CELULAS VIVAS POR TERMINAL")
    print("Elige una posicion donde añadir o borrar celulas")
    while True:
        estado, posicion = pediryvalidarCoordenada(tablero)
    
        if estado == "SALIR":
            break
        elif estado == "Valido":
            if posicion not in vivas:
                vivas.append(posicion)
                informacion(f"Añadida celula a la posicion {posicion}")
            else:
                vivas.remove(posicion)
                informacion(f"Borrada la celula de la posicion {posicion}")
        
        informacion(f"Las celulas vivas son: {vivas}")
    
    informacion(f"Has elegido salir. Las celulas vivas son: {vivas}")
    tablero = actualizarTablero(tablero, vivas)
    mostrarTablero(tablero)
    return vivas

def editarVivasGrafico(tablero, vivas):
    '''
    Uso: Interactua con el usuario permitiendo añadir o borrar celulas en una posicion del tablero especifica mediante mover un cursor por el tablero. En cualquier momento de la partida. Las posiciones forman tuplas dentro de una lista.
    Recibe: El tablero actual. 
    Devuelve: Una lista de tuplas que forman las posiciones de las celulas vivas.
    Dependencias: cabecera(), dimensionesTablero(), pediryvalidarCoordenada(), actualizarTablero(), mostrarTablero(), pedirOpcion(), informacion()
    '''
    cabecera("EDITAR CELULAS GRAFICAMENTE")
    print("Muevete por el tablero mientras añades o borras celulas")
    num_filas, num_colum = dimensionesTablero(tablero)
    
    fila = 0
    columna = 0
    copia_anterior = tablero[fila][columna]

    terminar = False
    while not terminar:
        posicion = fila, columna
        f = fila
        c = columna

        tablero = actualizarTablero(tablero, vivas)
        tablero[fila][columna] = "O"
        mostrarTablero(tablero)
        informacion(f"Las celulas vivas son: {vivas} y tu posicion es {posicion}")

        opcionesEditarGrafico = {'w': 'Arriba', 'a': 'Izquierda', 's': 'Abajo', 'd': 'Derecha', 'x': 'Añadir/Borrar celula', '-1': 'Salir'}
        orden = pedirOpcion(opcionesEditarGrafico)

        if orden == "-1":
            break

        elif orden == "d":
            if c < num_colum-1:
                tablero[f][c] = copia_anterior
                copia_anterior = tablero[f][c+1]
                columna = c+1
            if c == num_colum-1:
                tablero[f][c] = copia_anterior
                copia_anterior = tablero[f][0]
                columna = 0

        elif orden == "a":
            if c > 0:
                tablero[f][c] = copia_anterior
                copia_anterior = tablero[f][c-1]
                columna = c-1
            if c == 0:
                tablero[f][c] = copia_anterior
                copia_anterior = tablero[f][num_colum-1]
                columna = num_colum-1

        elif orden == "s":
            if f < num_filas-1:
                tablero[f][c] = copia_anterior
                copia_anterior = tablero[f+1][c]
                fila = f+1
            if f == num_filas-1:
                tablero[f][c] = copia_anterior
                copia_anterior = tablero[0][c]
                fila = 0

        elif orden == "w":
            f = fila
            if f > 0:
                tablero[f][c] = copia_anterior
                copia_anterior = tablero[f-1][columna]
                fila = f-1
            if f == 0:
                tablero[f][c] = copia_anterior
                copia_anterior = tablero[num_filas-1][c]
                fila = num_filas-1
        
        elif orden == "x":
            posicion = f, c
            if posicion not in vivas:
                vivas.append(posicion)
                informacion(f"Añadida celula a la posicion {posicion}")
            else:
                vivas.remove(posicion)
                informacion(f"Borrada la celula de la posicion {posicion}")
    
    tablero = actualizarTablero(tablero, vivas)
    mostrarTablero(tablero)
    informacion(f"Has elegido salir. Las celulas vivas son: {vivas}")
    return vivas

# ------------ Funciones Juego --------------------------------------------

def avanzarGeneracion(tablero,vivas):
    '''
    Uso: Aplica el algoritmo principal del juego y las reglas de este a la partida actual para avanzar una generacion.
    Recibe: El tablero actual y una lista de tuplas con las posiciones de las celulas vivas.
    Devuelve: Una lista de tuplas con las posiciones de las celulas vivas.
    Dependencias: cabecera(), dimensionesTablero(), actualizarTablero(), mostrarTablero(),
    '''
    cabecera("AVANZAR GENERACION")
    num_fil, num_col = dimensionesTablero(tablero)
    
    tablero = actualizarTablero(tablero,vivas)
    mostrarTablero(tablero)
    informacion(f"Las celulas vivas son: {vivas}")
    
    #Se prepara la siguiente genearcion
    generacionSiguiente = []

    for col in range(num_col): #Recorrer todo el tablero
        for fil in range(num_fil):
            viva = False #"Mata" la celula hasta que se demuestre que esta viva
            contador = 0 #Celulas vivas alrededor
            celula = fil,col #Forma una tupla con la posicion de la celula a comprobar

            for c in range(col-1, col+2): #Mini matriz de para comprobar las celulas de alrededor
                for f in range(fil-1, fil+2):
                    alrededor = f,c #Forma una tupla con la posicion de la celula de alrededor que se esta comprobando

                    if alrededor in vivas: #Si la celula de alrededor esta viva
                        contador +=1
                        if (c == col) and (f == fil): #Se ha sumado ella misma al recorrer la "mini matriz" como si fuera del alrededor. Necesario restar.
                            contador -=1

            if (contador < 2) or (contador > 3): #Reglas 1 y 2
                viva = False
            elif (celula in vivas) and ((contador == 2) or (contador == 3)): #Regla 3
                viva = True
            elif (celula not in vivas) and (contador == 3): #Regla 4
                viva = True

            if viva: #Si la celula esta viva para la siguiente generacion, se añade la posicion a la lista de generacionSiguiente
                generacionSiguiente.append(celula) 
    
    #Cuando acaba la comprobacion de todas las celulas, se borra la lista de la generacion anterior y se añade la de la siguiente
    vivas.clear()
    vivas.extend(generacionSiguiente)
    return vivas

def finjuego():
    '''
    Uso: Acabar el juego.
    Recibe: Nada.
    Devuelve: Nada.
    Dependencias: cabecera(), informacion()
    '''
    cabecera("FIN JUEGO")
    quit()

# ------------ Programa Principal --------------------------------------------

opcionesMenu = {'1':'Crear tablero', '2':'Editar celulas', '3':'Avanzar', '-1':'Salir del juego'}

terminar = False

while not terminar:
    operacion = pedirOpcion(opcionesMenu)

    if operacion == "1":
        tablero = crearTablero(tablero, vivas)
    elif operacion == "2" and tablero != []:
        opcionesEditar = {'1': 'Modo Grafico', '2': 'Modo Terminal'}
        operacion = pedirOpcion(opcionesEditar)
        if operacion == "1":
            vivas = editarVivasGrafico(tablero, vivas)
        elif operacion == "2":
            vivas = editarVivasTerminal(tablero, vivas)
    elif operacion == "3" and tablero != []:
        vivas = avanzarGeneracion(tablero, vivas)
    elif operacion == "-1":
        finjuego()
    else:
        informacion("Tienes que crear un tablero primero")
