#4. Pide por teclado una direccion y muestra cuantos accidentes se han producido de ese tipo.

import json
with open('resumen-accidentes-2015.json') as data_file:
	data = json.load(data_file)

direccion = raw_input("Introduce un nombre de calle: ")
direccion = direccion.upper()

numero = raw_input("Introduce un numero de la calle anterior: ")
tipos = []
contador = 0

for accidentes in data:
	if accidentes["TIPO DE ACCIDENTE"] not in tipos:
		tipos.append(accidentes["TIPO DE ACCIDENTE"])

for tipo in tipos:
	if tipo == "":
		tipo = 	"SIN TIPO"
	for accidentes in data:
		if tipo == accidentes["TIPO DE ACCIDENTE"] and direccion == accidentes["CALZADA 1"] and numero == accidentes["NUMERO"]:
			buscado = tipo

for tipo in tipos:
	for accidentes in data:
		if buscado == accidentes["TIPO DE ACCIDENTE"]:
			contador = contador + 1

print "El tipo de accidente ocurrido en esa calle fue: "+buscado+" y en 2015 se produjeron %d accidentes mas de ese tipo."%(contador -1)