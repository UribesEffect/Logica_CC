# Visualizacion de tableros de ajedrez 3x3 a partir de
# una lista de literales. Cada literal representa una casilla;
# el literal es positivo sii hay un caballo en la casilla.

# Formato de la entrada: - las letras proposionales seran: 1, ..., 9;
#                        - solo se aceptan literales (ej. 1, ~2, 3, ~4, etc.)
# Requiere también un número natural, para servir de índice del tablero,
# toda vez que pueden solicitarse varios tableros.

# Salida: archivo tablero_%i.png, donde %i es un número natural

#################
# importando paquetes para dibujar
print("Importando paquetes...")
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
print("Listo!")

def dibujar_tablero(f, letras, n):
  # Visualiza un tablero dada una formula f
    # Input:
    #   - f, una lista de literales
    #   - n, un numero de identificacion del archivo
    # Output:
    #   - archivo de imagen tablero_n.png

    # Inicializo el plano que contiene la figura
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    # Dibujo el tablero
    step1 = 1./5
    step2 = 1./4
    tangulos = []

    # Creo los cuadrados claros en el tablero
    tangulos.append(patches.Rectangle((0, step2), step1, step2, facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(step1, 0), step1, step2], facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(2 * step1, step2), step1, step2], facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(step1, 2 * step2), step1, step2], facecolor='cornsilk'))


    # Creo los cuadrados oscuros en el tablero
    tangulos.append(patches.Rectangle(*[(2 * step1, 2 * step2), step1, step2], facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(0, 2 * step2), step1, step2], facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(2 * step1, 0), step1, step2], facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(step1, step2), step1, step2], facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(0, 0), step1, step2], facecolor='lightslategrey'))

    ###############################################################################
    tangulos.append(patches.Rectangle(*[(0, 3 * step2), step1, step2], facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(3 * step1, step2), step1, step2], facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(3 * step1, 0), step1, step2], facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(step1, 3 * step2), step1, step2], facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(3 * step1, 3 * step2), step1, step2], facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(3 * step1, 2 * step2), step1, step2], facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(2 * step1, 3 * step2), step1, step2], facecolor='cornsilk'))
    ################################################################################
    tangulos.append(patches.Rectangle(*[(4 * step1, 3 * step2), step1, step2], facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(4 * step1, 2 * step2), step1, step2], facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(4 * step1, 1 * step2), step1, step2], facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(4 * step1, 0 * step2), step1, step2], facecolor='lightslategrey'))
    #################################################################################

    # Creo las líneas del tablero
    for j in range(3):
        locacion = j * step2
        # Crea linea horizontal en el rectangulo
        tangulos.append(patches.Rectangle(*[(0, step2 + locacion), 1, 0.005], facecolor='black'))
             

    for k in range(4):
        locacion = k * step1
        # Crea linea vertical en el rectangulo
        tangulos.append(patches.Rectangle(*[(step1 + locacion, 0), 0.005, 1], facecolor='black'))

    for t in tangulos:
        axes.add_patch(t)

    # Creando las direcciones de los numeros de acuerdo al literal
    direcciones = {}
    direcciones[1] = [0.1, 0.875]  # A
    direcciones[2] = [0.3, 0.875]  # B
    direcciones[3] = [0.5, 0.875]  # C
    direcciones[4] = [0.7, 0.875]  # D
    direcciones[5] = [0.9, 0.875]  # E
    direcciones[6] = [0.1, 0.625]  # F
    direcciones[7] = [0.3, 0.625]  # G
    direcciones[8] = [0.5, 0.625]  # H
    direcciones[9] = [0.7, 0.625]  # I
    direcciones[10] = [0.9, 0.625] # J
    direcciones[11] = [0.1, 0.375] # K
    direcciones[12] = [0.3, 0.375] # L
    direcciones[13] = [0.5, 0.375] # M
    direcciones[14] = [0.7, 0.375] # N
    direcciones[15] = [0.9, 0.375] # P
    direcciones[16] = [0.1, 0.125] # Q
    direcciones[17] = [0.3, 0.125] # R
    direcciones[18] = [0.5, 0.125] # S
    direcciones[19] = [0.7, 0.125] # T
    direcciones[20] = [0.9, 0.125] # U
   

    # Asignar direccion a cada casilla del tablero
    aux = {}
    for i in range(1, 10):
        aux["A0" + str(i)] = 1
        aux["B0" + str(i)] = 2
        aux["C0" + str(i)] = 3
        aux["D0" + str(i)] = 4
        aux["E0" + str(i)] = 5
        aux["F0" + str(i)] = 6
        aux["G0" + str(i)] = 7
        aux["H0" + str(i)] = 8
        aux["I0" + str(i)] = 9
        aux["J0" + str(i)] = 10
        aux["K0" + str(i)] = 11
        aux["L0" + str(i)] = 12
        aux["M0" + str(i)] = 13
        aux["N0" + str(i)] = 14
        aux["P0" + str(i)] = 15
        aux["Q0" + str(i)] = 16
        aux["R0" + str(i)] = 17
        aux["S0" + str(i)] = 18
        aux["T0" + str(i)] = 19
        aux["U0" + str(i)] = 20
 
    for i in range(10, 21):
        aux["A" + str(i)] = 1
        aux["B" + str(i)] = 2
        aux["C" + str(i)] = 3
        aux["D" + str(i)] = 4
        aux["E" + str(i)] = 5
        aux["F" + str(i)] = 6
        aux["G" + str(i)] = 7
        aux["H" + str(i)] = 8
        aux["I" + str(i)] = 9
        aux["J" + str(i)] = 10
        aux["K" + str(i)] = 11
        aux["L" + str(i)] = 12
        aux["M" + str(i)] = 13
        aux["N" + str(i)] = 14
        aux["P" + str(i)] = 15
        aux["Q" + str(i)] = 16
        aux["R" + str(i)] = 17
        aux["S" + str(i)] = 18
        aux["T" + str(i)] = 19
        aux["U" + str(i)] = 20
       


    # Asignamos los numeros de la interpretacion al tablero
    for l in f:
        if f[l] == 1:
            print(l, letras[l])
            #print(direcciones[aux[l]][0], direcciones[aux[l]][1])
            plt.text(direcciones[aux[l]][0], direcciones[aux[l]][1], letras[l],
                     fontsize = 15, horizontalalignment = 'center',
                     verticalalignment = 'center')

    # plt.show()

    # Salvamos la imagen del tablero con la respectiva interpretación
    fig.savefig("tablero_4x5_" + str(n) + ".png")



