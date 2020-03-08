#------------Le Jeu du Serpent par Mathias FLAGEY dans le cadre du projet "Le Repère des G@mers", ISN 2018-----------


#coding:utf-8
#-----------Import des modules----------
from tkinter import * #tkinter pour le traitement graphique
from random import * 
import winsound #winsound pour la musique

#-----------Musique---------- 
winsound.PlaySound('son1.wav', winsound.SND_LOOP | winsound.SND_ASYNC) #Active la musique en boucle (loop) et en arriere plan (async)

#-----------Fonctions-----------
#Fonction prenant en compte le deplacement, et les colisions du serpent
def mouvement():
    global a,b,z,y,lx,ly,j,serpent,score
    c=len(serpent)
    c=c-1
    while c!=0:
        lx[c]=lx[c-1]
        ly[c]=ly[c-1]
        c+=-1

    lx[0]+=a #(voir fonction haut,bas,gauche droite)
    ly[0]+=b #(idem)
    c=0
        #On applique les nouvelles coordonnées aux carrés correspondant
    while c!=len(serpent):
        maps.coords(serpent[c],lx[c],ly[c],lx[c]+20,ly[c]+20)
        c+=1
    c=1
     #Collision du serpent avec lui même
    while c!=len(serpent):
        if lx[c]==lx[0] and ly[c]==ly[0]:
            j=1
            mort()#L'écran de game over est lancé
            
            break
        c+=1
    #Interaction avec les bordures de la map (Avec d permettant d'éviter un bug lors du changement de coordonnées)
    d=1
    if lx[0]>=400:
        lx[0]=20
        d=0
    if lx[0]<=0 and d==1:
        lx[0]=400
    if ly[0]>=400:
        ly[0]=20
        d=0
    if ly[0]<=0 and d==1:
        ly[0]=400
    d=0
    #Interactions avec la nourriture
    if z-14<=lx[0]<=z+14 and y-14<=ly[0]<=y+14:
        score+=1
        scores.set(str(score*10))
        snake()
    if j!=1:
        fen.after(100,mouvement)#On lance la fonction mouvement toutes les 100 millisecondes pour faire avancer le serpent
        
    
#Fonction qui permet d'agrandir le serpent lorsqu'il mange un fruit
def snake():
    global a,b,lx,ly,z,y,n #z et y sont des variables aléatoires qui permettent de gérer la position de la nourriture independemment de celle du serpent.
    z=randrange(2,18)
    y=randrange(2,18)
    z = z*10
    y = y*10
    maps.coords(miam,z,y,z+20,y+20)
    serpents = maps.create_oval(500,500,510,510,fill='green')#Serpent généré hors de la map pour éviter des bugs
    serpent.append(serpents)
    lx.append(lx[n]+12+a)
    ly.append(ly[n]+12+b)
    n+=1


#Haut, bas, gauche, droite
    #Ces fonctions modifient les variables a et b pour influencer la direction et le sens du mouvement
def haut(event):
    global a,b,s, bstart
    bstart.destroy()
    a=0
    b=-20
    if s==0:
        s=1
        mouvement()
                                                                                                                          
   
    
def bas(event):
    global a,b,s,bstart
    bstart.destroy()
    a=0
    b=20
    if s==0:
        s=1
        mouvement()

def gauche(event):
    global a,b,s,bstart
    bstart.destroy()
    a=-20
    b=0
    if s==0:
        s=1
        mouvement()
      
def droite(event):
    global a,b,s,bstart
    bstart.destroy()
    a=20
    b=0
    if s==0:
        s=1
        mouvement()
        
#Pour sortir du menu principal et lancer le jeu.
def lancement():
    
    accueil.destroy()
    blancer.destroy()
    bstart.grid(row=1,column=3,columnspan=5)
    Label(fen, text='Score:  ', bg='green', font='Impact').grid(row=0,column=0)
    Score.grid(row=0,column=1)
    
#Lorsque le joueur perd: on affiche son score, l'écran de game over et les boutons quitter et recommencer.
def mort():
    global score
    score= 'Game over! \n Vous avez \n' + str(score*10)+'points!'
    scores.set(score)
    ecran_mort.grid(row=1,column=0,columnspan=3)
    brecommencer.grid(row=1,column=0,columnspan=3)
    bquitter.grid(row=1, column=0)
    
#Si le joueur veut recommencer une partie
def restart():
    global z,y,lx,ly,score,serpent,j,m,s,n,a,b,miam,bstart,brecommencer,bquitter,ecran_mort
    #On detruit tout    
    brecommencer.destroy()
    bquitter.destroy()
    ecran_mort.destroy()
    maps.delete(ALL)
    #on recréé les variables
    ecran_mort=Canvas(fen,width=400, height=400,bg='green')
    ecran_mort.create_image(200,200, image=image_mort)
    brecommencer=Button(fen, text='Recommencer', command=restart, font='impact', bg='lightgrey', foreground='green', activebackground='lightgrey', activeforeground='darkgreen')
    bquitter=Button(fen, text='Quitter le jeu', font='Impact', command=quitter, bg='lightgrey', foreground='green', activebackground='lightgrey', activeforeground='darkgreen')
    bstart=Label(fen, text= 'Appuyer sur une touche \n de direction pour commencer!', font='Impact')
    #On reaffiche l'ecran de debut
    bstart.grid(row=1,column=3,columnspan=5)
    s=score=j=m=t=a=b=0
    z=y=50
    lx,ly,serpent = [100,110],[100,110],[] 
    n=1
    maps.create_image(200,200,image=image_map)
    serpent_tete= maps.create_oval(100,100,110,110,fill='green') #(x0,y0,x1,y1 , couleur)
    serpent_corps= maps.create_oval(110,100,120,110,fill='dark green')
    serpent.append(serpent_corps)
    serpent.append(serpent_tete)
    miam=maps.create_oval(z,y,z+20,y+20,fill='orange')
    
    
    scores.set('0')

