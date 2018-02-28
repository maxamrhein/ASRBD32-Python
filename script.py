#!/usr/bin/python3.6.4

'''
a=10
b=5
print(a+b)
'''

#python script.py (pour lancer le script depuis CMD)


'''
age = "je suis max"
print (age)

txt = "Hello World"
print (len(txt))

prenom = "MAX"
print ("Bonjour, je m'appelle %s"  % (prenom))
'''

'''
maListe = []
print (type(maListe))
maListe = [1,2,3]
maListe.append("Quatre") #  .append permet d'ajouter à la fin de la liste
print (maListe)

print (maListe.count("Quatre")) #renvoie 1 car il n'y a qu'un "Quatre" dans maListe

print("Quatre" in maListe) #renvoie True car "Quatre" est dans maListe
'''

'''
monTuple = ()                #comme une liste mais non modififable (constante)
print (type(monTuple))
monTuple = ("toto")      
print (type(monTuple))
monTuple[1] = "error"
'''
'''
a = "yo"
c = 5
def test():
	b = "test"
	print (c)

test()
print (a, b)
'''

'''
from random import *

def jeu():
	mystere = randint(0, 100) 
	print ("devinez le nombre entre 0 et 100")
	print ("Entrer un nombre : ")
	nombre = int (input())        
	while (nombre != mystere):  
		if (nombre < mystere):
			print ("trop petit")  
		else:
			print ("trop grand")     
    		nombre = int (input())
print ("Bravo vous avez trouvé le bon numero ")


jeu()
'''

'''
class Voiture:
	def __init__(self):
		self.nom = "Ferrari"
		self.origine = "Italie"

ma_voiture = Voiture()
print (ma_voiture.nom)
print (ma_voiture.origine)
'''

'''
import socket

ip = socket.gethostbyname(socket.gethostname())
print (ip)
'''

import os
subnet = "10.94.45." 
for i in range(1, 255):
    hostname = subnet + str(i)
    response = os.system("ping -n 1 " + hostname)
    if response == 0:
    	print(hostname, 'is up!')