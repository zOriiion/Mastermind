#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Bastien
#
# Created:     26/11/2019
# Copyright:   (c) Bastien 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def mastermind():
    nbChiffre = 4
    manche = 0
    #Manche actuelle
    chiffreCorrect = 0
    compteurTour = 0
    codeCorrect = 0
    codeMalPlace = 0
    tour = 0
    place1 = 0
    place2 = 0
    place3 = 0
    place4 = 0
    place5 = 0
    scoreJoueur1 = 0
    scoreJoueur2 = 0



    print("0 = Normal , 1 = 5 chiffres , 2 = Pas le droit de mettre deux fois la meme couleur.")
    variante = int(input("Entrer la variante voulu (lire console):"));
    #Choix de la variante
    nbManche = int(input("Choisissez le nombre de manches voulu :"))
    #Choix du nombre de manches
    if (variante ==1):
        nbChiffre += 1;

    while(manche != nbManche):
        while(nbChiffre != chiffreCorrect):
            #Input et vérification du code secret
            chiffre1 = int(input("Entrez le premier chiffre du code :"));
            chiffre2 = int(input("Entrez le deuxième chiffre du code :"));
            chiffre3 = int(input("Entrez le troisième chiffre du code :"));
            chiffre4 = int(input("Entrez le quatrième chiffre du code :"));
            if (variante==1):
                chiffre5 = int(input("Entrez le cinquième chiffre du code :"));

            if (chiffre1 < 7):
                chiffreCorrect += 1
            if (chiffre2 < 7):
                chiffreCorrect += 1
            if (chiffre3 < 7):
                chiffreCorrect += 1
            if (chiffre4 < 7):
                chiffreCorrect += 1
            if (chiffre1 == 0):
                chiffreCorrect -= 1
            if (chiffre2 == 0):
                chiffreCorrect -= 1
            if (chiffre3 == 0):
                chiffreCorrect -= 1
            if (chiffre4 == 0):
                chiffreCorrect -= 1
            if (variante == 1):
                if (chiffre5 < 7):
                    chiffreCorrect += 1
                if (chiffre5 == 0):
                    chiffreCorrect -= 1
            if (variante == 2):
                if (chiffre1 == chiffre2):
                    chiffreCorrect = 0;
                if (chiffre1 == chiffre3):
                    chiffreCorrect = 0;
                if (chiffre1 == chiffre4):
                    chiffreCorrect = 0;
                if (chiffre2 == chiffre3):
                    chiffreCorrect = 0;
                if (chiffre2 == chiffre4):
                    chiffreCorrect = 0;
                if (chiffre3 == chiffre4):
                    chiffreCorrect = 0;
            if (chiffreCorrect != nbChiffre):
                print("Les chiffres doivent etre entre 1 et 6 ou si vous avez choisit la variante 2, ils doivent etre differents.")
        chiffreCorrect = 0
        if (variante != 1):
            print("Le code est : "+str(chiffre1)+str(chiffre2)+str(chiffre3)+str(chiffre4))
        if (variante == 1):
            print("Le code est : "+str(chiffre1)+str(chiffre2)+str(chiffre3)+str(chiffre4)+str(chiffre5))
            #Passage au chercheur

        while(compteurTour == 0):
            code1 = int(input("Entrez le premier chiffre :"));
            code2 = int(input("Entrez le deuxième chiffre :"));
            code3 = int(input("Entrez le troisième chiffre :"));
            code4 = int(input("Entrez le quatrième chiffre :"));
            if(variante == 1):
                code5 = int(input("Entrez le cinquiéme chiffre :"));
            tour += 1

            if (code1 == chiffre1):
                codeCorrect += 1;
                place1 += 1;

            if (code2 == chiffre2):
                codeCorrect += 1;
                place2 += 1;

            if (code3 == chiffre3):
                codeCorrect += 1;
                place3 += 1;

            if (code4 == chiffre4):
                codeCorrect += 1;
                place4 += 1;

            if (variante == 1):
                if (code5 == chiffre5):
                    codeCorrect += 1;
                    place5 += 1;

            if (place1 == 0):
                if (code1 == chiffre2):
                    codeMalPlace += 1
                    place1 += 1
                elif (code1 == chiffre3):
                    codeMalPlace += 1
                    place1 += 1
                elif (code1 == chiffre4):
                    codeMalPlace += 1
                    place1 += 1

            if (place2 == 0):
                if (code2 == chiffre3):
                    codeMalPlace += 1
                    place2 += 1
                elif (code2 == chiffre4):
                    codeMalPlace += 1
                    place2 += 1

            if (place3 == 0):
                if (code3 == chiffre4):
                    codeMalPlace += 1
                    place3 += 1

            if (variante == 1):
                if (place5 == 0):
                    if (code5 == chiffre1):
                        codeMalPlace += 1
                        place5 += 1
                    elif (code5 == chiffre2):
                        codeMalPlace += 1
                        place5 += 1
                    elif (code5 == chiffre3):
                        codeMalPlace += 1
                        place5 += 1
                    elif (code5 == chiffre4):
                        codeMalPlace += 1
                        place5 += 1





            print("Il y a "+str(codeCorrect)+"chiffre(s) bien placé(s) et "+str(codeMalPlace)+" chiffre(s) mal placé(s)");

            if (codeCorrect == nbChiffre):
                compteurTour += 1;
                print("Bien joué ! Le joueur 1 remporte "+str(tour)+"point ! Au tour du joueur 2.");


            if (tour == 12):
                compteurTour += 1;
                print("Perdu ! Le joueur 1 remporte "+str(tour)+"point ! Au tour du joueur 2.");

            codeCorrect = 0;
            place1 = 0
            place2 = 0
            place3 = 0
            place4 = 0
            place5 = 0
            scoreJoueur1 += tour

        compteurTour = 0;
        tour = 0;1

        #Changement de joueur


        while(nbChiffre != chiffreCorrect):
            #Input et vérification du code secret
            chiffre1 = int(input("Entrez le premier chiffre du code :"));
            chiffre2 = int(input("Entrez le deuxième chiffre du code :"));
            chiffre3 = int(input("Entrez le troisième chiffre du code :"));
            chiffre4 = int(input("Entrez le quatrième chiffre du code :"));
            if (variante==1):
                chiffre5 = int(input("Entrez le cinquième chiffre du code :"));

            if (chiffre1 < 7):
                chiffreCorrect += 1
            if (chiffre2 < 7):
                chiffreCorrect += 1
            if (chiffre3 < 7):
                chiffreCorrect += 1
            if (chiffre4 < 7):
                chiffreCorrect += 1
            if (chiffre1 == 0):
                chiffreCorrect -= 1
            if (chiffre2 == 0):
                chiffreCorrect -= 1
            if (chiffre3 == 0):
                chiffreCorrect -= 1
            if (chiffre4 == 0):
                chiffreCorrect -= 1
            if (variante == 1):
                if (chiffre5 < 7):
                    chiffreCorrect += 1
                if (chiffre5 == 0):
                    chiffreCorrect -= 1
            if (variante == 2):
                if (chiffre1 == chiffre2):
                    chiffreCorrect = 0;
                if (chiffre1 == chiffre3):
                    chiffreCorrect = 0;
                if (chiffre1 == chiffre4):
                    chiffreCorrect = 0;
                if (chiffre2 == chiffre3):
                    chiffreCorrect = 0;
                if (chiffre2 == chiffre4):
                    chiffreCorrect = 0;
                if (chiffre3 == chiffre4):
                    chiffreCorrect = 0;
            if (chiffreCorrect != nbChiffre):
                print("Les chiffres doivent etre entre 1 et 6 ou si vous avez choisit la variante 2, ils doivent etre differents.")
        chiffreCorrect = 0
        if (variante != 1):
            print("Le code est : "+str(chiffre1)+str(chiffre2)+str(chiffre3)+str(chiffre4))
        if (variante == 1):
            print("Le code est : "+str(chiffre1)+str(chiffre2)+str(chiffre3)+str(chiffre4)+str(chiffre5))
            #Passage au chercheur

        while(compteurTour == 0):
            code1 = int(input("Entrez le premier chiffre :"));
            code2 = int(input("Entrez le deuxième chiffre :"));
            code3 = int(input("Entrez le troisième chiffre :"));
            code4 = int(input("Entrez le quatrième chiffre :"));
            if(variante == 1):
                code5 = int(input("Entrez le cinquiéme chiffre :"));
            tour += 1

            if (code1 == chiffre1):
                codeCorrect += 1;
                place1 += 1;

            if (code2 == chiffre2):
                codeCorrect += 1;
                place2 += 1;

            if (code3 == chiffre3):
                codeCorrect += 1;
                place3 += 1;

            if (code4 == chiffre4):
                codeCorrect += 1;
                place4 += 1;

            if (variante == 1):
                if (code5 == chiffre5):
                    codeCorrect += 1;
                    place5 += 1;

            if (place1 == 0):
                if (code1 == chiffre2):
                    codeMalPlace += 1
                    place1 += 1
                elif (code1 == chiffre3):
                    codeMalPlace += 1
                    place1 += 1
                elif (code1 == chiffre4):
                    codeMalPlace += 1
                    place1 += 1

            if (place2 == 0):
                if (code2 == chiffre3):
                    codeMalPlace += 1
                    place2 += 1
                elif (code2 == chiffre4):
                    codeMalPlace += 1
                    place2 += 1

            if (place3 == 0):
                if (code3 == chiffre4):
                    codeMalPlace += 1
                    place3 += 1

            if (variante == 1):
                if (place5 == 0):
                    if (code5 == chiffre1):
                        codeMalPlace += 1
                        place5 += 1
                    elif (code5 == chiffre2):
                        codeMalPlace += 1
                        place5 += 1
                    elif (code5 == chiffre3):
                        codeMalPlace += 1
                        place5 += 1
                    elif (code5 == chiffre4):
                        codeMalPlace += 1
                        place5 += 1





            print("Il y a "+str(codeCorrect)+"chiffre(s) bien placé(s) et "+str(codeMalPlace)+" chiffre(s) mal placé(s)");

            if (codeCorrect == nbChiffre):
                compteurTour += 1;
                print("Bien joué ! Le joueur 1 remporte "+str(tour)+"point ! Au tour du joueur 2.");


            if (tour == 12):
                compteurTour += 1;
                print("Perdu ! Le joueur 1 remporte "+str(tour)+"point ! Au tour du joueur 2.");

            codeCorrect = 0;
            place1 = 0
            place2 = 0
            place3 = 0
            place4 = 0
            place5 = 0
            scoreJoueur2 += tour





        compteurTour = 0
        tour = 0
        manche += 1

    print("Fin du jeu, le joueur 1 a : "+str(scoreJoueur1)+" points et le joueur 2 : "+str(scoreJoueur2)+" points.")













def main():
    mastermind();

if __name__ == '__main__':
    main()