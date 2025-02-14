f = open("primo.csv", "r")
lista = []
r = f.readline()
somma = 0
while r != '':
    lista.append(r.split(','))
    r = f.readline()
for i in range (len(lista)):
    riga = lista[i]
    somma = somma + int(riga[0])
    
print(somma)

f.close()
