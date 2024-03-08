from services.files_parser import IdentFile


def login_screen():
    print("🏦 Bienvenue dans votre application de Gestion Bancaire ! 🏦")
    print("Veuillez vous identifier...")
    print()

    user_id = input("🆔 Identifiant : ")
    user_password = input("🔑 Mot de passe : ")

    if not user_id or not user_password:
        print("❌ Veuillez remplir tous les champs ! ❌")
        return login_screen()

    if len(user_id) != 8:
        print("❌ L'identifiant doit contenir 8 caractères ! ❌")
        return login_screen()

    if len(user_password) != 6 or not user_password.isdigit():
        print("❌ Le mot de passe doit contenir 6 chiffres ! ❌")
        return login_screen()

    ident = IdentFile("ident.txt")
    users = ident.get_users()

    user = users.find_by_id(user_id)

    if user and user["password"] == user_password:
        print(f"🎉 Bienvenue {user['name']} ! 🎉")
    else:
        print("❌ Identifiant ou mot de passe incorrect ! ❌")
        login_screen()
