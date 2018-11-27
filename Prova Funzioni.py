#Programma con Funzioni differenti.

import random #Libreria per creare un numero random nel dado
import math #Libreria Matematica per calcolo raggio sfera

#Funzione Salute
def Benvenuto():
    print ('Ciao! Il mio nome e Carmine')
    print ('E questo e un esercizio su come creare le funzioni!!')
    print ('In questo esercizio vedremo più esempi di funzioni in un unico programma!!')
    print ('|------------------------------------------------------------------------|')

#Funzione IF
def IF (voto):
     if voto<6:
       print ("Bocciato!!")
     elif voto<8:
       print ("Potevi fare di meglio,NABBOH!!")
     else:
       print ("Promosso!!")

#Funzione Massimo
def Massimo (N,M,i):
    i=0

    while i<9:
        N = input ('inserisci il valore: ')
        N = int(N)
        if N>M:
            M=N
        i += 1
            
    print ('il valore più alto inserito è: ' + str(M))

#Funzione Area Rettangolo
def AreaR (h,b):
    return h * b


#Funzione While
def While(A):
    while A<10:
        print(A)
        A += 1

#Funzione Random Dado
def LancioDado():
	return random.randint(1,6)

#Funzione Somma
def somma(a,b):
    return a + b

#Funzione Sfera
def sfera(r): 
    Volume= (r**3*math.pi*4./3.)
    return Volume




#Main Benvenuto
Benvenuto()

print ('|-------------------------------------------|')
print ('|-------------------------------------------|')


#Main IF
voto = input('inserisci voto: ')
voto = int(voto)
IF(voto)

print ('|-------------------------------------------|')


#Main Massimo
N = input ('inserisci 1° valore: ')
N = int(N)
M = N
i=0
Massimo(N,M,i)

print ('|-------------------------------------------|')


#Main Area Rettangolo
h = input ("Inserisci il valore dell'Altezza(h): ")
h = int(h)

b = input ("Inserisci il valore della Base(b): ")
b = int(b)

AreaRettangolo = AreaR(h,b)
print ("Il valore dell'area del Rettangolo è: " + str(AreaRettangolo))

print ('|-------------------------------------------|')


#Main While
A=0
While(A)

print ('|-------------------------------------------|')


#Main Dado
print ("Lancia un dado di 6 faccie: ")
print ("|----------------------------|")

print ("Il Numero uscito dal lancio del dado è: " + str(LancioDado()))

print ('|-------------------------------------------|')


#Main Somma
a = input ('Inserisci il 1° Numero: ')
a = int(a)

b = input ('Inserisci il 2° Numero: ')
b = int(b)

Somma1 = somma(a,b)
print (Somma1)

print ('|-------------------------------------------|')


#Main Sfera
r = input('Quanto vale il raggio?  ')
r = int(r)
print (sfera(r))

print ('|-------------------------------------------|')
print ('|-------------------------------------------|')

    
