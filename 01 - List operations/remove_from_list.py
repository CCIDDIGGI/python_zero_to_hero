# 1 [Operazioni sulle liste] 
# Se avete una lista x, scrivete il codice necessario per 
# eliminare in sicurezza un elemento se, e solo se, tale valore è presente nella lista.
# Modificare il codice in modo che elimini l'elemento solo se si presenta più volte all'interno della lista

x = [0, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9]

x.remove(2)

print(x)

y = x

# se esiste più di un elemento 3 entra nel corpo della condizione
if(y.count(3) > 1):
    # cancella la prima occorrenza trovata
    y.remove(3) 

print(y)

