import csv
fname = r"C:\users\m.natile\a.txt"
people_fname = r"C:\users\m.natile\a.txt" #file fixture deve essere
outfname = r"C:\users\m.natile\a.txt"
with open(people_fname, "rb") as fpeople:

class DebugExporter(object):
	def do_export(self,f,rows)    #f = file rows = assumiamo essere una lista di righe di database
		for row in rows:
			#f.write("{}\n".format(row))
			print("{}\n".format(row))
			
class Exporter(object):
	def do_export(self,f,rows):    #f = file rows = assumiamo essere una lista di righe di database
		for row in rows:
			f.write("{}\n".format(row))

import json

class JsonExporter(object):
	def do_export(self,f,rows) :   
		json.dump(rows,f, indent=2)



class CsvExporter(object):
	def do_export(self,f,rows) :   
		fieldnames = rows[0].keys()
        writer = csv.DictWriter(f, fieldnames = fieldnames, delimiter = ";")

        writer.writeheader()
        
        for row in rows:
            writer.writerow(row)
		
xp = CsvExporter()
l2 =[1,2,3,4,10,200,30]
#xp.do_export(None, rows=l2)
with open(outfname, "ab") as f:
	xp.do_export(f, rows=PEOPLE)