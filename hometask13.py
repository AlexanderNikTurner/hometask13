import enchant


class CaesarsCipher:
    """
    Класс описывает шифр Цезаря.
    """

    def __init__(self):
        """Устанавливает атрибуты для объекта CaesarsCipher."""
        self.decrypted_message = None
        self.encrypted_message = None
        self.key = None

    @property
    def key(self):
        """Property для атрибута key."""
        return self._key

    @key.setter
    def key(self, user_key):
        self._key = user_key

    def decrypt(self, encrypted_message: str, crypt_key: int) -> str:
        """
        Метод, расшифровывающий сообщение.
        Args:
            encrypted_message: Зашифрованное сообщение.
            crypt_key: Ключ шифра Цезаря.

        Returns:
            Расшифрованное сообщение.
        """
        self.decrypted_message = ''
        self.encrypted_message = encrypted_message
        self.key = crypt_key
        for symbol in self.encrypted_message:
            if symbol in SYMBOLS:
                symbol_index = SYMBOLS.find(symbol)
                decrypted_index = symbol_index - self.key
                if decrypted_index >= len(SYMBOLS):
                    decrypted_index = decrypted_index - len(SYMBOLS)
                elif decrypted_index < 0:
                    decrypted_index = decrypted_index + len(SYMBOLS)
                self.decrypted_message = (self.decrypted_message +
                                          SYMBOLS[decrypted_index])
            else:
                self.decrypted_message = self.decrypted_message + symbol
        return self.decrypted_message

    def encrypt(self, decrypted_message: str, crypt_key: int) -> str:
        """
        Метод, зашифровывающий сообщение.
        Args:
            decrypted_message: Сообщение, которое нужно зашифровать.
            crypt_key: Ключ шифра Цезаря.

        Returns:
            Зашифрованное сообщение.
        """
        self.encrypted_message = ''
        self.decrypted_message = decrypted_message
        self.key = crypt_key
        for symbol in self.decrypted_message:
            if symbol in SYMBOLS:
                symbol_index = SYMBOLS.find(symbol)
                encrypted_index = symbol_index + self.key
                if encrypted_index >= len(SYMBOLS):
                    encrypted_index = encrypted_index - len(SYMBOLS)
                elif encrypted_index < 0:
                    encrypted_index = encrypted_index + len(SYMBOLS)
                self.encrypted_message = (self.encrypted_message
                                          + SYMBOLS[encrypted_index])
            else:
                self.encrypted_message = self.encrypted_message + symbol
        return self.encrypted_message


eng = enchant.Dict("en_US")
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
note = 'o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D'
result = CaesarsCipher()

for i in range(len(SYMBOLS)):
    result_note = result.decrypt(note, i)
    words_in_note = result_note.split(' ')
    try:
        word_check = [eng.check(word) for word in words_in_note
                      if len(word) > 2]
        if any(word_check) is True:
            break
        result_key = i + 1
    except ValueError:
        continue

print(f'Подобранный ключ: расшифрованный текст\n{result_key}: {result_note}')
print()

path = input('Введите путь к файлу для записи:\n')
with open(path, 'w', encoding='utf-8') as file:
    file.write(f'Подобранный ключ: расшифрованный текст\n'
               f'{result_key}: {result_note}')
