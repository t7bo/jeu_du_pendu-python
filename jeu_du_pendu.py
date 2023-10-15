import random
import string
import ascii_patterns
import listes

from colorama import Fore, Back, Style, init
init(autoreset=True)

# 1ER INPUT >  L'UTILISATEUR CHOISIT UNE THEMATIQUE AVEC SON CHIFFRE CORRESPONDANT
# si l'utilisateur ne rentre pas une valeur correcte alors on lui demande de rentrer une valeur correcte


thematiques_listes = {
    1: listes.animaux, 2: listes.films,
    3: listes.series, 4: listes.superheros,
    5: listes.prenoms_masculins, 6: listes.prenoms_feminins,
    7: listes.pays, 8: listes.capitales,
    9: listes.musique, 10: listes.metiers}


index_thematique = {"1": "animaux", "2": "films", "3": "series", "4": "superheros", "5": "prenoms_masculins",
                    "6": "prenoms_feminins", "7": "pays", "8": "capitales du monde", "9": "artistes musicaux",
                    "10": "métiers"}


thematique_choisie = input("""
                                Bonjour! Nous allons jouer au jeu du pendu.
                                Merci de choisir une thématique parmi les choix suivants:\n
                                1: noms d'animaux
                                2: titres de films
                                3: séries
                                4: noms de super-héros
                                5: prenoms masculins
                                6: prenoms féminins
                                7: pays du monde
                                8: capitales du monde
                                9: artistes musicaux
                                10: métiers\n
                                """)


while not thematique_choisie.isdigit() or int(thematique_choisie) not in range(1, len(thematiques_listes)+1, 1):
    thematique_choisie = input("""Je n'ai pas compris.
                               Merci de taper une valeur correspondante à la thématique de votre choix :\n
                                1: noms d'animaux
                                2: titres de films
                                3: séries
                                4: noms de super-héros
                                5: prenoms masculins
                                6: prenoms féminins
                                7: pays du monde
                                8: capitales du monde
                                9: artistes musicaux
                                10: métiers\n
                                  """)


cat = index_thematique[thematique_choisie]
print(f"{Fore.YELLOW}Vous avez choisi la catégorie '{cat}'.")


# CHOIX ALEATOIRE D'UN MOT DE LA LISTE DE LA THEMATIQUE CHOISIE PAR L'UTILISATEUR

liste_mots = thematiques_listes[int(thematique_choisie)]

mot_choisi = random.choice(liste_mots).upper()
# print(f" le mot aléatoire à deviner : {mot_choisi}")

# chaîne contenant toutes les lettres majuscules de l'alphabet
lettres_alphabet_majuscules = string.ascii_uppercase


# TRANSFORMATION DES LETTRES DU MOT RANDOM CHOISI EN UNDERSCORES, CREATION D'ESPACES ENTRE CHAQUE UNDERSCORE
# ET CREATION D'UNE LISTE VIDE DANS LAQUELLE ON METTRA TOUTES LES LETTRES JOUEES QUI NE FIUGRENT PAS DANS LE MOT A DEVINER

# remplacer les lettres du mot choisi par des tirets bas (_) si pas dans le mot et la lettre
mot = mot_choisi.replace(mot_choisi, "_"*len(mot_choisi))
# mot_join = " ".join(mot)

L = set()


# DEUXIEME INPUT > NIVEAU DE DIFFICULTE
# L'UTILISATEUR CHOISI SON NIVEAU DE PREFERENCE, PLUS LE NIVEAU EST DIFFICILE MOINS L'UTILISATEUR AURA DE TENTATIVES POUR TROUVER LE MOT


niveau_difficulte_dico = {
    1: "facile", 2: "moyen",
    3: "difficile", 4: "impossible"
}

niveau_de_difficulte = input("""
                             Dernière étape :
                             merci de taper le chiffre correspondant au niveau de difficulté que vous souhaitez.\n
                             1: Facile
                             2: Moyen
                             3: Difficile
                             4: Impossible
                             \n""")


