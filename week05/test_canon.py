import unittest
from canon import canon


# just input two random filenames when prompted; they won't affect the tests whatsoever
class TestCanon(unittest.TestCase):
    def test_canon1(self):
        self.assertTrue(canon('test.txt', 'test.txt'))

    def test_canon2(self):
        self.assertTrue(
            canon('..\\..\\..\\..\\.\\.\\Users\\bob\\test.txt', 'test.txt'))

    def test_canon3(self):
        self.assertTrue(canon('C:\\Users\\bob\\test.txt', 'test.txt'))

    def test_canon4(self):
        self.assertFalse(canon('test.txt', 'script.py'))

    def test_canon5(self):
        self.assertTrue(canon('test.txt', '.\\.\\.\\.\\.\\.\\test.txt'))


if __name__ == '__main__':
    unittest.main()
