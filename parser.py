import os
import pprint

from csv_parser import CSVParser


pp = pprint.PrettyPrinter(indent=4)

CSV_FILES_DIR = os.path.join(os.path.dirname(__file__), 'csv_files')

file_names_to_display = ('1.csv', '2.csv', '3.csv')


for file_name in file_names_to_display:
    print "Results for {}:".format(file_name)

    with open(os.path.join(CSV_FILES_DIR, file_name)) as f:
        pp.pprint(CSVParser(f).parse())

    print "-----------------------------------------------"

