# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 18:19:06 2020

@author: nicob
"""
#Nicolas Botero
#Santiago Uribe Luna


def codifica(f, c, Nf, Nc):
    # Funcion que codifica la fila f y columna c
    assert((f >= 0) and (f <= Nf - 1)), 'Primer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nf) - 1  + "\nSe recibio " + str(f)
    assert((c >= 0) and (c <= Nc - 1)), 'Segundo argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nc - 1)  + "\nSe recibio " + str(c)
    n = Nc * f + c
    # print(u'Número a codificar:', n)
    return n

def decodifica(n, Nf, Nc):
    # Funcion que codifica un caracter en su respectiva fila f y columna c de la tabla
    assert((n >= 0) and (n <= Nf * Nc - 1)), 'Codigo incorrecto! Debe estar entre 0 y' + str(Nf * Nc - 1) + "\nSe recibio " + str(n)
    f = int(n / Nc)
    c = n % Nc
    return f, c

Nfilas = 4
Ncolumnas = 5
print(u"Números correspondientes a la codificación:")
print("\nfilas(4) x columnas(5)")
for i in range(Nfilas):
    for j in range(Ncolumnas):
        v1 = codifica(i, j, Nfilas, Ncolumnas)
        print(v1, end = " ")
    print("")
    
# for v1 in range(20):
#     f, c = decodifica(v1, Nfilas, Ncolumnas)
#     print('Código: '+str(v1)+', Fila: '+str(f)+', Columna: '+str(c))

letras = []
# print("\n\nfilas x columnas")
for i in range(Nfilas):
    for j in range(Ncolumnas):
        v1 = codifica(i, j, Nfilas, Ncolumnas)
        cod = chr(v1 + 256)
        # print(cod, end = " ")
        letras.append(cod)
    print("")
# for cod in letras:
#     print('Letra = '+cod, end=', ')
#     f, c = decodifica(ord(cod)-256, Nfilas, Ncolumnas)
#     print('Fila = '+str(f), end=', ')
#     print('Columna = '+str(c))
    
def P(f, c, o, Nf, Nc, No):
    # Funcion que codifica tres argumentos
    assert((f >= 0) and (f <= Nf - 1)), 'Primer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nf - 1) + "\nSe recibio " + str(f)
    assert((c >= 0) and (c <= Nc - 1)), 'Segundo argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nc - 1) + "\nSe recibio " + str(c)
    assert((o >= 0) and (o <= No - 1)), 'Tercer argumento incorrecto! Debe ser un numero entre 0 y ' + str(No - 1)  + "\nSe recibio " + str(o)
    v1 = codifica(f, c, Nf, Nc)
    v2 = codifica(v1, o, Nf * Nc, No)
    codigo = chr(256 + v2)
    return codigo

def Pinv(codigo, Nf, Nc, No):
    # Funcion que codifica un caracter en su respectiva fila f, columna c y objeto o
    x = ord(codigo) - 256
    v1, o = decodifica(x, Nf * Nc, No)
    f, c = decodifica(v1, Nf, Nc)
    return f, c, o
letras = []
Nnumeros = 20
for k in range(Nnumeros):
    # print("Numero: "+str(k))
    # print("filas x columnas")
    for i in range(Nfilas):
        for j in range(Ncolumnas):
            cod = P(i, j, k, Nfilas, Ncolumnas, Nnumeros)
            # print(cod, end = " ")
            letras.append(cod)
    #     print("")
    # print('\n')
print("LETRAS PROPOSICIONALES")
for cod in letras:#codigo que me saca las proposiciones
    print('Letra = '+cod, end=', ')
    f, c, o = Pinv(cod, Nfilas, Ncolumnas, Nnumeros)
    f, c, o = f+1, c+1, o+1 
    # f+1=fe
    # c+1=ce
    # o+1=oe
    print('Numero = '+str(o), end=', ')
    print('Fila = '+str(f), end=', ')
    print('Columna = '+str(c))
print("##########RESTRICCIONES##########")
print("aqui se ven todas las letras que cumplen la siguiente restriccion")
# regla de existencia
def regla1():
    inicial = True
    for n in range(Nnumeros):
        for i in range(Nfilas):
            for h in range(Ncolumnas):
                inicial2 = True
                if inicial2:
                    formula1 = P(i, h, n, Nfilas, Ncolumnas, Nnumeros)
                    inicial2 = False
                else:
                    formula1 += P(i, h, n, Nfilas, Ncolumnas, Nnumeros) + "O"
                    
            if inicial:
                regla = formula1
                inicial = False
            else:
                regla += formula1 + "Y"
                
    return regla

def truncac(x):
        
    if x < 0:
            
        return 0
    elif x >4:
        return 4
    else:
        return x
def truncaf(x):
    if x <0:
            
        return 0
    elif x > 3:
        return 3
    else:
        return x
def adyacentes(casilla):
    x, y = casilla 
    adyacentes = [(truncaf(x - 1), y), (truncaf(x + 1), y), (x, truncac(y - 1)), (x, truncac(y + 1))]
    # meter diagonales
    adyacentes = [c for c in adyacentes if c != casilla]
    return adyacentes
def diagonales(casilla):
    x,y = casilla
    adyacentesd =[(truncaf(x - 1), truncac(y-1)), (truncaf(x - 1), truncac(y+1)), (truncaf(x+1), truncac(y - 1)), (truncaf(x+1), truncac(y + 1))]
    adyacentesd = [c for c in adyacentesd if c != casilla]
    return adyacentesd              
print(adyacentes((2,2))+diagonales((2,2)))

print(regla1())
# regla de perimetro revisa que numeros consecuentes puede meter cerca
def regla2():
    inicial2=True
    for n in range(Nnumeros-1):
        for  i  in range(Nfilas):
            for j in range(Ncolumnas):
                if inicial2:
                    casillasadyacentes=adyacentes((i,j))+diagonales((i,j))
                    formula=P(i, j, n, Nfilas, Ncolumnas, Nnumeros)+">"
                    for c in casillasadyacentes:
                        formula+=P(c[0],c[1],n+1, Nfilas, Ncolumnas, Nnumeros)+"O"
                    inicial2=False
                else:
                    casillasadyacentes=adyacentes((i,j))+diagonales((i,j))
                    formula+=P(i, j, n, Nfilas, Ncolumnas, Nnumeros)+">"
                    for c in casillasadyacentes:
                        formula+=P(c[0],c[1],n+1, Nfilas, Ncolumnas, Nnumeros)+"O"
                        
                    inicial2=False
    return formula
# revisa que nose repitan los numeros en la misma casilla
def regla3():
    inicial2=True
    for n in range(Nnumeros-1):
        for  i  in range(Nfilas):
            for j in range(Ncolumnas):
                if inicial2:
                    formula1 = P(i, j, n, Nfilas, Ncolumnas, Nnumeros)
                    for k in range(Nfilas):
                        for t in range(Ncolumnas):
                            if(i != k and j!=t):
                                formula1+=P(k, t, n, Nfilas, Ncolumnas, Nnumeros)+"-Y"
                    inicial2 = False
                    
                    
                else:
                    formula1 += P(i, j, n, Nfilas, Ncolumnas, Nnumeros)
                    for k in range(Nfilas):
                        for t in range(Ncolumnas):
                            if(i != k and j!=t):
                                formula1+=P(k, t, n, Nfilas, Ncolumnas, Nnumeros)+"-Y"
                    inicial2 = False
                    
                    
           
                
    return formula1
print(regla3())
print(regla2())

from random import choice
##############################################################################
# Variables globales
##############################################################################

# Crea las letras minúsculas a-z
letrasProposicionales = [chr(x) for x in range(97, 123)]
# inicializa la lista de interpretaciones
listaInterpsVerdaderas = []
# inicializa la lista de hojas
listaHojas = []

##############################################################################
# Definición de objeto tree y funciones de árboles
##############################################################################

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def string2Tree(A):
    letrasProposicionales=[chr(x) for x in range(97, 123)]
    Conectivos = ['O','Y','>','=']
    Pila = []
    for c in A:
        if c in letrasProposicionales:
            Pila.append(Tree(c,None,None))
        elif c=='-':
            FormulaAux = Tree(c,None,Pila[-1])
            del Pila[-1]
            Pila.append(FormulaAux)
        elif c in Conectivos:
            FormulaAux = Tree(c,Pila[-1],Pila[-2])
            del Pila[-1]
            del Pila[-1]
            Pila.append(FormulaAux)
        else:
            print(u"Hay un problema: el símbolo " + str(c)+ " no se reconoce")
    return Pila[-1]
def Inorder2Tree(A):
	if len(A) == 1:
		return Tree(A[0], None, None)
	elif A[0] == '-':
		return Tree(A[0], None, Inorder2Tree(A[1:]))
	elif A[0] == "(":
		counter = 0 #Contador de parentesis
		for i in range(1, len(A)):
			if A[i] == "(":
				counter += 1
			elif A[i] == ")":
				counter -=1
			elif (A[i] in ['Y', 'O', '>', '=']) and (counter == 0):
				return Tree(A[i], Inorder2Tree(A[1:i]), Inorder2Tree(A[i + 1:-1]))
	else:
		return -1

##############################################################################
# Definición de funciones de tableaux
##############################################################################

def imprime_hoja(H):
	cadena = "{"
	primero = True
	for f in H:
		if primero == True:
			primero = False
		else:
			cadena += ", "
		cadena += Inorder(f)
	return cadena + "}"
def imprime_listaHojas(L):
	for h in L:
		print(imprime_hoja(h))
def complemento(l):
    if (l.label == '-'):
        return l.right
    else:
        return Tree('-',None,l)

def par_complementario(l):
	# Esta función determina si una lista de solo literales
	# contiene un par complementario
	# Input: l, una lista de literales
	# Output: True/False
    for i in l:
        indices = [x for x in l if x != i]
        for j in indices:
            if (Inorder(i) == Inorder(complemento(j))):
                return True
        
    return False

def es_literal(f):
	# Esta función determina si el árbol f es un literal
	# Input: f, una fórmula como árbol
	# Output: True/False
    if (f.label == "-"):
        if(f.right.label in letrasProposicionales):
            return True
#        elif(f.right.label == "-"):
#            if (f.right.right.label in letrasProposicionales):
#                return True
    if(f.label in letrasProposicionales):
        return True
    return False

def no_literales(l):
	# Esta función determina si una lista de fórmulas contiene
	# solo literales
	# Input: l, una lista de fórmulas como árboles
	# Output: None/f, tal que f no es literal

    for i in l:
       if (es_literal(i) == False):
            return i
        
    return None
def clasificacion(l):
    if (l.label == '-'):
        if (l.right.label == '-'):
            return "1alfa"
        elif (l.right.label == 'O'):
            return "3alfa"
        elif (l.right.label == '>'):
            return "4alfa"
        elif (l.right.label == 'Y'):
            return "1beta"
        
    if (l.label == 'Y'):
        return "2alfa"
    
    if (l.label == 'O'):
        return "2beta"
    
    if (l.label == '>'):
        return "3beta"
    return "error"

# a=Tree('>',Tree('Y',Tree('p',None,None),Tree('>',Tree('p',None,None),Tree('q',None,None))),Tree('q',None,None))

# print(clasificacion(a))
def clasifica_y_extiende(f, h):
	# clasifica una fórmula como alfa o beta y extiende listaHojas
	# de acuerdo a la regla respectiva
	# Input: f, una fórmula como árbol 
	# Output: no tiene output, pues modifica la variable global listaHojas
    global listaHojas
    tipo = clasificacion(f)
    if (tipo == "1alfa"):
        aux = [x for x in h if x!=f] + [f.right.right]
        listaHojas.remove(h)
        listaHojas.append(aux)
    elif (tipo == "2alfa"):
        aux = [x for x in h if x!=f] + [f.left, f.right]
        listaHojas.remove(h)
        listaHojas.append(aux)
    elif (tipo == "3alfa"):
        aux = [x for x in h if x!=f] + [Tree('-', None, f.right.right), Tree('-', None, f.right.left)]
        listaHojas.remove(h)
        listaHojas.append(aux)
    elif (tipo == "4alfa"):
        aux = [x for x in h if x!=f] + [f.right.left, Tree('-', None, f.right.right)]
        listaHojas.remove(h)
        listaHojas.append(aux)
    elif (tipo == "1beta"):
        aux1 = [x for x in h if x!=f] + [Tree('-', None, f.right.right)]
        aux2 = [x for x in h if x!=f] + [Tree('-', None, f.right.left)]
        listaHojas.remove(h)
        listaHojas.append(aux1)
        listaHojas.append(aux2)
    elif (tipo == "2beta"):
        aux1 = [x for x in h if x!=f] + [f.right]
        aux2 = [x for x in h if x!=f] + [f.left]
        listaHojas.remove(h)
        listaHojas.append(aux1)
        listaHojas.append(aux2)
    elif (tipo == "3beta"):
        aux1 = [x for x in h if x!=f] + [f.right]
        aux2 = [x for x in h if x!=f] + [Tree('-', None, f.left)]
        listaHojas.remove(h)
        listaHojas.append(aux1)
        listaHojas.append(aux2)
        
# f = Inorder2Tree('-(pO(rYs))')

# h = [f, Inorder2Tree('q'), Inorder2Tree('p')]

# listaHojas = [h]

# clasifica_y_extiende(f, h)

# imprime_listaHojas(listaHojas)

def Tableaux(f):

	# Algoritmo de creacion de tableau a partir de lista_hojas
	# Imput: - f, una fórmula como string en notación polaca inversa
	# Output: interpretaciones: lista de listas de literales que hacen
	#		 verdadera a f

	global listaHojas
	global listaInterpsVerdaderas

	A = string2Tree(f)
	print(u'La fórmula introducida es:\n', Inorder(A))

	listaHojas = [[A]]

	while (len(listaHojas) > 0):
		h = choice(listaHojas)
		print("Trabajando con hoja:\n", imprime_hoja(h))
		x = no_literales(h)
		if x == None:
			if par_complementario(h):
				listaHojas.remove(h)
			else:
				listaInterpsVerdaderas.append(h)
				listaHojas.remove(h)
		else:
			clasifica_y_extiende(x, h)

	return listaInterpsVerdaderas


f = Inorder2Tree('(pYq)')

h = [f, Inorder2Tree('-q')]

listaHojas = [h]

clasifica_y_extiende(f, h)

imprime_listaHojas(listaHojas)