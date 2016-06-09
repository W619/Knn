#Trabajo del 8B hecho por:
#Wilver Diaz Zamora
#Daniel Tehozol Tehozol
#Vianey Lent Perez Perez
import csv #Esta linea llama al modulo csv para leer archivos como si fueran tablas
import math #Importa funciones matematicas avanzadas
import operator #importa un conjunto de funciones para operadores intrinsecos
from colorama import init, Fore, Back, Style #modulo que permite imprimir textos en colores en la salida de la terminal o consola.

def cargarDataset(archivo, trainingSet=[]): #define la funcion para la carga del conjunto de datos
	with open(archivo, 'rb') as csvfile: #abre el archivo en modo binario como un cvsfile
	    lines = csv.reader(csvfile) #lee el archivo y guarda en lines
	    dataset = list(lines) #Guarda una indice de lines
	    for x in (dataset): #Declara un bucle que itera en la lista de dataset
	    	print(x) #imprime x
	    print("\n 	DataSet: "+str(len(dataset))) #imprime el numero de filas en el archivo
	    for x in range(len(dataset)-1): #Declara un bucle para recorrer las filas del archivo
	        for y in range(4): #Declara un bucle para recorre las columnas del archivo
	        	dataset[x][y] = int(dataset[x][y]) #guarda la columna en un arreglo
	        trainingSet.append(dataset[x]) #aniade un objeto a la lista

def euclideanDistance(instance1, instance2, length): #Define la funcion para la distancia euclidiana
	distance = 0 #Declara la distancia a cero
	for x in range(length): #Declara un bucle entre las instncia con tenidas y 
		distance += pow((instance1[x] - instance2[x]), 2) # incrementa distacia con el resultado de la diferencia al cuadrado
	return math.sqrt(distance) # obtiene la raiz cuadrada de distancia

def getNeighbors(trainingSet, testInstance, k): #declara la funcion para obtener a los vecinos en k
	distances = [] #declara la distancia como un arreglo
	length = len(testInstance)-1 #Obtiene numero de  variables de la instacicia de prueba
 	for x in range(len(trainingSet)): #Declara un buble para recorer las instancias
		dist = euclideanDistance(testInstance, trainingSet[x], length) #Calcula la distancia euclidiana en cada instacncia
		distances.append((trainingSet[x], dist)) #Aniade un objeto a la lista
	distances.sort(key=operator.itemgetter(1))#ordena de menor a mayor

	neighbors = [] #Declara un arreglo de vecinos
	for x in range(k): #Declara un bucle para los elementos de k
		neighbors.append(distances[x][0]) #Aniade un objetos a vecinos
		print("\n		Vecinos:  "+str(distances[x][0])) #Imprime los vecinos
	return neighbors #Retorna a los vecinos

def getResponse(neighbors): #Declara la funcion para obtener una respuesta
	classVotes = {} #Declara una variable para los votos
	for x in range(len(neighbors)): #Declara el bucle para recorrer a los vecinos en k
		response = neighbors[x][-1] #Guarda en respuesta a vecino de columna -1
		if response in classVotes: #Declara la condicion si
			classVotes[response] += 1 # Especifica la sentencia diferente de 1
		else: #Declara el caso contrarip
			classVotes[response] = 1 #Especifica la sentencia 1
	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True) #Clasifica los votos
	return sortedVotes[0][0] #Retorna la clasificacion de votos
	
def datos(): #Declara la funcion para datos
	newInstance = "" #Variable para la instacncias de tipo streen
	codHex = [] #Declara un arreglo para la nueva instancia
	while len(newInstance) < 4 or len(newInstance) > 4: #Aseguara que se obtengan 4 datos
		newInstance = raw_input("\nIngresa 4 datos, sin espacios o comas,donde \nprimer espacio: 1-suuny 2-overcast 3-rainy\nsegundo espacio: 1-hot 2-mild 3-cool \ntercer espacio: 1-high 2-normal \ncuarto espacio: 1-false 2-true \nRecuerda solo numeros\n\n 	: ") #imprime mensaje para obtener datso
	for x in range(0,4): #Bucle para obtener los datos
			codHex.append(int(newInstance[x])) #aniade los objetos a codhex
	return codHex #Retorna Codhex

def main(): #Define la funcion principal
	# prepare data
	trainingSet=[] #Declara arreglo
	cargarDataset('clima.data', trainingSet) #Obtiene los datos del archivo cvs
	#print(trainingSet)
	codHex = datos() #Invoca la funcion Datos y los guarda en codhex
	#print(codHex)

	predictions=[] #Declara un arreglo para la prediccion
	k = int(raw_input("\n 	Ingresa el valor k: \n Debe ser un numero impar mayor a 1\n\n 	: ")) #Obtenemos K
	neighbors = getNeighbors(trainingSet, codHex, k) #Invocamos la funcion vecinos para obtener a los vecinos
	result = getResponse(neighbors) #Se obtiene una respuesta de los vecinos
	predictions.append(result) #Aniadimos el resultado a predicion
	
	init(autoreset=True) #Inicializamos la funcion init como verdadera
	print(Fore.YELLOW + Back.BLUE + Style.BRIGHT + '\n 	> El elemento de prueba es de clase =' + repr(result)) #Imprimimos el resultado de knn 
main() # Termina la funcion main
