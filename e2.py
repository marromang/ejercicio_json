import json
with open('resumen-accidentes-2015.json') as data_file:
	data = json.load(data_file)

#2. Muestra los tipos de accidente y cuantos hay de cada tipo.
tipos = []
contador= 0

for accidentes in data:
	if accidentes["TIPO DE ACCIDENTE"] not in tipos:
		tipos.append(accidentes["TIPO DE ACCIDENTE"])
		

for tipo in tipos:
	if tipo == "":
		tipo = 	"SIN TIPO"
	for accidentes in data:
		if tipo == accidentes["TIPO DE ACCIDENTE"]:
			contador = contador + 1
	print tipo, contador

