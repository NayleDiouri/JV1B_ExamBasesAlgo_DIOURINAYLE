#Question 1 
print("Question 1")

ligne1 = ['_','_','_']
ligne2 = ['_','_','_']
ligne3 = ['_','_','_']

print(ligne1)
print(ligne2)
print(ligne3)


#Question 2
print("Question 2")


ligne1 = ['_','_','_']
ligne2 = ['_','_','_']
ligne3 = ['_','_','_']

for i in range (0, 5):
    CaseJoueur1 = input("sur quelle case voulez vous mettre un O?")
    #chaque correspond a un numéro en commençant par 1 en haut à gauche jusqu'a 9 en bas à droite


    if(CaseJoueur1 == "1"):
        ligne1[0] = 'O'
    elif(CaseJoueur1 == "2"):
        ligne1[1] = 'O'
    elif(CaseJoueur1 == "3"):
        ligne1[2] = 'O'
    elif(CaseJoueur1 == "4"):
        ligne2[0] = 'O'
    elif(CaseJoueur1 == "5"):
        ligne2[1] = 'O'
    elif(CaseJoueur1 == "6"):
        ligne2[2] = 'O'
    elif(CaseJoueur1 == "7"):
        ligne3[0] = 'O'
    elif(CaseJoueur1 == "8"):
        ligne3[1] = 'O'
    else:
        ligne3[2] = 'O'

    print(ligne1)
    print(ligne2)
    print(ligne3)



    CaseJoueur2 = input("sur quelle case voulez vous mettre un X?")


    if(CaseJoueur2 == "1"):
        ligne1[0] = 'X'
    elif(CaseJoueur2 == "2"):
        ligne1[1] = 'X'
    elif(CaseJoueur2 == "3"):
        ligne1[2] = 'X'
    elif(CaseJoueur2 == "4"):
        ligne2[0] = 'X'
    elif(CaseJoueur2 == "5"):
        ligne2[1] = 'X'
    elif(CaseJoueur2 == "6"):
        ligne2[2] = 'X'
    elif(CaseJoueur2 == "7"):
        ligne3[0] = 'X'
    elif(CaseJoueur2 == "8"):
        ligne3[1] = 'X'
    else:
        ligne3[2] = 'X'

    print(ligne1)
    print(ligne2)
    print(ligne3)


#Question 6 
# Il faudrait qu'au lieu de placer des o ont ils "tombent" dans la grille, et augmenter de 1  la fonctionnalité vérifiant si oui ou non l’un des joueurs a réussi à aligner 3
# symboles sur une ligne verticale, horizontale, diagonale, et aussi prendre en compte que les o placés au dessus d'un autre reste bien au dessus.