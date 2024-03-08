class Users:
    def __init__(self, users: list[list[str]]):
        self._users = [{
            "id": user[0],
            "password": user[1],
            "name": user[2],
            "key": user[3]
        } for user in users]

    def find_by_id(self, user_id: str) -> dict | None:
        """
        Trouver un utilisateur par son identifiant.
        """
        for user in self._users:
            if user["id"] == user_id:
                return user

        return None

    def get_all(self) -> list[dict]:
        """
        Obtenir la liste de tous les utilisateurs.
        """
        return self._users

    def __str__(self) -> str:
        return str(self._users)
