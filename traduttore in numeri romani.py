numrom = { #li scriviamo in ordine decrescente perchè i numeri romani iniziano con i numeri più grandi per poi finire a quelli più piccoli
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}

output = ""

num10 = int(input("Inserisci il numero intero da convertire (da 1 a massimo 100 compreso) >> "))
num10iniz = num10

if num10 < 0 or num10 > 100:
    print("")
elif num10 == 0:
    print("I romani non avevano idea di cosa fosse il numero 0, non lo avevano mai pensato, nascerà poi nel 628.")
else:
    for valore, simbolo in numrom.items(): #per ogni valore del dizionario che "sta" nel numero dato, scrivi il simbolo e sottraine il valore
        while num10 >= valore:
            output += simbolo
            num10 -= valore

    print(num10iniz ,"scritto in numeri romani è ", output)
