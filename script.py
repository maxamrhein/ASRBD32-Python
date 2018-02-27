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
    print "Entrez un nombre : "
    nombre = int (input())

print ("Bravo vous avez trouvé le bon numero ")


jeu()