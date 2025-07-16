import time 
from modules import print_data, average_data, search

client_data = []
i = 1
bug = True

#Rating
while bug:
	size = int(input("Ingrese cantidad de reseñas a evaluar: "))
	if size<=0:
		print("Error, el valor debe ser natural")
	else:
		bug = False
#Loading Data
while i <= size:
	name = input(f"Ingresar nombre de producto Nro.{i}: ").lower()
	data = int(input(f"Ingresar reseña de producto Nro.{i} (1-100): "))
	if data <= 100 and data >= 1:
		client_data.append((name,data)) #Mostramos una tupla de pares con Nombre de producto y reseña
		i+=1
	else:
		print("Error: Valores asignados incorrectos, por favor intente nuevamente...")

print("Cargando base de datos...")
time.sleep(4)
print("Los datos obtenidos fueron los siguientes:")
print_data(client_data)
average_data(client_data)
search(client_data)
