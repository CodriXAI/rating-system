#Rangos que tomo en cuenta, Mala (1-30), Regular (40-50), Buena (60-80), Excelente (90-100):
 
#Modules

def print_data(dataBase : list[tuple[str, int]]) -> str:
	"""
	Print Data 
	==========
	Allows you to print the database listed and in vertical format

	Parameters 
	----------
		dataBase: (Tuple List)
			Contains name and rating information for each product

	Return
	------
		str (data)
		
	"""
	for i, (name, data) in enumerate(dataBase, start=0): #Tengo que utilizar Enumerate para poder indicarle el índice de inicio al For
		print(f"{i+1}. '{name}' - {data}")

def average_data(dataBase : list[tuple[str, int]]) -> str:
	"""
	Average data
	============

	Allows you to evaluate the average number of reviews given a database

	Parameters
	----------
		dataBase: (Tuple List)
			Contains name and rating information for each product
	
	Return
	------
		str (average)
	"""
	if(not(dataBase)):
		print("Lista vacía, no hay datos para mostrar")
	else:
		bad = regular = good = excelent = 0
		for _,i in dataBase:
			if(i >= 1 and i <= 30):
				bad+=1
			elif(i >= 40 and i <= 50):
				regular+=1
			elif(i >= 60 and i <= 80):
				good+=1
			else:
				excelent+=1
		rate = [("bad",bad),("regular",regular),("good",good),("excelent",excelent)]
		print("Cantidad de Productos: ",len(dataBase))
		for name,value in rate:
			print(f"Promedio de '{name}' es de: ", value / len(dataBase))  		

def search(dataBase :  list[tuple[str, int]]) -> str:
	"""
	Search
	======

	Allows you to ask the user if they want to search for an item in the database.

	If yes, [Y, y] will perform a full search of the list looking for a match.

	If it finds one, it will say yes, print it, tell you what position it was in, and how many times it occurs.
	
	If no, [otherwise] will skip the entire process.

	Parameters
	---------- 
		dataBase (Tuple List)
			Contains name and rating information for each product
			
	Return
	------
		str (product)
	"""
	found = False
	count = 0
	option = input("¿Desea realizar alguna búsqueda en la Base de Datos? [Y = Yes / Otherwise = No]: ").lower()
	if(option == 'y'):
		dataSearch = input("Ingrese nombre de producto a buscar:").lower()
		for i,(name,value) in enumerate(dataBase):
			if(name == dataSearch):
				found = True
				count+=1
				print(f"{i+1}. {name} - {value}")
		if(found):
			print("El Producto",dataSearch,"fue encontrado en cantidad:",count)
		else:
			print("El producto no fue encontrado")				 	
