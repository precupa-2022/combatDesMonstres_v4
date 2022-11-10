"""
Programme fait par Alexander Precup
Groupe: 402
Description: TP3 - combat des monstres version 4
    Le but de la partie est d’accumuler le plus possible de victoires.  Elles s’additionnent en vainquant des monstres.
    Pour gagner des points de vie, l’usager doit avoir un total aux dés supérieur à la force du monstre.
    L’usager peut tomber face à face avec un monstre trop effrayant.
    Dans ce cas, l’usager peut contourner le monstre et aller ouvrir une autre porte (l'usage perd 1 point de vie)
    L’usager perd le combat si son total aux dés est inférieur (ou égal) à la force du monstre.
    Dans ce cas l’usager perdra autant de points de vie que la force du monstre affronté.
    L’usager commence la partie avec un pactole de points de vie (fixé arbitrairement à 20).

    Après 3 victoires, l’usager tombe face à face avec un monstre nécessairement plus difficile (e.g. le boss).

    Modifier le code pour que le combat se fasse avec 2 dés.  Modifier force_adversaire en conséquence.
"""
import random

niveau_vie = 20  # l'usager commence avec 20 points de vie
# initialiser les variables utilisées dans les messages
numero_adversaire = 0
numero_combat = 0
nombre_victoires = 0
nombre_defaites = 0
nombre_victoires_consecutives = 0
statut_combat = "Aucun"

boucle_jeu = True
while boucle_jeu:
    force_adversaire = random.randint(1, 11)    # force de monstre
    numero_adversaire = numero_adversaire + 1   # augumenter les nombres de monstres combatus

    # afficher le menu de la partie et demander l'utilisateur de faire une choix
    print(f"Vous tombez face à face avec un adversaire de difficulté : {force_adversaire} ")
    print(f"Que voulez vous faire ? ")
    print(f"1 - Combattre cet adversaire ")
    print(f"2 - Conturner cet adversaire et aller ouvrir une autre porte ")
    print(f"3 - Afficher les règles du jeu ")
    print(f"4 - Quitter la partie ")
    choix = int(input("Entrez votre choix :"))

    if choix == 1:  # le choix utilisateur est de combattre
        choix_combattre = True
        while choix_combattre:
            # augumenter le numéro combat pour chaque lancement de dé
            numero_combat = numero_combat + 1

            # afficher le statut de la partie
            print(f"Adversaire : {numero_adversaire}")
            print(f"Force de l'adversaire : {force_adversaire}")
            print(f"Niveau de vie de l'usager : {niveau_vie}")
            print(f"Combat {numero_combat} : victoires {nombre_victoires} vs defaites {nombre_defaites}")

            # afficher le résultat de lancement dés usager
            lance_de_no1 = random.randint(1, 6)
            lance_de_no2 = random.randint(1, 6)
            print(f"Lancer du dé # 1: {lance_de_no1}")
            print(f"Lancer du dé # 2: {lance_de_no2}")

            # afficher le statut de combat
            if numero_combat >= 2:
                print(f"Dérnier combat = {statut_combat}")

            # niveau de vie de l'usager diminue dans le cas d'une défaite
            if (lance_de_no1 + lance_de_no2) <= force_adversaire:
                niveau_vie = niveau_vie - force_adversaire
                nombre_defaites = nombre_defaites + 1
                statut_combat = "Défaite"
            else:  # niveau de vie de l'usager augumente dans le cas d'une victoire
                niveau_vie = niveau_vie + force_adversaire
                nombre_victoires = nombre_victoires + 1
                nombre_victoires_consecutives = nombre_victoires_consecutives + 1
                statut_combat = "Victoire"

            # combat soldé par la victoire de l'usager
            if statut_combat == "Victoire":
                print(f"Niveau de vie : {niveau_vie}")
                print(f"Nombre de victoires consécutives : {nombre_victoires_consecutives}")
            else:  # combat soldé par la défaite de l'usager
                print(f"Niveau de vie : {niveau_vie}")

            # proposer un nouvel adversaire; après 3 victoires, l’usager tombe avec un monstre plus difficile
            if nombre_victoires >= 3:
                print(f"Après 3 victoires, vous tombez avec un adversaire plus difficile ! ")
                force_adversaire = random.randint(1, 20)
            else:
                force_adversaire = random.randint(1, 11)

            # niveau de vie de l’usager est inférieur ou égal à 0
            # L’ordinateur annonce à l’usager la fin de la partie et le nombre de victoire(s) réussie(s).
            if niveau_vie <= 0:
                print(f"La partie est terminée, vous avez vaincu {nombre_victoires} monstre(s).")
                choix_combattre = False
                boucle_jeu = False

    elif choix == 2:  # le choix utilisateur est de conturner cet adversaire et aller ouvrir une autre porte
        niveau_vie = niveau_vie - 1  # pénalité de 1 point de vie

    elif choix == 3:  # le choix utilisateur est d'afficher les règles du jeu
        print(f"Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.")
        print(f"Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.")
        print(f"Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de "
              f"l’adversaire.")
        print(f"Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.")
        print(f"Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.")
        print(f"Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.")
        print(f" ")
        print(f"La partie se termine lorsque les points de vie de l’usager tombent sous 0.")
        print(f" ")
        print(f"L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité "
              f"de 1 point de vie.")

    else:  # le choix utilisateur est quitter jeu
        print(f"Merci et au revoir … ")
        boucle_jeu = False
