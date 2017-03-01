import json
with open('resumen-accidentes-2015.json') as data_file:
	data = json.load(data_file)

#1. Lista la fecha, el tipo de accidente y numero de vehiculos involucrados.	
for accidentes in data:
	print accidentes["FECHA"]+" "+accidentes["TIPO DE ACCIDENTE"]+" " +accidentes["NUMERO DE VEHICULOS"]+"."
