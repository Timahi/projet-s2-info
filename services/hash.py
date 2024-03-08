class HashModule:
    def __init__(self, key: int) -> None:
        self._key = key

    @staticmethod
    def compare_passwords(password1, password2):
        return password1 == password2

    def _get_character_type(self, ascii_code: int):
        if ascii_code >= 48 and ascii_code <= 57:
            return "number"
        elif ascii_code >= 65 and ascii_code <= 90:
            return "uppercase"
        elif ascii_code >= 97 and ascii_code <= 122:
            return "lowercase"
        else:
            return "other"

    def decrypt(self, hashed_string: str) -> str:
        resolved_string = ""

        for character in hashed_string:
            ascii_code = ord(character)
            character_type = self._get_character_type(ascii_code)

            match character_type:
                case "number":
                    if ascii_code - self._key >= 48:
                        resolved_string += chr(ascii_code - self._key)
                    elif ascii_code - self._key < 48:
                        while ascii_code - self._key < 48:
                            ascii_code += 10
                        resolved_string += chr(ascii_code - self._key)

                case "uppercase":
                    if ascii_code - self._key >= 65:
                        resolved_string += chr(ascii_code - self._key)
                    elif ascii_code - self._key < 65:
                        while ascii_code - self._key < 65:
                            ascii_code += 26
                        resolved_string += chr(ascii_code - self._key)

                case "lowercase":
                    if ascii_code - self._key >= 97:
                        resolved_string += chr(ascii_code - self._key)
                    elif ascii_code - self._key < 97:
                        while ascii_code - self._key < 97:
                            ascii_code += 26
                        resolved_string += chr(ascii_code - self._key)

                case "other":
                    resolved_string += character

        return resolved_string
