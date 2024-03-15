from colorama import Fore
import random
import time
import sys


points_repentance = 0
points_puissance = 0
pdv = 100
monstres_existant = ["Pilleur", "Mercenaire", "Mendiant"]
victoire = False


def combat_ou_pacification_monstre():
    global points_repentance, points_puissance, pdv, monstres_existant
    monstre = monstres_existant[random.randint(0,2)]
    choix = input("Vou rencontrez un {}, Voulez-vous combattre (1) ou tenter de pacifier (2) l'ennemi ? ".format(monstre))
    if choix == "1":
        if monstre == "Mercenaire":
            if random.random() > 0.7:
                points_puissance += 10
                print("Vous avez vaincu l'ennemi.")
            else :
                pdv += -10
                print("Vous avez été vaincu, vous perdez 10 PV.")
        else :
            if random.random() > 0.2:
                points_puissance += 10
                print("Vous avez vaincu l'ennemi.")
            else :
                pdv += -10
                print("Vous avez été vaincu, vous perdez 10 PV.")

    elif choix == "2":
        if monstre == "Mercenaire":
            if random.random() > 0.2:
                points_repentance += 10 
                print("Vous avez réussi à pacifier l'ennemi, vous gagnez 10 points de repentance")
            else :
                pdv += -5
                print("Votre tentative de pacificationa échoué, vous perdez 5 PV.")
        else :
            if random.random() > 0.7:
                points_repentance += 10 
                print("Vous avez réussi à pacifier l'ennemi, vous gagnez 10 points de repentance")
            else :
                pdv += -5
                print("Votre tentative de pacificationa échoué, vous perdez 5 PV.")

def fin_du_jeu(meurtre):
    global victoire
    if meurtre:
        print("Fin 1: Vous êtes craint et seul.")
    else:
        print("Fin 2: Vous avez pacifié vos ennemis et vivez une vie heureuse.")
    victoire = True
   
def combat_ou_pacification_boss():
    global points_repentance, points_puissance, pdv, monstres_existant
    choix = input("Vous rencontrez le boss final, Voulez-vous combattre (1) ou tenter de le pacifier (2) ?")
    if choix == "1":
        if points_puissance >= 100 :
            print("Vous avez vaincu le boss, félicitations !")
            fin_du_jeu(True)
        else :
            print("Vous n'êtes pas encore assez puissant, le boss vous bat et vous perdez 10 PV")
    elif choix == "2":
        if points_repentance >= 100 :
            print("Vous avez pacifié le boss, félicitations !")
            fin_du_jeu(False)
        else :
            print("Vous n'êtes pas encore assez conavaincant, le boss vous bat et vous perdez 5 PV")


def menu():
    print(f"{Fore.CYAN}MAIN MENU :{Fore.RESET}")
    print(f"{Fore.YELLOW}1. Create New Game{Fore.RESET}")
    print(f"{Fore.RED}2. Load Saved Game{Fore.RESET}")
    print(f"{Fore.GREEN}3. About{Fore.RESET}")
    print("4. Exit")
    user_choice = input("> Veuillez choisir 1 option : ")
    return user_choice

def afficher_dialogue(dialogue):
    print(dialogue)

def dialogue_suivant():
    input("Appuyez sur Entrée pour passer au dialogue suivant.")

def introduction():
    afficher_dialogue(f"Villageois: {user_name},{user_name}! Réveillez vous!")
    dialogue_suivant()

    afficher_dialogue("Villageois: cette fois la faction des crasseux ont décider de nous prendre toute notre eau, notre chef voudrais vous parler.")
    dialogue_suivant()

    afficher_dialogue(f"Chef du village: {user_name} ,s'en est assez, le village croule sous le travaille et les pillages des crasseux, si cela continue, nous seront mort dans un futur proche")
    dialogue_suivant()

    afficher_dialogue(f"Chef du village: Si tu arrives à nous débarrasser de nos ennemis, tu seras mis à l'honneur du village et nous nous souviendrons de toi comme le héros que tu as été.")
    dialogue_suivant()

    afficher_dialogue("Chef du village : Maintenant part et reviens lorsque tu te seras débarrassé de ces vermines")
    dialogue_suivant()

