#3. Pide por teclado una fecha y muestra los accidentes de ese dia, con sus caracteristicas.

import json
with open('resumen-accidentes-2015.json') as data_file:
	data = json.load(data_file)

date = raw_input("Introduce una fecha de 2015(dd/mm/aaaa): ")

error = False 

for accidentes in data:
	if date == accidentes["FECHA"]:
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
	else:
		error = True	

if error:
	print "No hubo accidentes ese dia."
