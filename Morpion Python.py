grille = "   |   |   \n-----------\n   |   |   \n-----------\n   |   |   "
print(grille,"\n")
print("\n--------------------------------")

  
def input_position(ligne,colonne):    
    liste = [int(ligne),int(colonne)]
    return liste


def remplissage(ligne,colonne):
    liste_positions = input_position(ligne,colonne)
    if liste_positions[0] == 1:
        grille2 = grille[0:1+(liste_positions[1]-1)*4] + icone() + grille[2+(liste_positions[1]-1)*4:59]
    elif liste_positions[0] == 2:
        grille2 = grille[0:25+(liste_positions[1]-1)*4] + icone() + grille[26+(liste_positions[1]-1)*4:59]
    elif liste_positions[0] == 3:
        grille2 = grille[0:49+(liste_positions[1]-1)*4] + icone() + grille[50+(liste_positions[1]-1)*4:59]
    else: 
        grille2 = grille
    return grille2
    
                
def tour_joueur():
    if compteur_joueur >= 0:
        joueur = 0
    if compteur_joueur <= 0:
        joueur = 1    
    return joueur
    

def icone():
    joueur = tour_joueur()
    if joueur == 0:
        return "O"
    if joueur == 1:
        return "X"   


#renvoie True si la ligne ou la colonne est hors de la grille
def erreur_valeur(ligne,colonne):
    if int(ligne) > 3 or int(ligne) < 1 or int(colonne) > 3 or int(colonne) < 1:
        print("La ligne ou la colonne donnée est trop grande.\nVeuiller donner les bonnes valeurs\n")
        return True
    

#renvoie True si une case est deja remplie    
def erreur_case_remplie(ligne,colonne):
    if (ligne,colonne) in liste_cases:
        print("\nErreur, cette case est deja remplie! Veuiller entrer de nouvelles valeurs.\n\n")
        return True
    

#revoie True si la partie est gagnee par un des deux joueurs
def gagne(grille):
    '''if ((('1','1') and ('1','2') and ('1','3')) in liste_joueur) or ((('2','1') and ('2','2') and ('2','3')) in liste_joueur) or ((('3','1') and ('3','2') and ('3','3'))in liste_joueur) or ((('1','1') and ('2','1') and ('3','1'))in liste_joueur) or ((('1','2') and ('2','2') and ('3','2'))in liste_joueur) or ((('1','3') and ('2','3') and ('3','3'))in liste_joueur) or ((('1','1') and ('2','2') and ('3','3'))in liste_joueur) or ((('3','1') and ('2','2') and ('1','3'))in liste_joueur):
        return True'''
    for i in range(3):
        if grille[1]==grille[5]==grille[9]!=' ' or grille[25]==grille[29]==grille[33]!=' ' or grille[49]==grille[53]==grille[57]!=' ' or grille[1]==grille[25]==grille[49]!=' ' or grille[5]==grille[29]==grille[53]!=' ' or grille[9]==grille[33]==grille[57]!=' ' or grille[1]==grille[29]==grille[57]!=' ' or grille[9]==grille[29]==grille[49]!=' ':
            return True
    
   
valeur = True
compteur_joueur = 1
liste_cases = []
liste_cases_joueur_1 = []
liste_cases_joueur_2 = []
partie_remportee = False
#boucle while qui fonctionne tant qu'une des conditions de fin de partie n'est pas remplie
while valeur == True:        
    ligne = input("donner une ligne: ")
    colonne = input("donner une colonne: ")
    #condition qui saute un tour de boucle s'il y a une erreur
    if erreur_valeur(ligne,colonne) != True and erreur_case_remplie(ligne,colonne) != True:
        liste_cases.append((ligne,colonne))
        grille = remplissage(ligne,colonne)
        print(grille)
        if gagne(grille) == True:
            if compteur_joueur > 0:
                print("\nLe joueur",1,"gagne!")
                partie_remportee = True
            if compteur_joueur < 0:
                print("\nLe joueur",2,"gagne!")
                partie_remportee = True                        
        compteur_joueur = compteur_joueur * -1
        print("\n--------------------------------")
        if len(liste_cases) == 9 or partie_remportee == True:
            valeur = False
            print("La partie est terminee")
