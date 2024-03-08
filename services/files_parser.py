from models.accounts import Accounts
from models.users import Users

from .hash import HashModule


class File(object):
    def __init__(self, path: str) -> None:
        self._path = path

    def _read_file(self) -> str:
        """
        Lire le contenu du fichier.
        """
        with open(self._path, "r") as file:
            return file.read()

    def decrypt_rows(self, rows: list[str], key: int) -> list[str]:
        """
        Décrypter les lignes du fichier.
        """
        hash_module = HashModule(key=key)
        return [hash_module.decrypt(r) for r in rows]


class IdentFile(File):
    def __init__(self):
        super().__init__("ident.txt")

    def get_users(self) -> Users:
        """
        Obtenir la liste des utilisateurs du fichier.
        """
        content = self._read_file()
        rows = content.split("\n")
        hashed_users = [u.split("*") for u in rows]
        users_list = [self.decrypt_rows(rows=u, key=23) for u in hashed_users]

        return Users(users_list)


class UserFile(File):
    def __init__(self, user: dict):
        self._user = user
        super().__init__(f"users/{user['id']}.txt")

    def get_infos(self) -> list[list[str]]:
        """
        Obtenir les informations de l'utilisateur.
        """
        content = self._read_file()
        rows = content.split("\n")
        hashed_infos = [r.split("*") for r in rows]
        return [self.decrypt_rows(rows=i, key=int(self._user["key"])) for i in hashed_infos]

    def get_accounts(self) -> Accounts:
        """
        Obtenir les comptes de l'utilisateur.
        """
        infos = self.get_infos()
        return Accounts(infos)
