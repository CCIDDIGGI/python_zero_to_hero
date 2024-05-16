# Supponete di avere una lista di stringhe in cui alcune di esse (non necessariamente tutte)
# iniziano e terminano con il carattere di doppio apice.

# Quali istruzioni utilizzereste su ciascun elemento per eliminare solo i doppi apici?
# Quali istruzioni potreste utilizzare per trovare la posizione dell'ultima "p" di Mississipi?
# Quando avete trovato tale posizione, quali istruzioni utilizzereste per eliminare solo l'ultima lettera?

x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']

for index, str in enumerate(x):
    x[index] = str.replace('"', '')

y = "Mississipi"

print(y.rindex("p"))

y = y[:-1]

print(y)