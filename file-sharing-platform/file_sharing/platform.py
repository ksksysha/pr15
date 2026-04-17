class User:
    """
    Класс пользователя системы.
    Хранит имя пользователя и пароль.
    """

    def __init__(self, username, password):
        self._username = username
        self._password = password

    def get_username(self):
        """Возвращает имя пользователя"""
        return self._username


class File:
    """
    Базовый класс файла.
    """

    def __init__(self, file_name, owner):
        self.file_name = file_name
        self.owner = owner

    def upload(self):
        """
        Метод загрузки файла
        """
        return f"Файл {self.file_name} загружен"


class EncryptedFile(File):
    """
    Класс зашифрованного файла.
    Наследуется от File.
    """

    def __init__(self, file_name, owner, key):
        super().__init__(file_name, owner)
        self.key = key

    def encrypt(self):
        """
        Метод шифрования файла
        """
        return f"Файл {self.file_name} зашифрован ключом {self.key}"