#################################### Bloque principal de instruccion##########################################

# Creamos las interpretaciones

inter1 = {}
for i in range(1, 10):
    inter1["A0" + str(i)] = 0
    inter1["B0" + str(i)] = 0
    inter1["C0" + str(i)] = 0
    inter1["D0" + str(i)] = 0
    inter1["E0" + str(i)] = 0
    inter1["F0" + str(i)] = 0
    inter1["G0" + str(i)] = 0
    inter1["H0" + str(i)] = 0
    inter1["I0" + str(i)] = 0
    inter1["K0" + str(i)] = 0
    inter1["J0" + str(i)] = 0
    inter1["M0" + str(i)] = 0
    inter1["L0" + str(i)] = 0
    inter1["N0" + str(i)] = 0
    inter1["P0" + str(i)] = 0
    inter1["Q0" + str(i)] = 0
    inter1["R0" + str(i)] = 0
    inter1["S0" + str(i)] = 0
    inter1["T0" + str(i)] = 0
    inter1["U0" + str(i)] = 0
  

for i in range(10, 21):
    inter1["A" + str(i)] = 0
    inter1["B" + str(i)] = 0
    inter1["C" + str(i)] = 0
    inter1["D" + str(i)] = 0
    inter1["E" + str(i)] = 0
    inter1["F" + str(i)] = 0
    inter1["G" + str(i)] = 0
    inter1["H" + str(i)] = 0
    inter1["I" + str(i)] = 0
    inter1["K" + str(i)] = 0
    inter1["J" + str(i)] = 0
    inter1["M" + str(i)] = 0
    inter1["L" + str(i)] = 0
    inter1["N" + str(i)] = 0
    inter1["P" + str(i)] = 0
    inter1["Q" + str(i)] = 0
    inter1["R" + str(i)] = 0
    inter1["S" + str(i)] = 0
    inter1["T" + str(i)] = 0
    inter1["U" + str(i)] = 0
  

# Letras proposicionales con valor de verdad en 1

inter1["A01"] = 1
inter1["B02"] = 1
inter1["C03"] = 1
inter1["D04"] = 1
inter1["E05"] = 1
inter1["F06"] = 1
inter1["G07"] = 1
inter1["H08"] = 1
inter1["I09"] = 1
inter1["J10"] = 1
inter1["K11"] = 1
inter1["L12"] = 1
inter1["M13"] = 1
inter1["N14"] = 1
inter1["P15"] = 1
inter1["Q16"] = 1
inter1["R17"] = 1
inter1["S18"] = 1
inter1["T19"] = 1
inter1["U20"] = 1



