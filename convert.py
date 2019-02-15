import csv
from io import open
with open('/home/hanl9/Downloads/csv/index_keywords_spaced_1.csv','r', encoding='ISO-8859-1') as csvin, open('/home/hanl9/Downloads/csv/controlled_vocabulary_spaced_1.txt', 'w') as tsvout:
    csvin = csv.reader(csvin)
    tsvout = csv.writer(tsvout, delimiter='\t')

    for row in csvin:
        tsvout.writerow(row)
