# -*- coding: utf-8 -*-
import random
from tkinter import *


#------définition des fonctions-------------------------

def canevas_debut():
    global nb_lignes
    global nb_colonnes
    global dos_carte
    canvas.delete(ALL)
    liste_ids=[]
    for colonne in range (nb_colonnes):
        for ligne in range (nb_lignes):
            liste_ids.append(canvas.create_image( 150*colonne+100,120*ligne+100, anchor=CENTER, image = dos_carte, tags="cartes",))
    return liste_ids
    
    
def apparition_images():
    
    global nb_total_cartes
    global nb_images
    global images
    nb_images= 1+nb_total_cartes // 2
    images = []
    
    for i in range (nb_images):
        
        images.append(PhotoImage(file="image{}.gif".format(i)))

    return images
        
def suppression_carte():
    global id_carte1
    global id_carte2
    global nb_cartes_trouvees
    global clics_a_zero
    global nb_total_cartes
    global fin_du_game
    
    canvas.delete(id_carte1)
    canvas.delete(id_carte2)
    
    nb_cartes_trouvees += 2
    
    if nb_cartes_trouvees == nb_total_cartes:
        fin_du_game()
    else :
        clics_a_zero()
    return fin_du_game

def valeur_de_carte (id_carte):
    
    index= liste_id_cartes.index(id_carte)
    
    return cartes_melangees[index]

def affichage_carte(id_carte):
    
    canvas.itemconfigure(id_carte, image=images[valeur_de_carte(id_carte)])


def disparition_cartes ():
    
    canvas.itemconfigure("cartes", image = dos_carte)
    clics_a_zero()
                                                
def melanger_les_cartes ():
    global nb_images
    liste=  list(range(1, nb_total_cartes//2+1))*2
    
    random.shuffle(liste)
    
    return liste


def pareil (id1, id2):
    
    return bool(valeur_de_carte(id1) == valeur_de_carte(id2))

def clics_souris (event):
    global id_carte1
    global id_carte2
    global affichage_carte
    global supprimer_cartes
    x = event.x
    y = event.y
    trouver=canvas.find_overlapping(x,y,x,y)

    if trouver and trouver[0] in liste_id_cartes:
        id_carte = trouver[0]
        
        if id_carte1 == 0:
            
            id_carte1 = id_carte
            id_carte2 = 0

            affichage_carte(id_carte1)

        elif id_carte2 == 0 and id_carte != id_carte1:
            id_carte2 = id_carte
            affichage_carte(id_carte2)
            if pareil(id_carte1, id_carte2):
                fenetre.after(delai, suppression_carte)
            else:
                fenetre.after(delai, disparition_cartes)
            
        

def clics_a_zero ():
    global id_carte1, id_carte2
    id_carte1 = id_carte2 = 0

def jeu():
    
    global cartes_melangees, liste_id_cartes
    global nb_cartes_trouvees
    liste_id_cartes = canevas_debut()
    cartes_melangees = melanger_les_cartes()
    nb_cartes_trouvees = 0
    clics_a_zero()
    return nb_cartes_trouvees

def fin_du_game ():
     
    canvas.delete(ALL)

    x=canvas.winfo_reqwidth()//2
    y= canvas.winfo_reqheight()//2

    canvas.create_text(x,y,text="Felicitations! vous avez fini votre partie! \n Vous pouvez daber pour fêter ça", font="Times 25 bold", fill="dark red")
    canvas.create_window(x,y+60,window=Button(canvas,text="Recommencer", command= jeu),)


#------Variables--------------------------------------

nb_lignes = 5
nb_colonnes = 4
nb_total_cartes = nb_lignes * nb_colonnes
delai=800

#------Programme pincipal-------------------------------

#mise en place de la fenêtre principale du jeu
fenetre= Tk()
fenetre.title("ISN 2018 , Le jeu de Memoire")
fenetre.resizable(width=False, height=False)

#images contient toutes les images des cartes

images = apparition_images()
dos_carte= images [0]


#debuter le canvas graphique
canvas = Canvas(fenetre, width=650, height=700)

canvas.pack()

jeu()

canvas.bind('<Button-1>',clics_souris)

Button(fenetre,text='Quitter',command=fenetre.destroy).pack(side =LEFT, padx=10, pady=10)

fenetre.mainloop()
