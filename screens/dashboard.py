from models.accounts import Accounts
from services.files_parser import UserFile


def dashboard_screen(user: dict, acc_input: Accounts | None = None) -> int:
    print("📋 Menu Principal 📋")
    print(f"👤 Connecté en tant que : {user['name']} 👤")
    print()

    if acc_input:
        accounts = acc_input
    else:
        accounts = UserFile(user).get_accounts()

    show_account_resume(accounts)

    print()
    print("1️⃣ Changer de compte principal")
    print("9️⃣ Quitter")
    print()
    choice = int(input("Votre choix : "))

    if choice == 1:
        for i in range(len(accounts._accounts)):
            print(i + 1, ":", accounts._accounts[i]["name"])
        new_account = int(input("Nouveau compte principal : "))
        accounts.primary_account = accounts._accounts[new_account - 1]
        return dashboard_screen(user, accounts)

    return choice


def show_account_resume(accounts_list: Accounts):
    print("🥇 Compte principal :")
    print(accounts_list.primary_account["name"], "•", accounts_list.get_balance(
        accounts_list.primary_account["name"]), "€")
