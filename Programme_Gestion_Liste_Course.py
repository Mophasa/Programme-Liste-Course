# 1- Créez une liste nommée « shopping_list » pour stocker les éléments.
shopping_list = []

# 2- Utilisez une boucle while pour créer un menu d’options permettant à l’utilisateur d’ajouter, de supprimer ou d’afficher des éléments de la liste.
def menu():
    max_items = 10
    while True:
        print("\nMenu :")
        print("1. Ajouter un élément (add)")
        print("2. Supprimer un élément (remove)")
        print("3. Afficher les éléments (view)")
        print("4. Quitter (quit)")

# 3- Utilisez la fonction input() pour inviter l’utilisateur à faire une sélection dans le menu.
        choice = input("Veuillez faire votre choix : ").strip().lower()

# 4- Utilisez un bloc if-elif-else pour déterminer la sélection de l’utilisateur et effectuer l’action correspondante.
        if choice == 'add':
            if len(shopping_list) < max_items:  

# 5- Si l’utilisateur sélectionne 'add', utilisez la fonction input() pour inviter l’utilisateur à entrer un élément à ajouter à la liste.
                for i in range(max_items - len(shopping_list)):
                    item = input("Entrez un élément à ajouter à la liste (ou tapez 'stop' pour arrêter) : ").strip()
                    if item.lower() == 'stop':
                        break
                    shopping_list.append(item)
                    print(f"{item} a été ajouté à la liste.")
            else:
                print(f"La liste est pleine. Vous ne pouvez pas ajouter plus de {max_items} éléments.")

# 6- Si l’utilisateur sélectionne 'remove', utilisez la fonction input() pour inviter l’utilisateur à entrer un élément à supprimer de la liste.
            item = input("Entrez un élément à supprimer de la liste : ").strip()
        elif choice == 'remove':          
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} a été supprimé de la liste.")
            else:
                print(f"{item} n'est pas dans la liste.")

# 7- Si l’utilisateur sélectionne « view », utilisez une boucle for pour parcourir la liste des éléments et les afficher à l’utilisateur.
        elif choice == 'view':            
            print("Éléments dans la liste de courses :")
            for idx, item in enumerate(shopping_list, start=1):
                print(f"{idx}. {item}")

        elif choice == 'quit':
            print("Au revoir !")
            break 

        else:
            print("Choix invalide. Veuillez réessayer.") 

# Appel de la fonction menu pour démarrer le programme
menu()