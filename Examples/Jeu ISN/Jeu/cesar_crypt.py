from tkinter import *
import Algorithme_fichier_de_niveau_action
global var_texte1, var_texte2, var_texte3, var_texte4


def valider():
    var_texte1 = ligne_texte1.get()
    var_texte2 = ligne_texte2.get()
    var_texte3 = ligne_texte3.get()
    var_texte4 = ligne_texte4.get()
    if var_texte1=="Jour 302." and var_texte2=="largage prevu vendredi," and var_texte3=="poche de resistance decouverte," and var_texte4=="leur QG : vieille eglise. A nettoyer.":
        print("décodé")
        Algorithme_fichier_de_niveau_action.confirmation = True
        Algorithme_fichier_de_niveau_action.mort()


fenetre = Tk()
cadre = Frame(fenetre, width=500, height=100, borderwidth=1)
cadre.pack(fill=BOTH)

champ_label = Label(fenetre, text="Glro 302.\n ixodxdb mobsr sbkaobaf,\n mlzeb ab obpfpqxkzb abzlrsboqb,\n ibro ND : sfbfiib bdifpb. X kbqqlvbo.")
champ_label.pack()


#w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()
#fenetre.overrideredirect(1)
#fenetre.geometry("%dx%d+0+0" % (w, h))


# Image de fond
photo = PhotoImage(file="data/image/others/cesar.gif")

# CrÃ©ation d'un widget Canvas (zone graphique)
Largeur = 440
Hauteur = 186
Canevas = Canvas(fenetre,width = Largeur, height =Hauteur)
item = Canevas.create_image(0,0,anchor=NW, image=photo)
print("Image de fond (item",item,")")
Canevas.pack()

var_texte1 = StringVar()
ligne_texte1 = Entry(fenetre, textvariable=var_texte1, width=50)
ligne_texte1.pack()

var_texte2 = StringVar()
ligne_texte2 = Entry(fenetre, textvariable=var_texte2, width=50)
ligne_texte2.pack()

var_texte3 = StringVar()
ligne_texte3 = Entry(fenetre, textvariable=var_texte3, width=50)
ligne_texte3.pack()



var_texte4 = StringVar()
ligne_texte4 = Entry(fenetre, textvariable=var_texte4, width=50)
ligne_texte4.pack()

bouton_quitter = Button(fenetre, text="verifier", command= valider)
bouton_quitter.pack()





fenetre.mainloop()