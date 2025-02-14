import random
def Crea_Parola():
    f=open("parole.csv","r")
    parole=f.readlines()
    f.close()
    parola=random.choice(parole)
    return parola

def Indovina_Parola(parola,spazi):
    tentativi=6
    posizione=[]
    while tentativi>0:
        if "_" in spazi:
            lettera=input("Inseresci la lettera che vuoi provare: ")
            if lettera in parola:
                for count in range(len(parola)):
                    if parola[count]==lettera:
                        spazi[count]=lettera

                print("Hai indovinato la lettera! Adesso la parola è",str(",".join(spazi)))
            else:
                print("Mi dispiace hai sbagliato, riprova")
                tentativi-=1
        else:
            tentativi=0
    return spazi

def main():
    x=False
    print("Benvenuto al gioco dell'impiccato!")
    parola=Crea_Parola()
    spazi_parola="_ "*(len(parola)-1)
    spazi=spazi_parola.split(" ")
    print("La parola da indovinare è",spazi_parola," e hai un totale di 6 tentativi")
    if "_" not in Indovina_Parola(parola,spazi):
        print("Complimenti, hai vinto!")
    else:
        print("Peccato, hai perso")
       
main()

x=False
while x==False:
    rigioca=input("Scrivi 'Si' se vuoi rigiocare al gioco dell'impiccato o 'No' se vuoi terminare ")
    while rigioca != "Si" and rigioca != "No":
        rigioca=input("Errore! Scrivi 'Si' se vuoi rigiocare al gioco dell'impiccato o 'No' se vuoi terminare ")
    if rigioca=="Si":
        main()
    else:
        x=True
