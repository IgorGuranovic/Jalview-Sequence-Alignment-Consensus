import csv, re, os
import numpy as np
import pandas as pd

with open('file.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

with open ('sequence.txt', "r") as text:
    text = text.read()

precision = data[0][1:-1]
indicator = data[1][1:-1]

letters = []

for element in indicator:
    letters.append(element[1])

temp = list(range(len(text)))
vals = [m.start() for m in re.finditer('-', text)]
indices = [x for x in temp if x not in vals]

precise = []
amino_acid = []

for number in indices:
    precise.append(precision[number])
for number in indices:
    amino_acid.append(letters[number])

sequence = text.replace('-','')

consensus = ''
for element in amino_acid:
    consensus = consensus + element

new = []
new_indices = []
new_precise = []

for index in range(len(consensus)):
    if consensus[index] == sequence[index]:
        new_indices.append(index)
        new.append(consensus[index])
        new_precise.append(precise[index])

new_precise1 = []
for element in new_precise:
    new_precise1.append(float(element))
sorted_indices = np.argsort(new_precise1)
sorted_indices = np.flip(sorted_indices)

final = []
final_indices = []
final_precise = []
final_letters = []
final_abbrev = []



for i in range(len(sorted_indices)):
    final_indices.append(new_indices[sorted_indices[i]]+1)
    final.append(new[sorted_indices[i]])
    final_precise.append(str(new_precise[sorted_indices[i]]) + "%")

for element in final:
    if element == 'A':
        final_letters.append('Alanine')
    elif element == 'C':
        final_letters.append('Cysteine')
    elif element == 'D':
        final_letters.append('Aspartic acid')
    elif element == 'E':
        final_letters.append('Glutamic acid')
    elif element == 'F':
        final_letters.append('Phenylalanine')
    elif element == 'G':
        final_letters.append('Glycine')
    elif element == 'H':
        final_letters.append('Histidine')
    elif element == 'I':
        final_letters.append('Isoleucine')
    elif element == 'K':
        final_letters.append('Lysine')
    elif element == 'L':
        final_letters.append('Leucine')
    elif element == 'M':
        final_letters.append('Methionine')
    elif element == 'N':
        final_letters.append('Asparagine')
    elif element == 'P':
        final_letters.append('Proline')
    elif element == 'Q':
        final_letters.append('Glutamine')
    elif element == 'R':
        final_letters.append('Arginine')
    elif element == 'S':
        final_letters.append('Serine')
    elif element == 'T':
        final_letters.append('Threonine')
    elif element == 'V':
        final_letters.append('Valine')
    elif element == 'W':
        final_letters.append('Tryptophan')
    elif element == 'Y':
        final_letters.append('Tyrosine')
    else:
        final_letters.append('Error')

for element in final:
    if element == 'A':
        final_abbrev.append('Ala')
    elif element == 'C':
        final_abbrev.append('Cys')
    elif element == 'D':
        final_abbrev.append('Asp')
    elif element == 'E':
        final_abbrev.append('Glu')
    elif element == 'F':
        final_abbrev.append('Phe')
    elif element == 'G':
        final_abbrev.append('Gly')
    elif element == 'H':
        final_abbrev.append('His')
    elif element == 'I':
        final_abbrev.append('Ile')
    elif element == 'K':
        final_abbrev.append('Lys')
    elif element == 'L':
        final_abbrev.append('Leu')
    elif element == 'M':
        final_abbrev.append('Met')
    elif element == 'N':
        final_abbrev.append('Asn')
    elif element == 'P':
        final_abbrev.append('Pro')
    elif element == 'Q':
        final_abbrev.append('Gln')
    elif element == 'R':
        final_abbrev.append('Arg')
    elif element == 'S':
        final_abbrev.append('Ser')
    elif element == 'T':
        final_abbrev.append('Thr')
    elif element == 'V':
        final_abbrev.append('Val')
    elif element == 'W':
        final_abbrev.append('Trp')
    elif element == 'Y':
        final_abbrev.append('Tyr')
    else:
        final_abbrev.append('Error')

display = [final_indices, final, final_abbrev, final_letters, final_precise]
df = pd.DataFrame(display)
df.to_csv(os.path.join('output.csv'), sep=',', header=None, index=None)