while not niveau_de_difficulte.isdigit():

    niveau_de_difficulte = input("""Je n'ai pas compris.
                                 Merci de taper le chiffre correspondant au niveau de difficulté que vous souhaitez.\n
                             1: Facile
                             2: Moyen
                             3: Difficile
                             4: Impossible
                                  \n""")


if niveau_de_difficulte == "1":
    tentatives = 20
    print(
        f"{Fore.YELLOW}Vous avez choisi le niveau '{niveau_difficulte_dico[1]}'.")
    print(
        f"Vous aurez {tentatives} essais pour trouver le mot auquel je pense. Nous pouvons commencer.\n")

elif niveau_de_difficulte == "2":
    tentatives = 15
    print(
        f"{Fore.YELLOW}Vous avez choisi le niveau '{niveau_difficulte_dico[2]}'.")
    print(
        f"Vous aurez {tentatives} essais pour trouver le mot auquel je pense. Nous pouvons commencer.\n")

elif niveau_de_difficulte == "3":
    tentatives = 10
    print(
        f"{Fore.YELLOW}Vous avez choisi le niveau '{niveau_difficulte_dico[3]}'.")
    print(
        f"Vous aurez {tentatives} essais pour trouver le mot auquel je pense. Nous pouvons commencer.\n")

elif niveau_de_difficulte == "4":
    tentatives = 8
    print(
        f"{Fore.YELLOW}Vous avez choisi le niveau '{niveau_difficulte_dico[4]}'.")
    print(
        f"Vous aurez {tentatives} essais pour trouver le mot auquel je pense. Nous pouvons commencer.\n")

else:
    niveau_de_difficulte = input("""Je n'ai pas compris. Dernière étape : merci de taper le chiffre correspondant au niveau de difficulté que vous souhaitez.
                             1: Facile
                             2: Moyen
                             3: Difficile
                             4: Impossible
                                  """)


# JEU DU PENDU
# On demande à l'utilisateur de rentrer une lettre (qu'on met en majuscule afin de la comparer avec la liste des mots)
# On indique à l'utilisateur son nombre d'erreurs éffectuées et le nombre de tentatives restantes

# On affique la liste des lettres jouées qui ne figurent pas dans le mot à trouver
# si la lettre indiquée par l'utilisateur est déjà dans la liste, alors on demande à l'utilisateur de choisir une nouvelle lettre tout en lui laissant ses nb d'erreurs et de tentatives intacts

# si il n'y a plus de underscores dans le mot à trouver, alors on affiche BRAVO

# à la dernière tentative disponible, on offre la possibilité à l'utilisateur de taper le mot complet si il pense avoir la bonne réponse
# si c'est la bonne réponse, alors on affiche BRAVO

# si plus de tentatives ou erreurs = 6 alors > Perdu, on affiche le mot qu'il fallait deviner.


erreur = 0
print(" ".join(mot), "\n")


