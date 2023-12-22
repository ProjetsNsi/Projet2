from PyPDF2 import PdfReader
from tkinter import *

from TextSearch import *
document = PdfReader("Code_penal.pdf")
number_of_pages = len(document.pages)
texte = ""
for i in range (9,number_of_pages): # On enlève les 9 premières pages car elles sont inutiles et génantes
    page = document.pages[i]        # pour l'algorithme .
    text = page.extract_text()
    texte += text

def recherche_naif(motif):
    return recherche_n(motif,texte, globalindesirable)

def recherche_Boyer(motif):
    return recherche_bm(motif,texte,globalindesirable)




texteindesirable = "Legif.   \n Plan   \n Jp.C.Cass.   \n Jp.Appel   \n Jp.Admin.   \n Juricaf\n"
debutindesirable = positions_BM(texteindesirable, texte)
globalindesirable = []
for elt in debutindesirable:
   for i in range(len(texteindesirable)):
        globalindesirable.append(elt+i)

#creation des fonctions qui s'active lors de l'utilisation des boutons ( bouton_recherche_bm et bouton_recherche_naif )
def bouton_bm():
    mot = entry_mot.get()
    a = recherche_Boyer(mot)
    result_text.insert(END, a)

def bouton_naif():
    mot = entry_mot.get()
    b = recherche_naif(mot)
    result_text.insert(END, b)


#création d'une interface


#creation de la fenêtre

fenetre = Tk()
fenetre.title("NOM DE LA FENETRE")
fenetre.geometry(f"{800}x{400}")
fenetre.configure(background='#32404D')


#creation du titre et du sous titre

label_titre = Label(fenetre, text="RECHERCHE TEXTUELLE", font=("Helvetica", 40), bg = "#32404D", fg ="#00D5DB")
label_titre.pack(expand = YES,pady=10)


label_sous_titre = Label(fenetre, text="Entrer le motif que vous souhaitez chercher dans le code pénal", font=("Helvetica", 30), bg = "#32404D", fg ="#00D5DB")
label_sous_titre.pack(expand = YES,  pady=5)

#creation d'une entrée dans laquelle les utilisateurs entre le motif qu'il cherche

entry_mot = Entry(fenetre,font=("Helvetica", 20), bg = "#32404D", fg ="#00D5DB")
entry_mot.pack(expand = YES,  pady=5)

#creation des boutons pour déclencher les fonctioons de recherche textuelle

bouton_recherche_bm = Button(fenetre, font=("Helvetica", 20),text="Recherche_bm", bg = "#32404D", fg ="#00D5DB", command=bouton_bm)
bouton_recherche_bm.pack(expand = YES,pady=10)

bouton_recherche_naif = Button(fenetre,font=("Helvetica", 20),  text="Recherche_naif", bg = "#32404D", fg ="#00D5DB",command=bouton_naif)
bouton_recherche_naif.pack(expand = YES,pady=10)

# création de la zone ou apparaitra le texte renvoyé par les fonctions de recherche

result_text = Text(fenetre, height=25, width=120, font = ("Helvetica",15),bg = "#32404D", fg ="#00D5DB")
result_text.pack(expand = YES, pady=10)




#affichage de l'interface
fenetre.mainloop()

#https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiBptmYiaSDAxUdUqQEHXzXDTMQFnoECA8QAQ&url=https%3A%2F%2Fcodes.droit.org%2FPDF%2FCode%2520p%25C3%25A9nal.pdf&usg=AOvVaw3kMNd6B10vLYI7vNXxZrVC&opi=89978449