###############################################################################

inter2 = {}
for i in range(1, 10):
    inter2["A0" + str(i)] = 0
    inter2["B0" + str(i)] = 0
    inter2["C0" + str(i)] = 0
    inter2["D0" + str(i)] = 0
    inter2["E0" + str(i)] = 0
    inter2["F0" + str(i)] = 0
    inter2["G0" + str(i)] = 0
    inter2["H0" + str(i)] = 0
    inter2["I0" + str(i)] = 0
    inter2["K0" + str(i)] = 0
    inter2["J0" + str(i)] = 0
    inter2["M0" + str(i)] = 0
    inter2["L0" + str(i)] = 0
    inter2["N0" + str(i)] = 0
    inter2["P0" + str(i)] = 0
    inter2["Q0" + str(i)] = 0
    inter2["R0" + str(i)] = 0
    inter2["S0" + str(i)] = 0
    inter2["T0" + str(i)] = 0
    inter2["U0" + str(i)] = 0
   

for i in range(10, 21):
    inter2["A" + str(i)] = 0
    inter2["B" + str(i)] = 0
    inter2["C" + str(i)] = 0
    inter2["D" + str(i)] = 0
    inter2["E" + str(i)] = 0
    inter2["F" + str(i)] = 0
    inter2["G" + str(i)] = 0
    inter2["H" + str(i)] = 0
    inter2["I" + str(i)] = 0
    inter2["K" + str(i)] = 0
    inter2["J" + str(i)] = 0
    inter2["M" + str(i)] = 0
    inter2["L" + str(i)] = 0
    inter2["N" + str(i)] = 0
    inter2["P" + str(i)] = 0
    inter2["Q" + str(i)] = 0
    inter2["R" + str(i)] = 0
    inter2["S" + str(i)] = 0
    inter2["T" + str(i)] = 0
    inter2["U" + str(i)] = 0
 

# Letras proposicionales con valor de verdad en 1

inter2["A01"] = 1
inter2["B02"] = 1
inter2["C03"] = 1
inter2["D04"] = 1
inter2["E05"] = 1
inter2["F10"] = 1
inter2["G09"] = 1
inter2["H08"] = 1
inter2["I07"] = 1
inter2["J06"] = 1
inter2["K11"] = 1
inter2["L12"] = 1
inter2["M13"] = 1
inter2["N14"] = 1
inter2["P15"] = 1
inter2["Q20"] = 1
inter2["R19"] = 1
inter2["S18"] = 1
inter2["T17"] = 1
inter2["U16"] = 1

###############################################################################

# Asignamos los posibles numeros del tablero a las letras proposicionales

asig = {}
for i in range(1, 10):
    asig["A0" + str(i)] = i
    asig["B0" + str(i)] = i
    asig["C0" + str(i)] = i
    asig["D0" + str(i)] = i
    asig["E0" + str(i)] = i
    asig["F0" + str(i)] = i
    asig["G0" + str(i)] = i
    asig["H0" + str(i)] = i
    asig["I0" + str(i)] = i
    asig["K0" + str(i)] = i
    asig["J0" + str(i)] = i
    asig["M0" + str(i)] = i
    asig["L0" + str(i)] = i
    asig["N0" + str(i)] = i
    asig["P0" + str(i)] = i
    asig["Q0" + str(i)] = i
    asig["R0" + str(i)] = i
    asig["S0" + str(i)] = i
    asig["T0" + str(i)] = i
    asig["U0" + str(i)] = i
   

for i in range(10, 21):
    asig["A" + str(i)] = i
    asig["B" + str(i)] = i
    asig["C" + str(i)] = i
    asig["D" + str(i)] = i
    asig["E" + str(i)] = i
    asig["F" + str(i)] = i
    asig["G" + str(i)] = i
    asig["H" + str(i)] = i
    asig["I" + str(i)] = i
    asig["K" + str(i)] = i
    asig["J" + str(i)] = i
    asig["M" + str(i)] = i
    asig["L" + str(i)] = i
    asig["N" + str(i)] = i
    asig["P" + str(i)] = i
    asig["Q" + str(i)] = i
    asig["R" + str(i)] = i
    asig["S" + str(i)] = i
    asig["T" + str(i)] = i
    asig["U" + str(i)] = i
 

###############################################################################

# Invocamos las funciones con las interpretaciones

dibujar_tablero(inter1, asig, 1)
dibujar_tablero(inter2, asig, 2)
