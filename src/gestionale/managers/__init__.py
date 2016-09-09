import json
import csv

import backends


BACKENDS_MAP = {
    "son": backends.JsonManager,
    "csv": backends.CsvManager
}


people_fname = r"C:\corsoPython\lessons-python4beginners\src\scripts\people_fixture.json"
with open(people_fname, "rb") as fpeople:
    PEOPLE = json.load(fpeople)
outfname = r"c:\Users\m.natile\a.txt"


# OLD: def apply_exportation(xp, fname, data):
# OLD: 
# OLD:     with open(fname, "wb") as f:
# OLD:         xp.do_export(f, rows=data)


def apply_exportation(xp, data):

    xp.do_export(rows=data)


def apply_exportation_from_file(fname, data):
    
    ext = fname[-3:]
    xp_klass = BACKENDS_MAP.get(ext, backends.FileManager)
    
    xp = xp_klass(f)
    # apply_exportation(xp, data)
    xp.do_export(data)



