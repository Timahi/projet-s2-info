#! /usr/bin/env python3
from screens.dashboard import dashboard_screen
from screens.login import login_screen


def main():
    user = login_screen()
    choice = dashboard_screen(user)
    match choice:
        case 9:
            print("👋 Au revoir ! 👋")
            main()


if __name__ == "__main__":
    main()
