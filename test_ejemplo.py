import unittest
from main import a

class Testa(unittest.TestCase):
    def testa(self):
        self.assertEqual(a(), "Ajedrez")

if __name__ == '__main__':
    unittest.main()