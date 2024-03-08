
class Accounts:
    def __init__(self, infos: list[list]):
        self._accounts = []
        for a in infos:
            if a[0] == "CPT":
                account = {
                    "name": a[1],
                    "operations": []
                }

                for o in infos:
                    if o[0] == "OPE" and o[3] == a[1]:
                        operation = {
                            "date": o[1],
                            "label": o[2],
                            "account": o[3],
                            "ammount": float(o[4]),
                            "type": o[5],
                            "verified": o[6] == "True",
                            "budget": o[7]
                        }
                        account["operations"].append(operation)

                self._accounts.append(account)

        self.primary_account = self._accounts[0]

    def get_account(self, name: str) -> dict:
        """
        Obtenir un compte.
        """
        return [a for a in self._accounts if a["name"] == name][0]

    def get_balance(self, name: str) -> float:
        """
        Obtenir le solde d'un compte.
        """
        account = self.get_account(name)
        return sum([o["ammount"] for o in account["operations"]])