#Si le joueur décide de quitter le jeu 
def quitter():
    maps.destroy()
    fen.destroy()
    winsound.PlaySound('son2.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)

def checkmusique():#Le son2 est un court enregistrement silencieux simplement pour éviter qu'un bruit Windows soit émis lorsqu'on éteint la musique
    global bmusique,etatmusique
    if etatmusique.get()==0:
        winsound.PlaySound('son1.wav', winsound.SND_LOOP | winsound.SND_ASYNC)
    elif etatmusique.get()==1:
        winsound.PlaySound('son2.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        
        
    

#-----------Variables-----------

s=score=j=m=t=a=b=0
z=y=50
lx,ly,serpent = [100,110],[100,110],[] #lx contient les cordonnées x0,x1 et
                                        #ly contient les coordonnées yo,y1
n=1

#Création de la fenêtre de jeu
fen=Tk()
fen.title("ISN 2018 : Le jeu du serpent")
fen.resizable(width=False, height=False)
fen.minsize(650,500)
fen.overrideredirect(1) #On fait disparaitre les boutons croix, réduire et cacher.
    #On centre la fenêtre de jeu sur l'écran du joueur en prenant en compte ses résolutions.
screen_x= int(fen.winfo_screenwidth())#On récupère la largeur de l'écran du joueur.
screen_y= int(fen.winfo_screenheight())#On recupère la hauteur de l'écran du joueur.
window_x=650 
window_y=500
posX= (screen_x//2)-(window_x//2)
posY= (screen_y//2)-(window_y//2)
geo="{}x{}+{}+{}".format(window_x, window_y, posX, posY)#On crée la variable geo pour centrer la fenêtre de jeu avec les données récupérées.
fen.geometry(geo)#On applique les modifications à la fenêtre.

#-----------Images-----------
image_accueil= PhotoImage(file='img1.gif') #sources: serpent sur un blog, arriere plan: le chateau ambulant miyazaki
image_map= PhotoImage(file='img2.gif') #Source: photo de gazon avec effet ombre
image_mort= PhotoImage(file='img3.gif')

#Création du canevas (de la map)
maps=Canvas(fen,width=400, height=400,bg='green')
maps.create_image(200,200,image=image_map)
maps.grid(row=1,column=0,columnspan=3)
maps.focus_set()

#création de l'accueil 
accueil=Canvas(fen,width=400, height=400,bg='green')
accueil.create_image(200,200,image=image_accueil)
accueil.grid(row=1,column=0,columnspan=3)
blancer=Button(fen, text= 'Lancer le jeu!', command=lancement,bg='green',activebackground='dark green', font='Impact')
blancer.grid(row=1,column=0)

#ecran de mort
ecran_mort=Canvas(fen,width=400, height=400,bg='green')
ecran_mort.create_image(200,200, image=image_mort)

#Design serpent
serpent_tete= maps.create_oval(100,100,110,110,fill='green') #(x0,y0,x1,y1 , couleur)
serpent_corps= maps.create_oval(110,100,120,110,fill='dark green')
serpent.append(serpent_corps)
serpent.append(serpent_tete)

#Design nourriture
miam=maps.create_oval(z,y,z+20,y+20,fill='orange')

#Controles    
maps.bind('<Up>', haut)
maps.bind('<Down>',bas)
maps.bind('<Left>',gauche)
maps.bind('<Right>',droite)

#Boutons
bstart=Label(fen, text= 'Appuyer sur une touche \n de direction pour commencer!', font='Impact')
bquitter=Button(fen, text='Quitter le jeu', font='Impact', command=quitter, bg='lightgrey', foreground='green', activebackground='lightgrey', activeforeground='darkgreen')
brecommencer=Button(fen, text='Recommencer',command=restart, font='impact', bg='lightgrey', foreground='green', activebackground='lightgrey', activeforeground='darkgreen')
#Petit bouton pour gérer la musique
etatmusique= IntVar()
bmusique= Checkbutton(fen, text="Musique", onvalue=0, offvalue=1,command=checkmusique, indicatoron=0,variable=etatmusique,  font='impact', bg='red', selectcolor='green',activebackground='blue')
bmusique.grid(row=2, column=3)


#Score
scores = StringVar()
Score = Label(fen, textvariable=scores, background='green', font='Impact')
scores.set('0')


#Aide à la programation
#def pointeur(event):
    #chaine.configure(text = "Clic détecté en X =" + str(event.x) +\
    #                        ", Y =" + str(event.y))
#accueil.bind("<Button-1>", pointeur)
#chaine = Label(fen)
#chaine.grid(row=2,column=0,columnspan=3) 

fen.mainloop()
