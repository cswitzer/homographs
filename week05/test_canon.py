import unittest
from canon import canon


# just input two random filenames when prompted; they won't affect the tests whatsoever
class TestCanon(unittest.TestCase):
    #True Cases (These are homographs)
    def test_canon1(self):
        self.assertTrue(canon('find_me.txt', 'find_me.txt'))

    def test_canon2(self):
        self.assertTrue(canon('find_me.txt', '\\Users\\bob\\find_me.txt'))

    def test_canon3(self):
        self.assertTrue(canon('find_me.txt', '.\\find_me.txt'))

    def test_canon4(self):
        self.assertTrue(canon('find_me.txt', '..\\bob\\find_me.txt'))

    def test_canon5(self):
        self.assertTrue(canon('find_me.txt', '.\\.\\find_me.txt'))

    def test_canon6(self):
        self.assertTrue(canon('find_me.txt', '..\\..\\Users\\bob\\find_me.txt'))

    #False Cases (These are not homographs)
    def test_canon7(self):
        self.assertFalse(canon('find_me.txt', 'find_me2.txt'))

    def test_canon8(self):
        self.assertFalse(canon('find_me.txt', '\\User\\bill\\week05\\find_me.txt'))

    def test_canon9(self):
        self.assertFalse(canon('find_me.txt', '.find_me2.txt'))

    def test_canon10(self):
        self.assertFalse(canon('find_me.txt', '.\\find_me2.txt'))

    def test_canon11(self):
        self.assertFalse(canon('find_me.txt', '..\\bill\\find_me.txt'))

    def test_canon12(self):
        self.assertFalse(canon('find_me.txt', '.\\.\\find_me2.txt'))

    def test_canon13(self):
        self.assertFalse(canon('find_me.txt', '..\\..\\Users\\bill\\find_me.txt'))


if __name__ == '__main__':
    unittest.main()
