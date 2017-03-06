#5. Pide por teclado un tipo de herido (ilesos, leves , graves o muertos) y un numero minimo y muestra los accidentes con el numero indicado de heridos de ese tipo,
import json
with open('resumen-accidentes-2015.json') as data_file:
	data = json.load(data_file)

herido = raw_input("Introduce un tipo de herido: ")
herido = herido.upper()
minh = (raw_input("Introduce un minimo de heridos: "))


for accidentes in data:
	if accidentes[herido] >= minh :
		print "HORA: "+accidentes["HORA"]
		print "CALZADA 1: "+accidentes["CALZADA 1"]
		print "NUMERO: "+accidentes["NUMERO"]
		print "CALZADA 2: "+accidentes["CALZADA 2"]
		print "TIPO DE ACCIDENTE: "+accidentes["TIPO DE ACCIDENTE"]
		print "ILESOS: "+accidentes["ILESOS"]
		print "LEVES: "+accidentes["LEVES"]
		print "GRAVES: "+accidentes["GRAVES"]
		print "MUERTOS: "+accidentes["MUERTOS"]
		print "NUMERO DE PEATONES: "+accidentes["NUMERO DE PEATONES"]
		print "NUMERO DE VEHICULOS: "+accidentes["NUMERO DE VEHICULOS"]
		print