while "_" in " ".join(mot):

    lettre = input(
        f"{Fore.LIGHTBLUE_EX}Entre une lettre de A à Z : ").upper()
    # print(f"Erreurs : {erreur}/6. Il vous reste {tentatives} tentative(s) pour trouver le mot.")
    # print(f"Lettres choisies qui ne figurent pas dans le mot à deviner : {L}")

    if lettre in " ".join(mot) and lettre in mot_choisi and lettre != " ":
        print(
            f"\n{Fore.RED}Vous avez déjà donné cette réponse. Merci d'indiquer une autre lettre.")
        tentatives += 1

    elif lettre in L:
        print(
            f"\n{Fore.RED}Vous avez déjà donné cette réponse. Merci d'indiquer une autre lettre.")
        tentatives += 1
        erreur -= 1

    if " ".join(mot) == mot_choisi:
        print(f"{Fore.LIGHTGREEN_EX}Bravo! Vous avez réussi à trouver le mot à deviner avant d'épuiser vos 10 tentatives ou de finir pendu!")
    elif len(lettre) > 1 or lettre.isdigit():
        print(f"\n{Fore.YELLOW}Merci d'entrer une lettre valide")

    if lettre in mot_choisi and len(lettre) == 1 and tentatives >= 1:

        tentatives -= 1

        # fonction et boucle pour sauvegarder les indices de mot_choisi où la lettre apparaît
        def remplacer_lettres(mot_choisi, mot, lettre):
            indices = []
            for i in range(len(mot_choisi)):
                if mot_choisi[i] == lettre:
                    indices.append(i)

            # Remplacez les underscores aux indices correspondants par la lettre
            for index in indices:
                mot = mot[:index] + lettre + mot[index + 1:]

            return mot

        mot = remplacer_lettres(mot_choisi, mot, lettre)
        # print(" ".join(mot))

        print(
            f"\n{Fore.LIGHTGREEN_EX}Bien joué! La lettre {lettre} est bien dans le mot mystère!\n")

    if lettre not in mot_choisi and len(lettre) == 1 and tentatives >= 1:

        print(
            f"\n{Fore.RED}Dommage! La lettre {lettre} ne se trouve pas dans le mot mystère!\n")

        # L.extend(lettre)
        L.add(lettre)

        messages_erreurs = {
            1: ascii_patterns.premiere_erreur,
            2: ascii_patterns.deuxieme_erreur,
            3: ascii_patterns.troisieme_erreur,
            4: ascii_patterns.quatrieme_erreur,
            5: ascii_patterns.cinquieme_erreur,
            6: ascii_patterns.sixieme_erreur,
            7: ascii_patterns.septieme_erreur,
            8: ascii_patterns.huitieme_erreur
        }
        erreur += 1
        tentatives -= 1
        # print(
        #     f"Erreurs : {erreur}/8. Il vous reste {tentatives} tentative(s) pour trouver le mot.")

        # print(f"{Fore.RED}Erreurs : {erreur}/8. {L}")
        # print(f"Il vous reste {tentatives} tentative(s) pour trouver le mot.")

        if erreur in messages_erreurs:
            print(f"{Fore.RED}{messages_erreurs[erreur]}")

        if erreur == 8:
            print(
                f"Vous avez fait {erreur} erreurs.\nVous avez perdu. Le mot à deviner était :")
            print(f"{Fore.YELLOW}{mot_choisi}")
            break
        print(f"{Fore.RED}Erreurs : {erreur}/8. {L}")
    print(f"Il vous reste {tentatives} tentative(s) pour trouver le mot.\n")
    print(f'{" ".join(mot)}\n')

    if tentatives == 0:
        if "_" in " ".join(mot):
            reponse = input(
                "Vous avez épuisé toutes vos tentatives. Avez-vous deviné à quel mot je pensais? Votre réponse : ").upper()
            if reponse != mot_choisi:
                erreur -= 1
                print(f"Vous avez perdu. Le mot à deviner était :")
                print(f"{Fore.YELLOW}{mot_choisi}")
                break
            else:
                print(f"""{Fore.LIGHTGREEN_EX} 
                Bravo! Vous avez réussi à trouver le mot à deviner avant d'épuiser vos tentatives ou de finir pendu!
                """)
                break
        elif not "_" in " ".join(mot):
            print(f"""{Fore.LIGHTGREEN_EX}
            Bravo! Vous avez réussi à trouver le mot à deviner avant d'épuiser vos tentatives ou de finir pendu!
            """)
            break

    elif not "_" in " ".join(mot):
        print(f"""{Fore.LIGHTGREEN_EX}
        Bravo! Vous avez réussi à trouver le mot à deviner avant d'épuiser vos tentatives ou de finir pendu!
        """)
        break
