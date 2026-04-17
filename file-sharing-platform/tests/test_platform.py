import unittest

from file_sharing.platform import User, File, EncryptedFile


class TestPlatform(unittest.TestCase):

    def test_user_creation(self):
        """
        Тест создания пользователя
        """
        user = User("kseniya", "1234")
        self.assertEqual(user.get_username(), "kseniya")

    def test_file_upload(self):
        """
        Тест загрузки файла
        """
        file = File("doc.txt", "kseniya")
        self.assertEqual(file.upload(), "Файл doc.txt загружен")

    def test_file_encryption(self):
        """
        Тест шифрования файла
        """
        enc_file = EncryptedFile("doc.txt", "kseniya", "key123")
        self.assertEqual(
            enc_file.encrypt(),
            "Файл doc.txt зашифрован ключом key123"
        )


if __name__ == "__main__":
    unittest.main()
