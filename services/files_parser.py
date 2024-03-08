from models.user_model import Users

from .hash import HashModule


class IdentFile:
    def __init__(self, path: str) -> None:
        self._path = path

    def _read_file(self) -> str:
        """
        Lire le contenu du fichier.
        """
        with open(self._path, "r") as file:
            return file.read()

    def decrypt_user(self, hashed_user: list[str]) -> list[str]:
        """
        Décrypter un utilisateur.
        """
        hash_module = HashModule(key=23)
        return [hash_module.decrypt(e) for e in hashed_user]

    def get_users(self) -> Users:
        """
        Obtenir la liste des utilisateurs du fichier.
        """
        content = self._read_file()
        rows = content.split("\n")
        hashed_users = [u.split("*") for u in rows]
        users_list = [self.decrypt_user(u) for u in hashed_users]

        return Users(users_list)
