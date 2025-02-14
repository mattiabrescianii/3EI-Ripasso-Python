#Il gioco dell'impiccato
#Scrivi un programma che simula il gioco dell'impiccato con le seguenti funzionalità:
# -Il programma deve selezionare una parola casuale da un elenco di parole presenti in un file
# -La parola scelta deve essere mostrata all'utente come una serie di trattini (ad esempio: "_ _ _ _ _ _").
# -Il giocatore ha un numero limitato di 6 tentativi (che corrispondono agli errori) per indovinare la parola. Il giocatore perde un tentativo quando fa un errore, mentre quando fa giusto si prosegue
# -Se il giocatore indovina tutte le lettere della parola il programma deve stampare un messaggio di vittoria.
# -Se il numero di tentativi arriva a zero, il programma deve stampare un messaggio di sconfitta e rivelare la parola.

import random

def carica_parole(random_parol.csv):    #Carica tutte le parole da un file e le restituisce come lista.
    f=open("random_parol.csv" 'r')
    rig = 0
    parola = f.readline()
    while riga != "":
        rig += 1
        parola = f.readline()
    f.close()

def scegli_parola_random(parole):   #Seleziona casualmente una parola dalla lista.
    return random.choice(parole)

def indovina_parola(parola):
    lettera = len(parola)
    tentativi = 6
    while tentativi != 0:
        risposta = input("inserisci una lettera che credi possa essere dentro la parola da indovinare: ")
        if risposta.lower() = lettera.lower():
            print(" bravo, hai indovinato una lettera ")
        else:
            tentativi -= 1
            print( "sbagliato hai ancora", tentativi, "tentativi")
    prnt("hai esaurito i tentativi, la parola era:", parola)

        