def direction():
    print(f"{Fore.CYAN}1. Go East{Fore.RESET}")
    print(f"{Fore.CYAN}2. Go North{Fore.RESET}")
    print(f"{Fore.CYAN}3. Go West{Fore.RESET}")
    print(f"{Fore.CYAN}4. Go South{Fore.RESET}")
    way = input("Ou souhaitez vous allez ? ")
    if way in ['1', '2', '3', '4']:
        print('Tres bien ! ')
    else:
        print(f"{Fore.RED} N'avons pas compris votre demande{Fore.RESET}")
        direction()

def partie():
    global victoire
    while not victoire : 
        if random.random() > 0.9 :
            combat_ou_pacification_boss()
        else :
            combat_ou_pacification_monstre()

def aleatoire_map():
    map_combat = ["fôret", "plage", "air"]
    return random.choice(map_combat)

def items_foret():
    object_frt = ["baton", "feu", "couteau"]
    return random.choice(object_frt)

def items_plage():
    object_plg = ["baton", "feu", "couteau"]
    return random.choice(object_plg)

objet_plg = items_plage()

def svg(user_name, user_choice, map_aleatoire):
    with open("sauvegarde.txt", "w") as file:
        file.write(f"{user_name}\n{user_choice}\n{map_aleatoire}\n")

print(f'''{Fore.GREEN}
 ██████╗  █████╗ ███╗   ███╗███████╗    ██████╗ ██████╗  ██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔══██╗██╔══██╗██╔════╝ 
██║  ███╗███████║██╔████╔██║█████╗      ██████╔╝██████╔╝██║  ███╗
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██╔══██╗██╔═══╝ ██║   ██║
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ██║  ██║██║     ╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝      ╚═════╝ 
{Fore.RESET}'''
)

time.sleep(2)

while True:
    choix = menu()
    map_aleatoire = aleatoire_map()

    if choix == "1":
        user_name = input("Veuillez entrer votre pseudo : ")
        print(f"Bienvenue, {user_name}! ")
        introduction()
        direction()
        if map_aleatoire == "fôret":
            print(f"Vous êtes actuellement dans la fôret {user_name} , tuer le boss pour gagner")
            svg(user_name, choix, map_aleatoire)

        elif map_aleatoire == "plage":
            print(f"Vous êtes actuellement à la plage {user_name} , tuer le boss pour gagner")
            question = input("Vous possédez d'une boite mystére pour combattre facilment le boss. "
                             "Souhaitez-vous l'ouvrir ? Oui/Non ")
            if question.lower() == "oui":
                print(f"{objet_plg}")
            svg(user_name, choix, map_aleatoire)

        elif map_aleatoire == "air":
            print(f"Vous êtes dans les airs {user_name} , tuer le boss pour gagner")
            svg(user_name, choix, map_aleatoire)
        
        partie()

    if choix == "2":
        with open("sauvegarde.txt", "r") as file:
            infos = file.read()
            infos = infos.split('\n')
            user_name = infos[0]
            user_choice = infos[1]
            map_aleatoire = infos[2]
        
        partie()

    if choix == "3":
        print(f'{Fore.RED}Le but du jeu est de tuer le boss.\n Vous pouvez rencontrer 3 ennemis différents :\n Pilleur : Facile à combattre, dur à convaincre\n Mercenaire : Dur à combattre, facile à convaincre\n Mendiant : Facile à combattre, facile à convaincre\n Gagnez 100 points de puissance pour tuer le boss ou 100 points de repentance pour le pacifier.{Fore.RESET}')

    if choix == "4":
        print(f"{Fore.MAGENTA} Vous avez décidé de quitter le jeu. Votre partie a été sauvegardée{Fore.RESET}")
        time.sleep(2)
        sys.exit()
        svg(user_name, choix, map_aleatoire)
        break

def défaite():
    if pdv <= 0 :
        print("Game over\n vous avez péris") and menu 
